using ESRI.ArcGIS.Controls;
using ESRI.ArcGIS.DataManagementTools;
using ESRI.ArcGIS.Geoprocessor;
using ESRI.ArcGIS.SpatialAnalystTools;
using Map_GIS;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace DroneMap.Forms
{
    public partial class CutFillForm : Form
    {
        public RichTextBox showinfo;
        public AxMapControl axMapControl1;

        public CutFillForm(AxMapControl axMapControl1, RichTextBox showinfo)
        {
            InitializeComponent();
            this.axMapControl1 = axMapControl1;
            this.showinfo = showinfo;
        }

        private void beforeRasterBtn_Click(object sender, EventArgs e)
        {
            String fileName = Common.openFile(openFileDialog1, "栅格文件|*.tif;*.img|全部文件|*.*");
            if (fileName.Trim() != "")
                beforeRasterText.Text = fileName;
        }

        private void afterRasterBtn_Click(object sender, EventArgs e)
        {
            String fileName = Common.openFile(openFileDialog1, "栅格文件|*.tif;*.img|全部文件|*.*");
            if (fileName.Trim() != "")
                afterRasterText.Text = fileName;
        }

        private void roiFileBtn_Click(object sender, EventArgs e)
        {
            String fileName = Common.openFile(openFileDialog1, "矢量文件|*.shp|全部文件|*.*");
            if (fileName.Trim() != "")
                roiFileText.Text = fileName;
        }

        private void outFileBtn_Click(object sender, EventArgs e)
        {
            String fileName = Common.saveFile(saveFileDialog1, "栅格文件|*.tif;*.img|全部文件|*.*");
            if (fileName.Trim() != "")
                outFileText.Text = fileName;
        }

        private void executeCMD(String path, String cmd)
        {
            Process p = new Process();
            p.StartInfo.FileName = "cmd.exe";
            p.StartInfo.Arguments = "/c " + cmd;
            p.StartInfo.WorkingDirectory = path;
            p.StartInfo.UseShellExecute = false;
            p.StartInfo.RedirectStandardInput = true;
            p.StartInfo.RedirectStandardOutput = true;
            p.StartInfo.RedirectStandardError = true;
            p.StartInfo.CreateNoWindow = true;
            p.StartInfo.WindowStyle = ProcessWindowStyle.Hidden;

            p.Start();
            p.WaitForExit();
            p.Close();
        }

        private void executeBtn_Click(object sender, EventArgs e)
        {
            var beforeFile = beforeRasterText.Text;
            var afterFile = afterRasterText.Text;
            var outFile = outFileText.Text;
            var roiFile = roiFileText.Text;

            var outPath = System.IO.Path.GetDirectoryName(outFile);
            var workPath = outPath + "\\temp";
            if (!System.IO.Directory.Exists(workPath))
                System.IO.Directory.CreateDirectory(workPath);
            Common.message_show(showinfo, 2, "临时工作空间创建完成！");

            var beforeRaster = workPath + "\\before.tif";
            var afterRaster = workPath + "\\after.tif";

            Geoprocessor GP = new Geoprocessor();
            GP.SetEnvironmentValue("nodata", "MINIMUM");
            GP.OverwriteOutput = true;

            Clip clipTool = new Clip();
            clipTool.in_raster = beforeFile;
            clipTool.out_raster = beforeRaster;
            clipTool.in_template_dataset = roiFile;
            clipTool.clipping_geometry = "ClippingGeometry";
            GP.Execute(clipTool, null);

            clipTool.in_raster = afterFile;
            clipTool.out_raster = afterRaster;
            clipTool.in_template_dataset = roiFile;
            clipTool.clipping_geometry = "ClippingGeometry";
            GP.Execute(clipTool, null);

            Minus minusTool = new Minus(afterRaster, beforeRaster, outFile);
            GP.Execute(minusTool, null);

            executeCMD(Common.AppStartPath + "\\ODM\\venv", $"python ../cutfill.py {outFile}");
            Common.DeleteDirectory(workPath);
            Common.message_show(showinfo, 1, "填挖方计算完成！");
        }
    }
}
