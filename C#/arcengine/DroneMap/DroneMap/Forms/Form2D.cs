using System;
using System.Windows.Forms;
using System.IO;

using ESRI.ArcGIS.Carto;
using ESRI.ArcGIS.Controls;
using ESRI.ArcGIS.SystemUI;

using DroneMap.Forms;

namespace Map_GIS
{
    public sealed partial class Form2D : Form
    {
        #region class private members
        private IMapControl3 m_mapControl = null;
        private string m_mapDocumentName = string.Empty;
        #endregion

        #region class constructor
        public Form2D()
        {
            InitializeComponent();
            ICommand command = new CreateNewDocument();
            axToolbarControl2.AddItem(command, 0, 0, false, 0, esriCommandStyles.esriCommandStyleIconOnly);
        }
        #endregion

        private void MainForm_Load(object sender, EventArgs e)
        {
            //get the MapControl
            m_mapControl = (IMapControl3)axMapControl1.Object;

            //disable the Save menu (since there is no document yet)

            axMapControl1.Map.Name = "Map";

        }

        //listen to MapReplaced evant in order to update the statusbar and the Save menu
        private void axMapControl1_OnMapReplaced(object sender, IMapControlEvents2_OnMapReplacedEvent e)
        {
            //get the current document name from the MapControl
            m_mapDocumentName = m_mapControl.DocumentFilename;
        }

        private void axMapControl1_OnMouseMove(object sender, IMapControlEvents2_OnMouseMoveEvent e)
        {
            statusBarXY.Text = string.Format("{0}, {1}  {2}", e.mapX.ToString("#######.##"), e.mapY.ToString("#######.##"), axMapControl1.MapUnits.ToString().Substring(4));
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
            fileExtension = fileExtension.ToLower();
            switch (fileExtension)
            {
                case ".img":
                case ".bmp":
                case ".jpg":
                case ".jpeg":
                case ".png":
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
                case ".mxd":
                    {
                        axMapControl1.LoadMxFile(filePath);
                    }
                    break;
                case ".lyr":
                    {
                        axMapControl1.AddLayerFromFile(filePath);
                    }
                    break;
                default:
                    {
                        Common.message_show(richTextBox1, 4, "不支持此数据打开");
                    }
                    break;
            }
        }

        private void newShpToolStripMenuItem_Click(object sender, EventArgs e)
        {
            NewShpFile NSForm = new NewShpFile(axMapControl1, richTextBox1);
            NSForm.Show();
        }

        private void clipRasterToolStripMenuItem_Click(object sender, EventArgs e)
        {
            ClipForm CForm = new ClipForm(axMapControl1, richTextBox1);
            CForm.Show();
        }

        private void cutFillToolStripMenuItem_Click(object sender, EventArgs e)
        {
            CutFillForm CFForm = new CutFillForm(axMapControl1, richTextBox1);
            CFForm.Show();
        }

        private void shpToRasterToolStripMenuItem_Click(object sender, EventArgs e)
        {
            ShpToRasterForm STRForm = new ShpToRasterForm(axMapControl1, richTextBox1);
            STRForm.Show();
        }
    }
}