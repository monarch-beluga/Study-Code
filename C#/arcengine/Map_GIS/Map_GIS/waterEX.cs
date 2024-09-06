using System;
using System.Collections.Generic;
using System.Linq;
using System.Windows.Forms;
using System.IO;

using ESRI.ArcGIS.esriSystem;
using ESRI.ArcGIS.Controls;
using ESRI.ArcGIS.Geometry;
using ESRI.ArcGIS.DataManagementTools;
using ESRI.ArcGIS.Geoprocessor;
using ESRI.ArcGIS.Geoprocessing;
using ESRI.ArcGIS.AnalysisTools;
using ESRI.ArcGIS.CartographyTools;
using ESRI.ArcGIS.EditingTools;
using ESRI.ArcGIS.Carto;

namespace Map_GIS
{
    public partial class waterEX : Form
    {
        public RichTextBox showinfo;
        public AxMapControl axMapControl1;
        private Queue<IGPProcess> _myGPToolsToExecute;
        private Geoprocessor GP;
        private int toolNums;
        public string sy_path;
        public string ly_path;

        public waterEX()
        {
            InitializeComponent();
        }

        public waterEX(RichTextBox showinfo, AxMapControl axMapControl1)
        {
            InitializeComponent();
            this.showinfo = showinfo;
            this.axMapControl1 = axMapControl1;
            comboBox1.DataSource = System.Enum.GetNames(typeof(riverDirection));
        }

        public enum riverDirection
        {
            未定义=0,向东=1,向西=2,向南=3,向北=4
        }

        private void button1_Click(object sender, EventArgs e)
        {
            String filename = Common.openFile(openFileDialog1, "矢量文件 (*.*)|*.shp");
            if (filename.Trim() != "")
            {
                textBox1.Text = filename;
                if (checkBox1.Checked)
                {
                    ILayer player = Common.LoadShpFile(filename);
                    axMapControl1.AddLayer(player, 0);
                    Common.message_show(showinfo, 1, "三调数据加载成功");
                }
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            String filename = Common.openFile(openFileDialog1, "矢量文件 (*.*)|*.shp");
            if (filename.Trim() != "")
            {
                textBox2.Text = filename;
                if (checkBox2.Checked)
                {
                    ILayer player = Common.LoadShpFile(filename);
                    axMapControl1.AddLayer(player, 0);
                    Common.message_show(showinfo, 1, "取水口数据加载成功");
                }
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            string filename = Common.openFile(openFileDialog1, "矢量文件 (*.*)|*.shp");
            if (filename.Trim() != "")
            {
                textBox3.Text = filename;
                if (checkBox3.Checked)
                {
                    ILayer player = Common.LoadShpFile(filename);
                    axMapControl1.AddLayer(player, 0);
                    Common.message_show(showinfo, 1, "分水岭数据加载成功");
                }
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            string filename = Common.saveFile(saveFileDialog1, "矢量文件 (*.*)|*.shp");
            if (filename.Trim() != "")
                textBox5.Text = filename;
        }

        private void button6_Click(object sender, EventArgs e)
        {
            this.Visible = false;
            string sd_path = textBox1.Text;
            string point_path = textBox2.Text;
            string fsl_path = textBox3.Text;

            if (sd_path.Trim() == "")
            {
                MessageBox.Show("未指定三调数据");
                return;
            }

            if (point_path.Trim() == "")
            {
                MessageBox.Show("未指定取水口数据");
                return;
            }

            if (fsl_path.Trim() == "")
            {
                MessageBox.Show("未指定分水岭数据");
                return;
            }

            string sd_file = System.IO.Path.GetFileName(sd_path);
            string point_file = System.IO.Path.GetFileName(point_path);
            string fsl_file = System.IO.Path.GetFileName(fsl_path);

            string strUpStreamDis = textBox6.Text;
            string strDownStreamDis = textBox7.Text;

            if (strUpStreamDis.Trim() == "")
            {
                MessageBox.Show("未指定上游河距据");
                return;
            }

            if (strDownStreamDis.Trim() == "")
            {
                MessageBox.Show("未指定下游河距据");
                return;
            }

            int intUpStreamDis = int.Parse(strUpStreamDis);
            int intDownStreamDis = int.Parse(strDownStreamDis);
            int intUpStreamDisPlus = intUpStreamDis + 100;

            int flowDirection = comboBox1.SelectedIndex;
            if (flowDirection==0)
            {
                MessageBox.Show("河流流向");
                return;
            }
            
            sy_path = textBox5.Text;
            if (sy_path.Trim() == "")
            {
                MessageBox.Show("未指定水域输出数据");
                return;
            }

            ly_path = textBox8.Text;
            if (ly_path.Trim() == "")
            {
                MessageBox.Show("未指定陆域输出数据");
                return;
            }

            string tempFolder = System.IO.Path.GetDirectoryName(sy_path) + "\\temp";
            if (!Directory.Exists(tempFolder))
                Directory.CreateDirectory(tempFolder);

            string po_prj = string.Format("{0}\\pro_{1}", tempFolder, point_file);
            string sd_prj = string.Format("{0}\\pro_{1}", tempFolder, sd_file);
            string fsl_prj = string.Format("{0}\\pro_{1}", tempFolder, fsl_file);

            string buffUp = string.Format("{0}\\buff_{1}.shp", tempFolder, intUpStreamDis);
            string buffUpPlus = string.Format("{0}\\buff_{1}.shp", tempFolder, intUpStreamDisPlus);
            string buffDown = string.Format("{0}\\buff_{1}.shp", tempFolder, intDownStreamDis);

            string clipUpPlus = string.Format("{0}\\clip_{1}.shp", tempFolder, intUpStreamDisPlus);

            string riverUpPlus = string.Format("{0}\\HL_{1}.shp", tempFolder, intUpStreamDisPlus);

            string riverAggUpPlus = string.Format("{0}\\HL_{1}_agg.shp", tempFolder, intUpStreamDisPlus);

            string riverJoinUpPlus = string.Format("{0}\\HL_{1}_join.shp", tempFolder, intUpStreamDisPlus);

            string riverSelectPlus = string.Format("{0}\\HL_{1}_select.shp", tempFolder, intUpStreamDisPlus);

            string riverEliPlus = string.Format("{0}\\HL_{1}_eli.shp", tempFolder, intUpStreamDisPlus);

            string riverLinePlus = string.Format("{0}\\HL_{1}_line.shp", tempFolder, intUpStreamDisPlus);

            string riverLineUp = string.Format("{0}\\HL_{1}_line.shp", tempFolder, intUpStreamDis);

            string tolerance = "100 Meters";
            string riverLineSimp = string.Format("{0}\\HL_{1}_sim.shp", tempFolder, intUpStreamDis);

            string CEMaxWidth = textBox9.Text + " Meters";
            string riverCenterLine = string.Format("{0}\\HL_CE_{1}_line.shp", tempFolder, intUpStreamDis);

            string riverCenterLineDown = string.Format("{0}\\HL_CE_{1}_line.shp", tempFolder, intDownStreamDis);

            string startEndPoint = "start_and_end_point";
            string pointMerge = "point_merge";

            string downPoint = string.Format("{0}\\point_DJ.shp", tempFolder);

            string riverBuffer = string.Format("{0}\\HL_CE_{1}_buff.shp", tempFolder, intUpStreamDis);

            string riverBufferClip = string.Format("{0}\\HL_CE_{1}_buff_clip.shp", tempFolder, intUpStreamDis);

            string riverBufferLine = string.Format("{0}\\HL_CE_{1}_buff_line.shp", tempFolder, intUpStreamDis);

            string downPointToRiver = string.Format("{0}\\CX_line.shp", tempFolder);

            string riverCenterExtend = string.Format("{0}\\CX_line_merge.shp", tempFolder);

            string extendLen = "1000 Meters";

            string rodeShp = string.Format("{0}\\rode.shp", tempFolder);

            string rodeLine = string.Format("{0}\\rode_line.shp", tempFolder);

            string rodeDiss = string.Format("{0}\\rode_diss.shp", tempFolder);

            string rodeLineClip = string.Format("{0}\\rode_line_clip.shp", tempFolder);

            string rodeMerge = string.Format("{0}\\rode_merge.shp", tempFolder);

            string rodeAndBuff = string.Format("{0}\\rode_and_buff.shp", tempFolder);

            string fslLine = string.Format("{0}\\fsl_line.shp", tempFolder);

            string fslLineClip = string.Format("{0}\\fsl_line_clip.shp", tempFolder);

            string riverEli = string.Format("{0}\\HL_{1}_eli.shp", tempFolder, intUpStreamDis);

            string fslAndRiver = string.Format("{0}\\fsl_and_river.shp", tempFolder);

            string fslDelRiver = string.Format("{0}\\fsl_diff_river.shp", tempFolder);

            string lyLine = string.Format("{0}\\ly_line.shp", tempFolder);
            string lyMain = string.Format("{0}\\ly_main.shp", tempFolder);
            string lyPoJoin = string.Format("{0}\\ly_po_join.shp", tempFolder);
            string lySelect = string.Format("{0}\\ly_select.shp", tempFolder);
            string lyNoEli = string.Format("{0}\\ly_select1.shp", tempFolder);
            
            GP = new Geoprocessor();
            GP.OverwriteOutput = true;
            _myGPToolsToExecute = new Queue<IGPProcess>();

            if (!Directory.Exists(tempFolder + "\\sy_temp.gdb"))
            {
                CreateFileGDB createFileTool;
                createFileTool = new CreateFileGDB(tempFolder, "sy_temp.gdb");
                GP.Execute(createFileTool, null);
            }

            GP.SetEnvironmentValue("workspace", tempFolder + "\\sy_temp.gdb");
            GP.ToolExecuting += new EventHandler<ToolExecutingEventArgs>(gp_ToolExecuting);
            GP.ToolExecuted += new EventHandler<ToolExecutedEventArgs>(gp_ToolExecuted);

            ISpatialReferenceFactory pSpatialReferenceFactory = new SpatialReferenceEnvironmentClass();
            ISpatialReference spatial_ref = pSpatialReferenceFactory.CreateProjectedCoordinateSystem(3857);
            Project projectTool;
            projectTool = new Project(point_path, po_prj, spatial_ref);
            _myGPToolsToExecute.Enqueue(projectTool);
            projectTool = new Project(fsl_path, fsl_prj, spatial_ref);
            _myGPToolsToExecute.Enqueue(projectTool);

            ESRI.ArcGIS.AnalysisTools.Buffer bufferTool;
            bufferTool = new ESRI.ArcGIS.AnalysisTools.Buffer(po_prj, buffUp, string.Format("{0} Meters", intUpStreamDis));
            _myGPToolsToExecute.Enqueue(bufferTool);
            bufferTool = new ESRI.ArcGIS.AnalysisTools.Buffer(po_prj, buffUpPlus, string.Format("{0} Meters", intUpStreamDisPlus));
            _myGPToolsToExecute.Enqueue(bufferTool);
            bufferTool = new ESRI.ArcGIS.AnalysisTools.Buffer(po_prj, buffDown, string.Format("{0} Meters", intDownStreamDis));
            _myGPToolsToExecute.Enqueue(bufferTool);

            ESRI.ArcGIS.AnalysisTools.Clip clipTool;
            clipTool = new ESRI.ArcGIS.AnalysisTools.Clip(sd_path, buffUpPlus, sd_prj);
            _myGPToolsToExecute.Enqueue(clipTool);

            projectTool = new Project(sd_prj, clipUpPlus, spatial_ref);
            _myGPToolsToExecute.Enqueue(projectTool);

            // 筛选河流
            ESRI.ArcGIS.AnalysisTools.Select selectTool;
            selectTool = new ESRI.ArcGIS.AnalysisTools.Select(clipUpPlus, riverUpPlus);
            selectTool.where_clause = "\"DLBM\" = '1101'";
            _myGPToolsToExecute.Enqueue(selectTool);

            // 聚合
            AggregatePolygons aggTool;
            aggTool = new AggregatePolygons(riverUpPlus, riverAggUpPlus, "40 Meters");
            _myGPToolsToExecute.Enqueue(aggTool);

            // 连接取水点
            SpatialJoin spatialJoinTool;
            spatialJoinTool = new SpatialJoin(riverAggUpPlus, po_prj, riverJoinUpPlus);
            _myGPToolsToExecute.Enqueue(spatialJoinTool);

            // 筛选与取水点连接的河流
            selectTool = new ESRI.ArcGIS.AnalysisTools.Select(riverJoinUpPlus, riverSelectPlus);
            selectTool.where_clause = "\"Join_Count\" = 1";
            _myGPToolsToExecute.Enqueue(selectTool);

            EliminatePolygonPart eliTool;
            eliTool = new EliminatePolygonPart(riverSelectPlus, riverEliPlus);
            eliTool.condition = "PERCENT";
            eliTool.part_area_percent = 99.9;
            _myGPToolsToExecute.Enqueue(eliTool);

            FeatureToLine featureToLineTool;
            featureToLineTool = new FeatureToLine(riverEliPlus, riverLinePlus);
            _myGPToolsToExecute.Enqueue(featureToLineTool);

            clipTool = new ESRI.ArcGIS.AnalysisTools.Clip(riverLinePlus, buffUp, riverLineUp);
            _myGPToolsToExecute.Enqueue(clipTool);

            SimplifyLine simpLineTool;
            simpLineTool = new SimplifyLine(riverLineUp, riverLineSimp, "POINT_REMOVE", tolerance);
            _myGPToolsToExecute.Enqueue(simpLineTool);

            CollapseDualLinesToCenterline CDLTCTool;
            CDLTCTool = new CollapseDualLinesToCenterline(riverLineSimp, riverCenterLine, CEMaxWidth);
            _myGPToolsToExecute.Enqueue(CDLTCTool);

            clipTool = new ESRI.ArcGIS.AnalysisTools.Clip(riverCenterLine, buffDown, riverCenterLineDown);
            _myGPToolsToExecute.Enqueue(clipTool);

            FeatureVerticesToPoints FVTPTool;
            FVTPTool = new FeatureVerticesToPoints(riverCenterLineDown, startEndPoint);
            FVTPTool.point_location = "DANGLE";
            _myGPToolsToExecute.Enqueue(FVTPTool);

            Merge mergeTool;
            mergeTool = new Merge(string.Format("{0};{1}", startEndPoint, po_prj), pointMerge);
            _myGPToolsToExecute.Enqueue(mergeTool);

            AddXY addXYTool;
            addXYTool = new AddXY(pointMerge);
            _myGPToolsToExecute.Enqueue(addXYTool);

            selectTool = new ESRI.ArcGIS.AnalysisTools.Select(pointMerge, downPoint);
            switch (flowDirection)
            {
                case 1:
                    selectTool.where_clause = string.Format("POINT_X = (SELECT MAX( POINT_X ) FROM {0})", pointMerge);
                    break;
                case 2:
                    selectTool.where_clause = string.Format("POINT_X = (SELECT MIN( POINT_X ) FROM {0})", pointMerge);
                    break;
                case 3:
                    selectTool.where_clause = string.Format("POINT_Y = (SELECT MIN( POINT_Y ) FROM {0})", pointMerge);
                    break;
                case 4:
                    selectTool.where_clause = string.Format("POINT_Y = (SELECT MAX( POINT_Y ) FROM {0})", pointMerge);
                    break;
            }
            _myGPToolsToExecute.Enqueue(selectTool);

            bufferTool = new ESRI.ArcGIS.AnalysisTools.Buffer(riverAggUpPlus, riverBuffer, "400 Meters");
            bufferTool.dissolve_option = "ALL";
            _myGPToolsToExecute.Enqueue(bufferTool);


            clipTool = new ESRI.ArcGIS.AnalysisTools.Clip(riverBuffer, buffUp, riverBufferClip);
            _myGPToolsToExecute.Enqueue(clipTool);

            featureToLineTool = new FeatureToLine(riverBufferClip, riverBufferLine);
            _myGPToolsToExecute.Enqueue(featureToLineTool);

            Near nearTool;
            nearTool = new Near(downPoint, riverLineUp);
            nearTool.location = "LOCATION";
            nearTool.angle = "NO_ANGLE";
            _myGPToolsToExecute.Enqueue(nearTool);

            XYToLine xyToLineTool;
            xyToLineTool = new XYToLine(downPoint, downPointToRiver, "NEAR_X", "NEAR_Y", "POINT_X", "POINT_Y");
            xyToLineTool.line_type = "1";
            xyToLineTool.spatial_reference = spatial_ref;
            _myGPToolsToExecute.Enqueue(xyToLineTool);

            mergeTool = new Merge(string.Format("{0};{1}", downPointToRiver, riverBufferLine), riverCenterExtend);
            _myGPToolsToExecute.Enqueue(mergeTool);

            ExtendLine extendLineTool;
            extendLineTool = new ExtendLine(riverCenterExtend);
            extendLineTool.extend_to = "EXTENSION";
            extendLineTool.length = extendLen;
            _myGPToolsToExecute.Enqueue(extendLineTool);

            selectTool = new ESRI.ArcGIS.AnalysisTools.Select(clipUpPlus, rodeShp);
            selectTool.where_clause = "\"DLBM\" = '1006'";
            _myGPToolsToExecute.Enqueue(selectTool);

            featureToLineTool = new FeatureToLine(rodeShp, rodeLine);
            _myGPToolsToExecute.Enqueue(featureToLineTool);

            Dissolve dissolveTool;
            dissolveTool = new Dissolve(rodeLine, rodeDiss);
            _myGPToolsToExecute.Enqueue(dissolveTool);

            Integrate integrateTool;
            integrateTool = new Integrate(rodeDiss);
            integrateTool.cluster_tolerance = "5 Meters";
            _myGPToolsToExecute.Enqueue(integrateTool);

            clipTool = new ESRI.ArcGIS.AnalysisTools.Clip(rodeDiss, riverBufferClip, rodeLineClip);
            _myGPToolsToExecute.Enqueue(clipTool);
            
            mergeTool = new Merge(string.Format("{0};{1}", rodeLineClip, riverBufferLine), rodeMerge);
            _myGPToolsToExecute.Enqueue(mergeTool);

            dissolveTool = new Dissolve(rodeMerge, rodeAndBuff);
            dissolveTool.dissolve_field = "FID";
            _myGPToolsToExecute.Enqueue(dissolveTool);

            extendLineTool = new ExtendLine(rodeAndBuff);
            extendLineTool.length = "80 Meters";
            _myGPToolsToExecute.Enqueue(extendLineTool);

            featureToLineTool = new FeatureToLine(fsl_prj, fslLine);
            _myGPToolsToExecute.Enqueue(featureToLineTool);

            clipTool = new ESRI.ArcGIS.AnalysisTools.Clip(fslLine, riverBufferClip, fslLineClip);
            _myGPToolsToExecute.Enqueue(clipTool);

            
            clipTool = new ESRI.ArcGIS.AnalysisTools.Clip(riverEliPlus, buffUp, riverEli);
            _myGPToolsToExecute.Enqueue(clipTool);

            
            clipTool = new ESRI.ArcGIS.AnalysisTools.Clip(fslLine, riverEli, fslAndRiver);
            _myGPToolsToExecute.Enqueue(clipTool);

            
            SymDiff symDiffTool;
            symDiffTool = new SymDiff(fslAndRiver, fslLineClip, fslDelRiver);
            _myGPToolsToExecute.Enqueue(symDiffTool);


            mergeTool = new Merge(string.Format("{0};{1};{2}", fslDelRiver, rodeAndBuff, riverCenterExtend), lyLine);
            _myGPToolsToExecute.Enqueue(mergeTool);

            extendLineTool = new ExtendLine(lyLine);
            extendLineTool.extend_to = "EXTENSION";
            extendLineTool.length = "5 Meters";
            _myGPToolsToExecute.Enqueue(extendLineTool);
            
            FeatureToPolygon featureToPolyTool;
            featureToPolyTool = new FeatureToPolygon(lyLine, lyMain);
            _myGPToolsToExecute.Enqueue(featureToPolyTool);
            
            spatialJoinTool = new SpatialJoin(lyMain, po_prj, lyPoJoin);
            _myGPToolsToExecute.Enqueue(spatialJoinTool);
            
            selectTool = new ESRI.ArcGIS.AnalysisTools.Select(lyPoJoin, lySelect);
            selectTool.where_clause = "\"Join_Count\" = 1";
            _myGPToolsToExecute.Enqueue(selectTool);

            clipTool = new ESRI.ArcGIS.AnalysisTools.Clip(lySelect, riverEli, sy_path);
            _myGPToolsToExecute.Enqueue(clipTool);

            symDiffTool = new SymDiff(lySelect, sy_path, lyNoEli);
            _myGPToolsToExecute.Enqueue(symDiffTool);

            eliTool = new EliminatePolygonPart(lyNoEli, ly_path);
            eliTool.part_area_percent = 5;
            eliTool.condition = "PERCENT";
            _myGPToolsToExecute.Enqueue(eliTool);

            toolNums = _myGPToolsToExecute.Count();
            GP.ExecuteAsync(_myGPToolsToExecute.Dequeue());
        }

        private void gp_ToolExecuted(object sender, ToolExecutedEventArgs e)
        {
            IGeoProcessorResult2 gpResult = (IGeoProcessorResult2)e.GPResult;

            if (e.GPResult.Status == esriJobStatus.esriJobSucceeded)
            {
                //IFeatureLayer player = new FeatureLayerClass();
                //player.FeatureClass = GP.Open(gpResult.GetOutput(0)) as IFeatureClass;
                //axMapControl1.AddLayer(player as ILayer);
                int current = toolNums - _myGPToolsToExecute.Count;
                Common.message_show(showinfo, 1, string.Format("{0}/{1}:{2} Succeeded!", current, toolNums, gpResult.Process.Tool.Name));
                System.Runtime.InteropServices.Marshal.ReleaseComObject(gpResult);
                //判断队列里是否还有工具，如果有继续执行
                if (_myGPToolsToExecute.Count > 0)
                {
                    GP.ExecuteAsync(_myGPToolsToExecute.Dequeue());
                }
                else
                {
                    string pFolder = System.IO.Path.GetDirectoryName(sy_path);
                    string pFile = System.IO.Path.GetFileName(sy_path);
                    axMapControl1.AddShapeFile(pFolder, pFile);
                    pFolder = System.IO.Path.GetDirectoryName(ly_path);
                    pFile = System.IO.Path.GetFileName(ly_path);
                    axMapControl1.AddShapeFile(pFolder, pFile);
                    Common.message_show(showinfo, 1, "水源保护区提取成功");
                    Common.DeleteDirectory(pFolder + "\\temp");
                    this.Close();
                }
            }
            else if (gpResult.Status == esriJobStatus.esriJobFailed)
            {
                Common.message_show(showinfo, 4, "水源保护区提取失败");
                string pFolder = System.IO.Path.GetDirectoryName(sy_path);
                if (!Directory.Exists(pFolder + "\\temp"))
                    Common.DeleteDirectory(pFolder + "\\temp");
                this.Visible = true;
            }
        }

        private void gp_ToolExecuting(object sender, ToolExecutingEventArgs e)
        {
            IGeoProcessorResult2 gpResult = (IGeoProcessorResult2)e.GPResult;
            Common.message_show(showinfo, 2, string.Format("{0} Executing……", gpResult.Process.Tool.Name));
        }    

        private void button7_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void button8_Click(object sender, EventArgs e)
        {
            String filename = Common.saveFile(saveFileDialog1, "矢量文件 (*.*)|*.shp");
            if (filename.Trim() != "")
                textBox8.Text = filename;
        }
        

    }
}
