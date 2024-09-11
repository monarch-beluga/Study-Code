using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using ESRI.ArcGIS.Geoprocessor;
using System.Windows.Forms;
using Map_GIS;
using ESRI.ArcGIS.DataManagementTools;
using ESRI.ArcGIS.Controls;

namespace DroneMap.Forms
{
    public partial class ClipForm : Form
    {
        public RichTextBox showinfo;
        public AxMapControl axMapControl1;

        public ClipForm(AxMapControl axMapControl1, RichTextBox showinfo)
        {
            InitializeComponent();
            this.axMapControl1 = axMapControl1;
            this.showinfo = showinfo;
        }

        private void inFileBtn_Click(object sender, EventArgs e)
        {
            String fileName = Common.openFile(openFileDialog1, "栅格文件|*.tif;*.img|全部文件|*.*");
            if (fileName.Trim() != "")
                inFileText.Text = fileName;
        }

        private void roiBtn_Click(object sender, EventArgs e)
        {
            String fileName = Common.openFile(openFileDialog1, "矢量文件|*.shp|全部文件|*.*");
            if (fileName.Trim() != "")
                roiText.Text = fileName;
        }

        private void outFileBtn_Click(object sender, EventArgs e)
        {
            String fileName = Common.saveFile(saveFileDialog1, "栅格文件|*.tif;*.img|全部文件|*.*");
            if (fileName.Trim() != "")
                outFileText.Text = fileName;
        }

        private void executeBtn_Click(object sender, EventArgs e)
        {
            var inFile = inFileText.Text;
            var outFile = outFileText.Text;
            var roiFile = roiText.Text;

            Geoprocessor GP = new Geoprocessor();
            GP.SetEnvironmentValue("nodata", "MINIMUM");
            GP.OverwriteOutput = true;

            Clip clipTool = new Clip();
            clipTool.in_raster = inFile;
            clipTool.out_raster = outFile;
            clipTool.in_template_dataset = roiFile;
            clipTool.clipping_geometry = "ClippingGeometry";
            GP.Execute(clipTool, null);

            var pFLayer = Common.LoadRaster(outFile);
            axMapControl1.AddLayer(pFLayer, 0);
            Common.message_show(showinfo, 1, "栅格裁剪成功！");
        }
    }
}
