using ESRI.ArcGIS.Controls;
using ESRI.ArcGIS.DataSourcesFile;
using ESRI.ArcGIS.Geodatabase;
using Map_GIS;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace DroneMap.Forms
{
    public partial class ShpToRasterForm : Form
    {
        public RichTextBox showinfo;
        public AxMapControl axMapControl1;

        public ShpToRasterForm(AxMapControl axMapControl1, RichTextBox showinfo)
        {
            InitializeComponent();
            this.axMapControl1 = axMapControl1;
            this.showinfo = showinfo;
        }

        private void inFileBtn_Click(object sender, EventArgs e)
        {
            String fileName = Common.openFile(openFileDialog1, "矢量文件|*.shp|全部文件|*.*");
            if (fileName.Trim() != "")
            {
                inFileText.Text = fileName;
                var pFC = Common.GetFeatureClass(fileName);
                var fields = pFC.Fields;
                for(int i=0; i < fields.FieldCount; i++)
                    if(fields.Field[i].Name != pFC.ShapeFieldName)
                        FieldComboBox.Items.Add(fields.Field[i].Name);
                FieldComboBox.SelectedIndex = 0;
            }
        }

        private void outFileBtn_Click(object sender, EventArgs e)
        {
            String fileName = Common.saveFile(saveFileDialog1, "栅格文件|*.tif;*.img|全部文件|*.*");
            if (fileName.Trim() != "")
                outFileText.Text = fileName;
        }

        private void ShpToRasterForm_FormClosed(object sender, FormClosedEventArgs e)
        {
            var pWorkspaceFactory = new ShapefileWorkspaceFactory();
            var ipWsFactoryLock = (IWorkspaceFactoryLockControl)pWorkspaceFactory;
            if (ipWsFactoryLock.SchemaLockingEnabled)
                ipWsFactoryLock.DisableSchemaLocking();
        }
    }
}
