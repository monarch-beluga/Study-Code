using System;
using System.Windows.Forms;
using System.IO;

using ESRI.ArcGIS.Carto;
using ESRI.ArcGIS.Controls;
using ESRI.ArcGIS.SystemUI;

namespace Map_GIS
{
    public sealed partial class MainForm : Form
    {
        #region class private members
        private IMapControl3 m_mapControl = null;
        private string m_mapDocumentName = string.Empty;
        #endregion

        #region class constructor
        public MainForm()
        {
            InitializeComponent();
        }
        #endregion

        private void MainForm_Load(object sender, EventArgs e)
        {
            //get the MapControl
            m_mapControl = (IMapControl3)axMapControl1.Object;

            //disable the Save menu (since there is no document yet)
            menuSaveDoc.Enabled = false;

            axMapControl1.Map.Name = "Map";

            Common.message_show(richTextBox1, 2, "欢迎使用本程序");
        }

        #region Main Menu event handlers
        private void menuNewDoc_Click(object sender, EventArgs e)
        {
            //execute New Document command
            ICommand command = new CreateNewDocument();
            command.OnCreate(m_mapControl.Object);
            command.OnClick();
        }

        private void menuOpenDoc_Click(object sender, EventArgs e)
        {
            //execute Open Document command
            ICommand command = new ControlsOpenDocCommandClass();
            command.OnCreate(m_mapControl.Object);
            command.OnClick();
        }

        private void menuSaveDoc_Click(object sender, EventArgs e)
        {
            //execute Save Document command
            if (m_mapControl.CheckMxFile(m_mapDocumentName))
            {
                //create a new instance of a MapDocument
                IMapDocument mapDoc = new MapDocumentClass();
                mapDoc.Open(m_mapDocumentName, string.Empty);

                //Make sure that the MapDocument is not readonly
                if (mapDoc.get_IsReadOnly(m_mapDocumentName))
                {
                    MessageBox.Show("Map document is read only!");
                    mapDoc.Close();
                    return;
                }

                //Replace its contents with the current map
                mapDoc.ReplaceContents((IMxdContents)m_mapControl.Map);

                //save the MapDocument in order to persist it
                mapDoc.Save(mapDoc.UsesRelativePaths, false);

                //close the MapDocument
                mapDoc.Close();
            }
        }

        private void menuSaveAs_Click(object sender, EventArgs e)
        {
            //execute SaveAs Document command
            ICommand command = new ControlsSaveAsDocCommandClass();
            command.OnCreate(m_mapControl.Object);
            command.OnClick();
        }

        private void menuExitApp_Click(object sender, EventArgs e)
        {
            //exit the application
            Application.Exit();
        }
        #endregion

        //listen to MapReplaced evant in order to update the statusbar and the Save menu
        private void axMapControl1_OnMapReplaced(object sender, IMapControlEvents2_OnMapReplacedEvent e)
        {
            //get the current document name from the MapControl
            m_mapDocumentName = m_mapControl.DocumentFilename;

            //if there is no MapDocument, diable the Save menu and clear the statusbar
            if (m_mapDocumentName == string.Empty)
            {
                menuSaveDoc.Enabled = false;
                statusBarXY.Text = string.Empty;
            }
            else
            {
                //enable the Save manu and write the doc name to the statusbar
                menuSaveDoc.Enabled = true;
                statusBarXY.Text = Path.GetFileName(m_mapDocumentName);
            }
        }

        private void axMapControl1_OnMouseMove(object sender, IMapControlEvents2_OnMouseMoveEvent e)
        {
            statusBarXY.Text = string.Format("{0}, {1}  {2}", e.mapX.ToString("#######.##"), e.mapY.ToString("#######.##"), axMapControl1.MapUnits.ToString().Substring(4));
        }

        private void waterEXToolStripMenuItem_Click(object sender, EventArgs e)
        {
            waterEX water_form = new waterEX(richTextBox1, axMapControl1);
            water_form.Show();
        }

        private void axMapControl1_OnOleDrop(object sender, IMapControlEvents2_OnOleDropEvent e)
        {
            IDataObjectHelper pDataObjectHelper = e.dataObjectHelper as IDataObjectHelper;
            if (e.dropAction == esriControlsDropAction.esriDropped)
            {
                System.Array array = pDataObjectHelper.GetFiles() as System.Array;
                for (int i = 0; i < array.Length; i++)
                {
                    AddData(array.GetValue(i).ToString());
                }
                axMapControl1.Extent = axMapControl1.FullExtent;
            }
        }

        private void AddData(string filePath)
        {
            string fileExtension = System.IO.Path.GetExtension(filePath);
            switch (fileExtension)
            {
                case ".tif":
                    {
                        ILayer player = Common.LoadRaster(filePath);
                        axMapControl1.AddLayer(player, 0);
                    }
                    break;
                case ".shp":
                    {
                        ILayer player = Common.LoadShpFile(filePath);
                        axMapControl1.AddLayer(player, 0);
                    }
                    break;
                default:
                    {
                        Common.message_show(richTextBox1, 4, "不支持此数据打开");
                    }
                    break;
            }
        }
    }
}