using ESRI.ArcGIS.esriSystem;
using ESRI.ArcGIS;
using System;
using System.Collections.Generic;
using System.Windows.Forms;

namespace MapControlApplication1
{
    static class Program
    {
        /// <summary>
        /// The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main()
        {
            if (!RuntimeManager.Bind(ProductCode.Desktop))
            {
                if (!RuntimeManager.Bind(ProductCode.Engine))
                {
                    MessageBox.Show("Unable to bind to ArcGIS runtime. Application will be shut down.");
                    return;
                }
            }

            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new MainForm());
        }
    }
}