
namespace Map_GIS
{
    partial class Form2D
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            //Ensures that any ESRI libraries that have been used are unloaded in the correct order. 
            //Failure to do this may result in random crashes on exit due to the operating system unloading 
            //the libraries in the incorrect order. 
            ESRI.ArcGIS.ADF.COMSupport.AOUninitialize.Shutdown();

            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form2D));
            this.menuStrip1 = new System.Windows.Forms.MenuStrip();
            this.shpFileToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.newShpToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.rasterToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.clipRasterToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.cutFillToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.conversionToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.shpToRasterToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.axMapControl1 = new ESRI.ArcGIS.Controls.AxMapControl();
            this.axToolbarControl1 = new ESRI.ArcGIS.Controls.AxToolbarControl();
            this.axTOCControl1 = new ESRI.ArcGIS.Controls.AxTOCControl();
            this.axLicenseControl1 = new ESRI.ArcGIS.Controls.AxLicenseControl();
            this.splitter1 = new System.Windows.Forms.Splitter();
            this.statusStrip1 = new System.Windows.Forms.StatusStrip();
            this.statusBarXY = new System.Windows.Forms.ToolStripStatusLabel();
            this.splitContainer1 = new System.Windows.Forms.SplitContainer();
            this.splitContainer2 = new System.Windows.Forms.SplitContainer();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.axToolbarControl2 = new ESRI.ArcGIS.Controls.AxToolbarControl();
            this.menuStrip1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.axMapControl1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.axToolbarControl1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.axTOCControl1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.axLicenseControl1)).BeginInit();
            this.statusStrip1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.splitContainer1)).BeginInit();
            this.splitContainer1.Panel1.SuspendLayout();
            this.splitContainer1.Panel2.SuspendLayout();
            this.splitContainer1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.splitContainer2)).BeginInit();
            this.splitContainer2.Panel1.SuspendLayout();
            this.splitContainer2.Panel2.SuspendLayout();
            this.splitContainer2.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.axToolbarControl2)).BeginInit();
            this.SuspendLayout();
            // 
            // menuStrip1
            // 
            this.menuStrip1.ImageScalingSize = new System.Drawing.Size(20, 20);
            this.menuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.shpFileToolStripMenuItem,
            this.rasterToolStripMenuItem,
            this.conversionToolStripMenuItem});
            this.menuStrip1.Location = new System.Drawing.Point(0, 0);
            this.menuStrip1.Name = "menuStrip1";
            this.menuStrip1.Size = new System.Drawing.Size(1145, 28);
            this.menuStrip1.TabIndex = 0;
            this.menuStrip1.Text = "menuStrip1";
            // 
            // shpFileToolStripMenuItem
            // 
            this.shpFileToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.newShpToolStripMenuItem});
            this.shpFileToolStripMenuItem.Name = "shpFileToolStripMenuItem";
            this.shpFileToolStripMenuItem.Size = new System.Drawing.Size(53, 24);
            this.shpFileToolStripMenuItem.Text = "矢量";
            // 
            // newShpToolStripMenuItem
            // 
            this.newShpToolStripMenuItem.Name = "newShpToolStripMenuItem";
            this.newShpToolStripMenuItem.Size = new System.Drawing.Size(152, 26);
            this.newShpToolStripMenuItem.Text = "新建矢量";
            this.newShpToolStripMenuItem.Click += new System.EventHandler(this.newShpToolStripMenuItem_Click);
            // 
            // rasterToolStripMenuItem
            // 
            this.rasterToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.clipRasterToolStripMenuItem,
            this.cutFillToolStripMenuItem});
            this.rasterToolStripMenuItem.Name = "rasterToolStripMenuItem";
            this.rasterToolStripMenuItem.Size = new System.Drawing.Size(53, 24);
            this.rasterToolStripMenuItem.Text = "栅格";
            // 
            // clipRasterToolStripMenuItem
            // 
            this.clipRasterToolStripMenuItem.Name = "clipRasterToolStripMenuItem";
            this.clipRasterToolStripMenuItem.Size = new System.Drawing.Size(137, 26);
            this.clipRasterToolStripMenuItem.Text = "裁剪";
            this.clipRasterToolStripMenuItem.Click += new System.EventHandler(this.clipRasterToolStripMenuItem_Click);
            // 
            // cutFillToolStripMenuItem
            // 
            this.cutFillToolStripMenuItem.Name = "cutFillToolStripMenuItem";
            this.cutFillToolStripMenuItem.Size = new System.Drawing.Size(137, 26);
            this.cutFillToolStripMenuItem.Text = "填挖方";
            this.cutFillToolStripMenuItem.Click += new System.EventHandler(this.cutFillToolStripMenuItem_Click);
            // 
            // conversionToolStripMenuItem
            // 
            this.conversionToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.shpToRasterToolStripMenuItem});
            this.conversionToolStripMenuItem.Name = "conversionToolStripMenuItem";
            this.conversionToolStripMenuItem.Size = new System.Drawing.Size(53, 24);
            this.conversionToolStripMenuItem.Text = "转换";
            // 
            // shpToRasterToolStripMenuItem
            // 
            this.shpToRasterToolStripMenuItem.Name = "shpToRasterToolStripMenuItem";
            this.shpToRasterToolStripMenuItem.Size = new System.Drawing.Size(224, 26);
            this.shpToRasterToolStripMenuItem.Text = "矢量转栅格";
            this.shpToRasterToolStripMenuItem.Click += new System.EventHandler(this.shpToRasterToolStripMenuItem_Click);
            // 
            // axMapControl1
            // 
            this.axMapControl1.AllowDrop = true;
            this.axMapControl1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.axMapControl1.Location = new System.Drawing.Point(0, 0);
            this.axMapControl1.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.axMapControl1.Name = "axMapControl1";
            this.axMapControl1.OcxState = ((System.Windows.Forms.AxHost.State)(resources.GetObject("axMapControl1.OcxState")));
            this.axMapControl1.Size = new System.Drawing.Size(839, 469);
            this.axMapControl1.TabIndex = 2;
            this.axMapControl1.OnMouseMove += new ESRI.ArcGIS.Controls.IMapControlEvents2_Ax_OnMouseMoveEventHandler(this.axMapControl1_OnMouseMove);
            this.axMapControl1.OnOleDrop += new ESRI.ArcGIS.Controls.IMapControlEvents2_Ax_OnOleDropEventHandler(this.axMapControl1_OnOleDrop);
            this.axMapControl1.OnMapReplaced += new ESRI.ArcGIS.Controls.IMapControlEvents2_Ax_OnMapReplacedEventHandler(this.axMapControl1_OnMapReplaced);
            // 
            // axToolbarControl1
            // 
            this.axToolbarControl1.Dock = System.Windows.Forms.DockStyle.Top;
            this.axToolbarControl1.Location = new System.Drawing.Point(0, 56);
            this.axToolbarControl1.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.axToolbarControl1.Name = "axToolbarControl1";
            this.axToolbarControl1.OcxState = ((System.Windows.Forms.AxHost.State)(resources.GetObject("axToolbarControl1.OcxState")));
            this.axToolbarControl1.Size = new System.Drawing.Size(1145, 28);
            this.axToolbarControl1.TabIndex = 3;
            // 
            // axTOCControl1
            // 
            this.axTOCControl1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.axTOCControl1.Location = new System.Drawing.Point(0, 0);
            this.axTOCControl1.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.axTOCControl1.Name = "axTOCControl1";
            this.axTOCControl1.OcxState = ((System.Windows.Forms.AxHost.State)(resources.GetObject("axTOCControl1.OcxState")));
            this.axTOCControl1.Size = new System.Drawing.Size(298, 469);
            this.axTOCControl1.TabIndex = 4;
            // 
            // axLicenseControl1
            // 
            this.axLicenseControl1.Enabled = true;
            this.axLicenseControl1.Location = new System.Drawing.Point(422, 274);
            this.axLicenseControl1.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.axLicenseControl1.Name = "axLicenseControl1";
            this.axLicenseControl1.OcxState = ((System.Windows.Forms.AxHost.State)(resources.GetObject("axLicenseControl1.OcxState")));
            this.axLicenseControl1.Size = new System.Drawing.Size(32, 32);
            this.axLicenseControl1.TabIndex = 5;
            // 
            // splitter1
            // 
            this.splitter1.Location = new System.Drawing.Point(0, 84);
            this.splitter1.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.splitter1.Name = "splitter1";
            this.splitter1.Size = new System.Drawing.Size(4, 754);
            this.splitter1.TabIndex = 6;
            this.splitter1.TabStop = false;
            // 
            // statusStrip1
            // 
            this.statusStrip1.ImageScalingSize = new System.Drawing.Size(20, 20);
            this.statusStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.statusBarXY});
            this.statusStrip1.Location = new System.Drawing.Point(4, 812);
            this.statusStrip1.Name = "statusStrip1";
            this.statusStrip1.Padding = new System.Windows.Forms.Padding(1, 0, 19, 0);
            this.statusStrip1.Size = new System.Drawing.Size(1141, 26);
            this.statusStrip1.Stretch = false;
            this.statusStrip1.TabIndex = 7;
            this.statusStrip1.Text = "statusBar1";
            // 
            // statusBarXY
            // 
            this.statusBarXY.BorderStyle = System.Windows.Forms.Border3DStyle.SunkenOuter;
            this.statusBarXY.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Text;
            this.statusBarXY.Name = "statusBarXY";
            this.statusBarXY.Size = new System.Drawing.Size(71, 20);
            this.statusBarXY.Text = "Test 123";
            // 
            // splitContainer1
            // 
            this.splitContainer1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.splitContainer1.Location = new System.Drawing.Point(4, 84);
            this.splitContainer1.Name = "splitContainer1";
            this.splitContainer1.Orientation = System.Windows.Forms.Orientation.Horizontal;
            // 
            // splitContainer1.Panel1
            // 
            this.splitContainer1.Panel1.Controls.Add(this.splitContainer2);
            // 
            // splitContainer1.Panel2
            // 
            this.splitContainer1.Panel2.Controls.Add(this.richTextBox1);
            this.splitContainer1.Size = new System.Drawing.Size(1141, 728);
            this.splitContainer1.SplitterDistance = 469;
            this.splitContainer1.TabIndex = 8;
            // 
            // splitContainer2
            // 
            this.splitContainer2.Dock = System.Windows.Forms.DockStyle.Fill;
            this.splitContainer2.Location = new System.Drawing.Point(0, 0);
            this.splitContainer2.Name = "splitContainer2";
            // 
            // splitContainer2.Panel1
            // 
            this.splitContainer2.Panel1.Controls.Add(this.axTOCControl1);
            // 
            // splitContainer2.Panel2
            // 
            this.splitContainer2.Panel2.Controls.Add(this.axLicenseControl1);
            this.splitContainer2.Panel2.Controls.Add(this.axMapControl1);
            this.splitContainer2.Size = new System.Drawing.Size(1141, 469);
            this.splitContainer2.SplitterDistance = 298;
            this.splitContainer2.TabIndex = 5;
            // 
            // richTextBox1
            // 
            this.richTextBox1.BackColor = System.Drawing.Color.White;
            this.richTextBox1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.richTextBox1.Font = new System.Drawing.Font("楷体", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.richTextBox1.Location = new System.Drawing.Point(0, 0);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.ReadOnly = true;
            this.richTextBox1.Size = new System.Drawing.Size(1141, 255);
            this.richTextBox1.TabIndex = 0;
            this.richTextBox1.Text = "";
            // 
            // axToolbarControl2
            // 
            this.axToolbarControl2.Dock = System.Windows.Forms.DockStyle.Top;
            this.axToolbarControl2.Location = new System.Drawing.Point(0, 28);
            this.axToolbarControl2.Name = "axToolbarControl2";
            this.axToolbarControl2.OcxState = ((System.Windows.Forms.AxHost.State)(resources.GetObject("axToolbarControl2.OcxState")));
            this.axToolbarControl2.Size = new System.Drawing.Size(1145, 28);
            this.axToolbarControl2.TabIndex = 6;
            // 
            // Form2D
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1145, 838);
            this.Controls.Add(this.splitContainer1);
            this.Controls.Add(this.statusStrip1);
            this.Controls.Add(this.splitter1);
            this.Controls.Add(this.axToolbarControl1);
            this.Controls.Add(this.axToolbarControl2);
            this.Controls.Add(this.menuStrip1);
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.MainMenuStrip = this.menuStrip1;
            this.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.Name = "Form2D";
            this.Text = "ArcEngine Controls Application";
            this.Load += new System.EventHandler(this.MainForm_Load);
            this.menuStrip1.ResumeLayout(false);
            this.menuStrip1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.axMapControl1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.axToolbarControl1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.axTOCControl1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.axLicenseControl1)).EndInit();
            this.statusStrip1.ResumeLayout(false);
            this.statusStrip1.PerformLayout();
            this.splitContainer1.Panel1.ResumeLayout(false);
            this.splitContainer1.Panel2.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.splitContainer1)).EndInit();
            this.splitContainer1.ResumeLayout(false);
            this.splitContainer2.Panel1.ResumeLayout(false);
            this.splitContainer2.Panel2.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.splitContainer2)).EndInit();
            this.splitContainer2.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.axToolbarControl2)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.MenuStrip menuStrip1;
        private ESRI.ArcGIS.Controls.AxMapControl axMapControl1;
        private ESRI.ArcGIS.Controls.AxToolbarControl axToolbarControl1;
        private ESRI.ArcGIS.Controls.AxTOCControl axTOCControl1;
        private ESRI.ArcGIS.Controls.AxLicenseControl axLicenseControl1;
        private System.Windows.Forms.Splitter splitter1;
        private System.Windows.Forms.StatusStrip statusStrip1;
        private System.Windows.Forms.ToolStripStatusLabel statusBarXY;
        private System.Windows.Forms.SplitContainer splitContainer1;
        private System.Windows.Forms.SplitContainer splitContainer2;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private ESRI.ArcGIS.Controls.AxToolbarControl axToolbarControl2;
        private System.Windows.Forms.ToolStripMenuItem shpFileToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem newShpToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem rasterToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem conversionToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem clipRasterToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem cutFillToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem shpToRasterToolStripMenuItem;
    }
}

