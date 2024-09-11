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
        public static String AppStartPath = Directory.GetParent(Directory.GetParent(Application.StartupPath).FullName).FullName;
        /// <summary>
        /// 提示消息文字颜色 0：蓝色 1：绿色 2：黑色 3：橘色 4：红色
        /// </summary>
        private static Color[] mLogMsgTypeColor = { Color.Blue, Color.Green, Color.Black, Color.Orange, Color.Red };
        public static void message_show(RichTextBox showinfo, int msgtype, string msg)
        {
            showinfo.SelectionFont = new Font(showinfo.SelectionFont, FontStyle.Bold);
            showinfo.SelectionColor = mLogMsgTypeColor[msgtype];
            showinfo.AppendText(string.Format(" {0}\n", msg));
            showinfo.ScrollToCaret();
        }

        public static void CopyDirectory(string sourceDir, string destinationDir, bool recursive)
        {
            // Get information about the source directory
            var dir = new DirectoryInfo(sourceDir);

            // Check if the source directory exists
            if (!dir.Exists)
                throw new DirectoryNotFoundException($"Source directory not found: {dir.FullName}");

            // Cache directories before we start copying
            DirectoryInfo[] dirs = dir.GetDirectories();

            // Create the destination directory
            Directory.CreateDirectory(destinationDir);

            // Get the files in the source directory and copy to the destination directory
            foreach (FileInfo file in dir.GetFiles())
            {
                string targetFilePath = Path.Combine(destinationDir, file.Name);
                file.CopyTo(targetFilePath);
            }

            // If recursive and copying subdirectories, recursively call this method
            if (recursive)
            {
                foreach (DirectoryInfo subDir in dirs)
                {
                    string newDestinationDir = Path.Combine(destinationDir, subDir.Name);
                    CopyDirectory(subDir.FullName, newDestinationDir, true);
                }
            }
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

        public static String openFolder(FolderBrowserDialog FBD)
        {
            FBD.Description = "请选择文件路径";
            FBD.ShowDialog();
            return FBD.SelectedPath;
        }

        public static IFeatureClass GetFeatureClass(string pPath)
        {
            string pFolder = Path.GetDirectoryName(pPath);
            string pFileName = Path.GetFileName(pPath);

            // 创建工作空间
            IWorkspaceFactory pWorkspaceFactory = new ShapefileWorkspaceFactory();
            IWorkspace pWorkspace = pWorkspaceFactory.OpenFromFile(pFolder, 0);
            IFeatureWorkspace pFeatureWorkspace = pWorkspace as IFeatureWorkspace;

            // 打开要素类
            IFeatureClass pFC = pFeatureWorkspace.OpenFeatureClass(pFileName);
            return pFC;
        }

        public static IFeatureLayer LoadShpFile(string pPath)
        {
            // 打开要素类
            IFeatureClass pFC = GetFeatureClass(pPath);

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
