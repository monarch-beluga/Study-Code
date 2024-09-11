
namespace DroneMap
{
    partial class MainForm
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
            this.MenuPanel = new System.Windows.Forms.Panel();
            this.Btn3D = new System.Windows.Forms.Button();
            this.Btn2D = new System.Windows.Forms.Button();
            this.DroneBtn = new System.Windows.Forms.Button();
            this.MainBtn = new System.Windows.Forms.Button();
            this.DesktopPanel = new System.Windows.Forms.Panel();
            this.MenuPanel.SuspendLayout();
            this.SuspendLayout();
            // 
            // MenuPanel
            // 
            this.MenuPanel.BackColor = System.Drawing.Color.DodgerBlue;
            this.MenuPanel.Controls.Add(this.Btn3D);
            this.MenuPanel.Controls.Add(this.Btn2D);
            this.MenuPanel.Controls.Add(this.DroneBtn);
            this.MenuPanel.Controls.Add(this.MainBtn);
            this.MenuPanel.Dock = System.Windows.Forms.DockStyle.Left;
            this.MenuPanel.Location = new System.Drawing.Point(0, 0);
            this.MenuPanel.Name = "MenuPanel";
            this.MenuPanel.Size = new System.Drawing.Size(166, 935);
            this.MenuPanel.TabIndex = 0;
            // 
            // Btn3D
            // 
            this.Btn3D.Dock = System.Windows.Forms.DockStyle.Top;
            this.Btn3D.FlatAppearance.BorderSize = 0;
            this.Btn3D.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.Btn3D.Font = new System.Drawing.Font("楷体", 13.8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.Btn3D.ForeColor = System.Drawing.Color.Transparent;
            this.Btn3D.Location = new System.Drawing.Point(0, 180);
            this.Btn3D.Name = "Btn3D";
            this.Btn3D.Size = new System.Drawing.Size(166, 60);
            this.Btn3D.TabIndex = 2;
            this.Btn3D.Text = "三维展示";
            this.Btn3D.UseVisualStyleBackColor = true;
            this.Btn3D.Click += new System.EventHandler(this.Btn3D_Click);
            // 
            // Btn2D
            // 
            this.Btn2D.Dock = System.Windows.Forms.DockStyle.Top;
            this.Btn2D.FlatAppearance.BorderSize = 0;
            this.Btn2D.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.Btn2D.Font = new System.Drawing.Font("楷体", 13.8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.Btn2D.ForeColor = System.Drawing.Color.Transparent;
            this.Btn2D.Location = new System.Drawing.Point(0, 120);
            this.Btn2D.Name = "Btn2D";
            this.Btn2D.Size = new System.Drawing.Size(166, 60);
            this.Btn2D.TabIndex = 1;
            this.Btn2D.Text = "二维展示";
            this.Btn2D.UseVisualStyleBackColor = true;
            this.Btn2D.Click += new System.EventHandler(this.Btn2D_Click);
            // 
            // DroneBtn
            // 
            this.DroneBtn.Dock = System.Windows.Forms.DockStyle.Top;
            this.DroneBtn.FlatAppearance.BorderSize = 0;
            this.DroneBtn.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.DroneBtn.Font = new System.Drawing.Font("楷体", 13.8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.DroneBtn.ForeColor = System.Drawing.Color.Transparent;
            this.DroneBtn.Location = new System.Drawing.Point(0, 60);
            this.DroneBtn.Name = "DroneBtn";
            this.DroneBtn.Size = new System.Drawing.Size(166, 60);
            this.DroneBtn.TabIndex = 0;
            this.DroneBtn.Text = "影像处理";
            this.DroneBtn.UseVisualStyleBackColor = true;
            this.DroneBtn.Click += new System.EventHandler(this.DroneBtn_Click);
            // 
            // MainBtn
            // 
            this.MainBtn.BackColor = System.Drawing.Color.DodgerBlue;
            this.MainBtn.Dock = System.Windows.Forms.DockStyle.Top;
            this.MainBtn.FlatAppearance.BorderSize = 0;
            this.MainBtn.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.MainBtn.Font = new System.Drawing.Font("楷体", 13.8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.MainBtn.ForeColor = System.Drawing.Color.Transparent;
            this.MainBtn.Location = new System.Drawing.Point(0, 0);
            this.MainBtn.Name = "MainBtn";
            this.MainBtn.Size = new System.Drawing.Size(166, 60);
            this.MainBtn.TabIndex = 3;
            this.MainBtn.Text = "开始界面";
            this.MainBtn.UseVisualStyleBackColor = false;
            this.MainBtn.Click += new System.EventHandler(this.MainBtn_Click);
            // 
            // DesktopPanel
            // 
            this.DesktopPanel.BackColor = System.Drawing.Color.WhiteSmoke;
            this.DesktopPanel.Dock = System.Windows.Forms.DockStyle.Fill;
            this.DesktopPanel.Location = new System.Drawing.Point(166, 0);
            this.DesktopPanel.Name = "DesktopPanel";
            this.DesktopPanel.Size = new System.Drawing.Size(1158, 935);
            this.DesktopPanel.TabIndex = 1;
            // 
            // MainForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1324, 935);
            this.Controls.Add(this.DesktopPanel);
            this.Controls.Add(this.MenuPanel);
            this.Name = "MainForm";
            this.Text = "DroneMap";
            this.FormClosed += new System.Windows.Forms.FormClosedEventHandler(this.MainForm_FormClosed);
            this.MenuPanel.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Panel MenuPanel;
        private System.Windows.Forms.Button Btn3D;
        private System.Windows.Forms.Button Btn2D;
        private System.Windows.Forms.Button DroneBtn;
        private System.Windows.Forms.Panel DesktopPanel;
        private System.Windows.Forms.Button MainBtn;
    }
}

