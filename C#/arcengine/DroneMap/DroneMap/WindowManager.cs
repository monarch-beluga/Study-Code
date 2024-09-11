using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace DroneMap
{
    public static class WindowManager
    {
        public static IntPtr intPtr;         //第三方应用窗口的句柄

        /// <summary>
        /// 调整第三方应用窗体大小
        /// </summary>
        public static void ResizeWindow()
        {
            ShowWindow(intPtr, 0);  //先将窗口隐藏
            ShowWindow(intPtr, 3);  //再将窗口最大化，可以让第三方窗口自适应容器的大小
        }

        /// <summary>
        /// 循环查找第三方窗体
        /// </summary>
        /// <returns></returns>
        public static bool FindWindow(string formName)
        {
            for (int i = 0; i < 100; i++)
            {
                //按照窗口标题查找Python窗口
                IntPtr vHandle = FindWindow(null, formName);
                if (vHandle == IntPtr.Zero)
                {
                    Thread.Sleep(100);  //每100ms查找一次，直到找到，最多查找10s
                    continue;
                }
                else      //找到返回True
                {
                    intPtr = vHandle;
                    return true;
                }
            }
            intPtr = IntPtr.Zero;
            return false;
        }

        public static void CloseWindow()
        {
            if (intPtr != IntPtr.Zero)
                SendMessage(intPtr, 0x10, IntPtr.Zero, 0);
        }

        /// <summary>
        /// 将第三方窗体嵌入到容器内
        /// </summary>
        /// <param name="hWndNewParent">父容器句柄</param>
        /// <param name="windowName">窗体名</param>
        public static void SetParent(IntPtr hWndNewParent, string windowName)
        {
            ShowWindow(intPtr, 0);                 //先将窗体隐藏，防止出现闪烁
            SetParent(intPtr, hWndNewParent);      //将第三方窗体嵌入父容器                    
            Thread.Sleep(100);                      //略加延时
            ShowWindow(intPtr, 3);                 //让第三方窗体在容器中最大化显示
            RemoveWindowTitle(intPtr);             // 去除窗体标题
        }


        /// <summary>
        /// 去除窗体标题
        /// </summary>
        /// <param name="vHandle">窗口句柄</param>
        public static void RemoveWindowTitle(IntPtr vHandle)
        {
            long style = GetWindowLong(vHandle, -16);
            style &= ~0x00C00000;
            SetWindowLong(vHandle, -16, style);
        }


        #region API 需要using System.Runtime.InteropServices;

        [DllImport("user32.dll ", EntryPoint = "SetParent")]
        private static extern IntPtr SetParent(IntPtr hWndChild, IntPtr hWndNewParent);   //将外部窗体嵌入程序

        [DllImport("user32.dll")]
        public static extern IntPtr FindWindow(string lpszClass, string lpszWindow);      //按照窗体类名或窗体标题查找窗体

        [DllImport("user32.dll", EntryPoint = "ShowWindow", CharSet = CharSet.Auto)]
        private static extern int ShowWindow(IntPtr hwnd, int nCmdShow);                  //设置窗体属性

        [DllImport("user32.dll", EntryPoint = "SetWindowLong", CharSet = CharSet.Auto)]
        public static extern IntPtr SetWindowLong(IntPtr hWnd, int nIndex, long dwNewLong);

        [DllImport("user32.dll", EntryPoint = "GetWindowLong", CharSet = CharSet.Auto)]
        public static extern long GetWindowLong(IntPtr hWnd, int nIndex);

        [DllImport("User32.dll", EntryPoint = "SendMessage")]
        private static extern void SendMessage(IntPtr hWnd, int Msg, IntPtr wParam, int lParam);

        #endregion
    }

}
