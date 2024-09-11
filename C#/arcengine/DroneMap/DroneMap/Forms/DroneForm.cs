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
using Map_GIS;

namespace DroneMap.Forms
{
    public partial class DroneForm : Form
    {
        public DroneForm()
        {
            InitializeComponent();
            int processorCount = Environment.ProcessorCount;
            maxConcurrencyText.Text = $"{processorCount}";

            imgPathText.Text = @"D:\Work\reality_map\丰城市铁路乡钨矿s23_s24";
            outPathText.Text = @"D:\Work\reality_map";
        }

        private void imgPathBtn_Click(object sender, EventArgs e)
        {
            String path = Common.openFolder(folderBrowserDialog1);
            if (path.Trim() != "")
                imgPathText.Text = path;
        }

        private void outPathBtn_Click(object sender, EventArgs e)
        {
            String path = Common.openFolder(folderBrowserDialog1);
            if (path.Trim() != "")
                outPathText.Text = path;
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

        private void executeODM(String path, String cmd)
        {
            Process p = new Process();
            p.StartInfo.FileName = "cmd.exe";
            p.StartInfo.Arguments = "/c " + cmd;
            p.StartInfo.WorkingDirectory = path;
            p.StartInfo.UseShellExecute = true;
            p.EnableRaisingEvents = true;
            p.StartInfo.CreateNoWindow = true;
            //隐藏窗体
            if (checkBoxProcess.Checked)
                p.StartInfo.WindowStyle = ProcessWindowStyle.Hidden;
            
            p.Start();
            p.Exited += new EventHandler(OMDExiteHandler);
        }

        private void OMDExiteHandler(object sender, System.EventArgs e)
        {
            String outPath = outPathText.Text;
            String workPath = outPath + "\\temp";
            executeCMD(workPath, "rd /q images");
            foreach (String sourceDir in copyFolders)
                Common.CopyDirectory($"{workPath}\\{sourceDir}", $"{outPath}\\{sourceDir}", true);
            Common.DeleteDirectory(workPath);
            Common.message_show(richTextBox1, 2, "无人机影像处理完成！！！");
        }

        private List<string> copyFolders;
        private void executeBtn_Click(object sender, EventArgs e)
        {
            String imgPath = imgPathText.Text;
            String outPath = outPathText.Text;
            String workPath = outPath + "\\temp";
            String resolution = resolutionText.Text;
            String maxConcurrency = maxConcurrencyText.Text; 

            if (!Directory.Exists(workPath))
                Directory.CreateDirectory(workPath);
            Common.message_show(richTextBox1, 1, "临时工作空间创建完成！！");
            executeCMD(workPath, "mklink /j images " + imgPath);
            String cmd = $"run {workPath} --max-concurrency={maxConcurrency} --orthophoto-resolution={resolution} --dem-resolution={resolution} ";
            copyFolders = new List<string>();
            if (checkBoxDsm.Checked)
            {
                cmd += "--dsm ";
                copyFolders.Add("odm_dem");
            }
            if (checkBoxDom.Checked)
                copyFolders.Add("odm_orthophoto");
            if (checkBox3D.Checked)
                copyFolders.Add("odm_texturing");
            if (checkBox25D.Checked)
                copyFolders.Add("odm_texturing_25d");

            Common.message_show(richTextBox1, 2, "开始处理无人机影像，需要长时间等待……");
            executeODM(Common.AppStartPath + "\\ODM", cmd);
        }
    }
}
