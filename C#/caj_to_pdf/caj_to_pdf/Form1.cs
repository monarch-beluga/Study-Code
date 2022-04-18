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

namespace caj_to_pdf
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        #region 打开文件选择框
        private OpenFileDialog pOpenFileDialogGet(string Title, string Filter)
        {
            OpenFileDialog pOpenFileDialog = new OpenFileDialog();
            pOpenFileDialog.CheckFileExists = true;
            pOpenFileDialog.Title = Title;
            pOpenFileDialog.Filter = Filter;
            pOpenFileDialog.Multiselect = false;
            pOpenFileDialog.RestoreDirectory = true;
            return pOpenFileDialog;
        }
        #endregion

        private void cajPathbtn_Click(object sender, EventArgs e)
        {
            OpenFileDialog pOpenFileDialog = pOpenFileDialogGet("打开cja文档", "caj 文档(*.caj)|*.caj");
            if (pOpenFileDialog.ShowDialog() == DialogResult.OK)
            {
                string pFileName = pOpenFileDialog.FileName;
                if (pFileName == "")
                    return;
                cajPathText.Text = pFileName;
            }
        }

        private string ExecuteCmd(String strInput)
        {
            Process p = new Process();
            //设置要启动的应用程序
            p.StartInfo.FileName = "cmd.exe";
            //是否使用操作系统shell启动
            p.StartInfo.UseShellExecute = false;
            // 接受来自调用程序的输入信息
            p.StartInfo.RedirectStandardInput = true;
            //输出信息
            p.StartInfo.RedirectStandardOutput = true;
            // 输出错误
            p.StartInfo.RedirectStandardError = true;
            //不显示程序窗口
            p.StartInfo.CreateNoWindow = true;
            //启动程序
            p.Start();

            //向cmd窗口发送输入信息
            p.StandardInput.WriteLine(strInput + "&exit");

            p.StandardInput.AutoFlush = true;

            //获取输出信息
            string strOuput = p.StandardOutput.ReadToEnd();
            //等待程序执行完退出进程
            p.WaitForExit();
            p.Close();
            return strOuput;
        }

        string pyScript = "caj2pdf";
        private void showBtn_Click(object sender, EventArgs e)
        {
            string pFileName = cajPathText.Text;
            if (pFileName == "")
                cajFileInfoText.Text = "文件路径为空！！";
            else
            {
                cajFileInfoText.Text = "";
                string strOuput = ExecuteCmd("cd E:/Paper/caj2pdf-master/&python " + pyScript + " show " + pFileName);
                string[] strArray = strOuput.Split('\n');
                int l = strArray.Length;
                for (int i = l - 6; i < l - 2; i++)
                    cajFileInfoText.AppendText(strArray[i]);
            }
        }

        private void convertBtn_Click(object sender, EventArgs e)
        {
            string pFileName = cajPathText.Text;
            if (pFileName == "")
                cajFileInfoText.Text = "文件路径为空！！";
            else
            {
                string outFileName = pFileName.Replace(".caj", ".pdf");
                string cmdStr = "cd E:/Paper/caj2pdf-master/&python " + pyScript + " convert " + pFileName + " -o " + outFileName;
                string strOuput = ExecuteCmd(cmdStr);
                cajFileInfoText.Text = "转换成功！！";
            }
        }
    }
}
