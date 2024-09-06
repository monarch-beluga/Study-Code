using System;

using System.Windows.Forms;
using System.IO;

using ESRI.ArcGIS.DataSourcesFile;
using ESRI.ArcGIS.Carto;
using ESRI.ArcGIS.DataSourcesRaster;
using System.Drawing;
using ESRI.ArcGIS.Geodatabase;

namespace Map_GIS
{
    class Common
    {
        /// <summary>
        /// 提示消息文字颜色 0：蓝色 1：绿色 2：黑色 3：橘色 4：红色
        /// </summary>
        private static Color[] mLogMsgTypeColor = { Color.Blue, Color.Green, Color.Black, Color.Orange, Color.Red };
        public static void message_show(RichTextBox showinfo, int msgtype, string msg)
        {
            showinfo.SelectionFont = new Font(showinfo.SelectionFont, FontStyle.Bold);
            showinfo.SelectionColor = mLogMsgTypeColor[msgtype];
            showinfo.AppendText(string.Format("> {0}\n", msg));
            showinfo.ScrollToCaret();
        }

        public static void DeleteDirectory(string path)
        {
            // 如果文件夹存在则进入目录下
            if (Directory.Exists(path))
            {
                // 返回所有文件及目录
                foreach (string p in Directory.GetFileSystemEntries(path))
                {
                    if (File.Exists(p))
                    {
                        // 删除文件
                        File.Delete(p);
                    }
                    else
                    {
                        // 删除子目录
                        DeleteDirectory(p);
                    }
                }
                // 删除当前空目录
                Directory.Delete(path, true);
            }
        }

        public static String saveFile(SaveFileDialog saveFD, String filter)
        {
            saveFD.FileName = "";
            saveFD.Title = "保存文件";
            saveFD.Filter = filter;
            saveFD.FilterIndex = 1;
            saveFD.ShowDialog();
            return saveFD.FileName;
        }

        public static String openFile(OpenFileDialog OFD, String Filter)
        {
            OFD.FileName = "";
            OFD.Title = "打开文件";
            OFD.Filter = Filter;
            OFD.FilterIndex = 0;
            OFD.ShowDialog();
            return OFD.FileName;
        }

        public static IFeatureLayer LoadShpFile(string pPath)
        {
            string pFolder = Path.GetDirectoryName(pPath);
            string pFileName = Path.GetFileName(pPath);


            // 创建工作空间
            IWorkspaceFactory pWorkspaceFactory = new ShapefileWorkspaceFactory();
            IWorkspace pWorkspace = pWorkspaceFactory.OpenFromFile(pFolder, 0);
            IFeatureWorkspace pFeatureWorkspace = pWorkspace as IFeatureWorkspace;

            // 打开要素类
            IFeatureClass pFC = pFeatureWorkspace.OpenFeatureClass(pFileName);

            // 要素图层
            IFeatureLayer pFLayer = new FeatureLayerClass();
            pFLayer.FeatureClass = pFC;
            pFLayer.Name = pFC.AliasName;

            return pFLayer;
        }

        public static IRasterLayer LoadRaster(string pPath)
        { 
            string pFolder = Path.GetDirectoryName(pPath);
            string pFileName = Path.GetFileName(pPath);

            IWorkspaceFactory pWorkspaceFactory = new RasterWorkspaceFactory();
            IWorkspace pWorkspace = pWorkspaceFactory.OpenFromFile(pFolder, 0);
            IRasterWorkspace pRasterWorkspace = pWorkspace as IRasterWorkspace;

            IRasterDataset pRasterDataset = pRasterWorkspace.OpenRasterDataset(pFileName);

            IRasterPyramid pRasterPyramid = pRasterDataset as IRasterPyramid;
            if (!pRasterPyramid.Present)
            {
                pRasterPyramid.Create();
            }

            // 栅格图层
            IRasterLayer pRasterLayer = new RasterLayer();
            pRasterLayer.CreateFromDataset(pRasterDataset);

            return pRasterLayer;
        }

    }
}
