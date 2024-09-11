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
using ESRI.ArcGIS.Carto;
using ESRI.ArcGIS.Controls;
using ESRI.ArcGIS.DataSourcesFile;
using ESRI.ArcGIS.Geodatabase;
using ESRI.ArcGIS.Geometry;
using Map_GIS;

namespace DroneMap.Forms
{
    public partial class NewShpFile : Form
    {
        public RichTextBox showinfo;
        public AxMapControl axMapControl1;

        public NewShpFile(AxMapControl axMapControl1, RichTextBox showinfo)
        {
            InitializeComponent();
            comboBox1.SelectedIndex = 0;
            this.axMapControl1 = axMapControl1;
            this.showinfo = showinfo;
        }

        private void outFileBtn_Click(object sender, EventArgs e)
        {
            String path = Common.saveFile(saveFileDialog1, "矢量文件|*.shp|全部文件|*.*");
            if (path.Trim() != "")
                outFileText.Text = path;
        }

        private void executeBtn_Click(object sender, EventArgs e)
        {
            String fileName = outFileText.Text;
            String geotype = comboBox1.Text;

            string pFolder = System.IO.Path.GetDirectoryName(fileName);
            string pFileName = System.IO.Path.GetFileName(fileName);

            // 创建工作空间
            IWorkspaceFactory pWorkspaceFactory = new ShapefileWorkspaceFactory();
            IWorkspace pWorkspace = pWorkspaceFactory.OpenFromFile(pFolder, 0);
            IFeatureWorkspace pFeatureWorkspace = pWorkspace as IFeatureWorkspace;

            IFields pFields = new FieldsClass();
            IFieldsEdit pFieldsEdit;
            pFieldsEdit = (IFieldsEdit)pFields;

            IField pField = new FieldClass();
            IFieldEdit pFieldEdit = (IFieldEdit)pField;
            pFieldEdit.Name_2 = "Shape";
            pFieldEdit.Type_2 = esriFieldType.esriFieldTypeGeometry;
            IGeometryDef pGeometryDef = new GeometryDefClass();
            IGeometryDefEdit pGDefEdit = (IGeometryDefEdit)pGeometryDef;
            if (geotype == "点")
                pGDefEdit.GeometryType_2 = esriGeometryType.esriGeometryPoint;
            else if (geotype == "线")
                pGDefEdit.GeometryType_2 = esriGeometryType.esriGeometryPolyline;
            else
                pGDefEdit.GeometryType_2 = esriGeometryType.esriGeometryPolygon;

            ISpatialReferenceFactory pSRF = new SpatialReferenceEnvironmentClass();
            ISpatialReference pSpatialReference = pSRF.CreateProjectedCoordinateSystem(3857);
            pGDefEdit.SpatialReference_2 = pSpatialReference;
            pFieldEdit.GeometryDef_2 = pGeometryDef;
            pFieldsEdit.AddField(pField);

            IFeatureClass pFeatureClass = pFeatureWorkspace.CreateFeatureClass(pFileName, pFields, null, null, esriFeatureType.esriFTSimple, "Shape", "");

            IFeatureLayer pFLayer = new FeatureLayerClass();
            pFLayer.FeatureClass = pFeatureClass;
            pFLayer.Name = pFeatureClass.AliasName;

            axMapControl1.AddLayer(pFLayer, 0);
            Common.message_show(showinfo, 1, "矢量创建成功！");
        }

    }
}
