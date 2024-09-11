using Map_GIS;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace DroneMap.Forms
{
    public partial class Form3D : Form
    {
        public Form3D()
        {
            InitializeComponent();
            executeCMD(Common.AppStartPath + "\\F3D\\bin", "f3d");
            FindWindow("F3D - A fast and minimalist 3D viewer", "空");
        }

        private void FindWindow(String windowName, String fileName)
        {
            Task.Run(() =>
            {
                if (WindowManager.FindWindow(windowName))
                {
                    this.Invoke(new Action(() =>
                    {
                        WindowManager.SetParent(panel1.Handle, windowName);
                        toolStripStatusLabel1.Text = fileName;
                    }));
                }
                else
                {
                    MessageBox.Show("未能查找到窗体");
                }
            });
        }

        private void executeCMD(String path, String cmd)
        {
            Process p = new Process();
            p.StartInfo.FileName = "cmd.exe";
            p.StartInfo.Arguments = "/c " + cmd;
            p.StartInfo.WorkingDirectory = path;
            //启动进程时不使用 shell
            p.StartInfo.UseShellExecute = false;
            //设置标准重定向输入
            p.StartInfo.RedirectStandardInput = true;
            //设置标准重定向输出
            p.StartInfo.RedirectStandardOutput = true;
            //设置标准重定向错误输出
            p.StartInfo.RedirectStandardError = true;
            //设置不显示cmd控制台窗体
            p.StartInfo.CreateNoWindow = true;
            //隐藏窗体
            p.StartInfo.WindowStyle = ProcessWindowStyle.Hidden;

            p.Start();
        }

        private void newToolStripMenuItem_Click(object sender, EventArgs e)
        {
            WindowManager.CloseWindow();
            executeCMD(Common.AppStartPath + "\\F3D\\bin", "f3d");
            FindWindow("F3D - A fast and minimalist 3D viewer", "空");
        }

        private void openToolStripMenuItem_Click(object sender, EventArgs e)
        {
            String filePath = Common.openFile(openFileDialog1, "全部文件|*.*");
            if (filePath.Trim() == "")
                return;
            var fileName = Path.GetFileName(filePath);
            WindowManager.CloseWindow();
            toolStripStatusLabel1.Text = "正在打开文件,请稍等...";
            executeCMD(Common.AppStartPath + "\\F3D\\bin", $"f3d {filePath}");
            FindWindow("F3D - A fast and minimalist 3D viewer", fileName);
        }
    }
}
