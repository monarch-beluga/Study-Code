
namespace DroneMap.Forms
{
    partial class CutFillForm
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
            this.beforeRasterBtn = new System.Windows.Forms.Button();
            this.beforeRasterText = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.afterRasterBtn = new System.Windows.Forms.Button();
            this.afterRasterText = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.roiFileBtn = new System.Windows.Forms.Button();
            this.roiFileText = new System.Windows.Forms.TextBox();
            this.label3 = new System.Windows.Forms.Label();
            this.outFileBtn = new System.Windows.Forms.Button();
            this.outFileText = new System.Windows.Forms.TextBox();
            this.label4 = new System.Windows.Forms.Label();
            this.executeBtn = new System.Windows.Forms.Button();
            this.saveFileDialog1 = new System.Windows.Forms.SaveFileDialog();
            this.openFileDialog1 = new System.Windows.Forms.OpenFileDialog();
            this.SuspendLayout();
            // 
            // beforeRasterBtn
            // 
            this.beforeRasterBtn.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.beforeRasterBtn.Font = new System.Drawing.Font("楷体", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.beforeRasterBtn.Location = new System.Drawing.Point(450, 10);
            this.beforeRasterBtn.Name = "beforeRasterBtn";
            this.beforeRasterBtn.Size = new System.Drawing.Size(54, 30);
            this.beforeRasterBtn.TabIndex = 11;
            this.beforeRasterBtn.Text = "<<<";
            this.beforeRasterBtn.UseVisualStyleBackColor = true;
            this.beforeRasterBtn.Click += new System.EventHandler(this.beforeRasterBtn_Click);
            // 
            // beforeRasterText
            // 
            this.beforeRasterText.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.beforeRasterText.Font = new System.Drawing.Font("楷体", 10.8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.beforeRasterText.Location = new System.Drawing.Point(144, 12);
            this.beforeRasterText.Name = "beforeRasterText";
            this.beforeRasterText.Size = new System.Drawing.Size(299, 28);
            this.beforeRasterText.TabIndex = 10;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("楷体", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.label1.Location = new System.Drawing.Point(7, 16);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(149, 20);
            this.label1.TabIndex = 9;
            this.label1.Text = "填挖方前栅格：";
            // 
            // afterRasterBtn
            // 
            this.afterRasterBtn.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.afterRasterBtn.Font = new System.Drawing.Font("楷体", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.afterRasterBtn.Location = new System.Drawing.Point(450, 57);
            this.afterRasterBtn.Name = "afterRasterBtn";
            this.afterRasterBtn.Size = new System.Drawing.Size(54, 30);
            this.afterRasterBtn.TabIndex = 14;
            this.afterRasterBtn.Text = "<<<";
            this.afterRasterBtn.UseVisualStyleBackColor = true;
            this.afterRasterBtn.Click += new System.EventHandler(this.afterRasterBtn_Click);
            // 
            // afterRasterText
            // 
            this.afterRasterText.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.afterRasterText.Font = new System.Drawing.Font("楷体", 10.8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.afterRasterText.Location = new System.Drawing.Point(144, 59);
            this.afterRasterText.Name = "afterRasterText";
            this.afterRasterText.Size = new System.Drawing.Size(299, 28);
            this.afterRasterText.TabIndex = 13;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("楷体", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.label2.Location = new System.Drawing.Point(7, 63);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(149, 20);
            this.label2.TabIndex = 12;
            this.label2.Text = "田挖方后栅格：";
            // 
            // roiFileBtn
            // 
            this.roiFileBtn.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.roiFileBtn.Font = new System.Drawing.Font("楷体", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.roiFileBtn.Location = new System.Drawing.Point(450, 106);
            this.roiFileBtn.Name = "roiFileBtn";
            this.roiFileBtn.Size = new System.Drawing.Size(54, 30);
            this.roiFileBtn.TabIndex = 17;
            this.roiFileBtn.Text = "<<<";
            this.roiFileBtn.UseVisualStyleBackColor = true;
            this.roiFileBtn.Click += new System.EventHandler(this.roiFileBtn_Click);
            // 
            // roiFileText
            // 
            this.roiFileText.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.roiFileText.Font = new System.Drawing.Font("楷体", 10.8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.roiFileText.Location = new System.Drawing.Point(105, 107);
            this.roiFileText.Name = "roiFileText";
            this.roiFileText.Size = new System.Drawing.Size(338, 28);
            this.roiFileText.TabIndex = 16;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Font = new System.Drawing.Font("楷体", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.label3.Location = new System.Drawing.Point(3, 111);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(109, 20);
            this.label3.TabIndex = 15;
            this.label3.Text = "计算范围：";
            // 
            // outFileBtn
            // 
            this.outFileBtn.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.outFileBtn.Font = new System.Drawing.Font("楷体", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.outFileBtn.Location = new System.Drawing.Point(450, 156);
            this.outFileBtn.Name = "outFileBtn";
            this.outFileBtn.Size = new System.Drawing.Size(54, 30);
            this.outFileBtn.TabIndex = 20;
            this.outFileBtn.Text = "<<<";
            this.outFileBtn.UseVisualStyleBackColor = true;
            this.outFileBtn.Click += new System.EventHandler(this.outFileBtn_Click);
            // 
            // outFileText
            // 
            this.outFileText.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.outFileText.Font = new System.Drawing.Font("楷体", 10.8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.outFileText.Location = new System.Drawing.Point(105, 158);
            this.outFileText.Name = "outFileText";
            this.outFileText.Size = new System.Drawing.Size(338, 28);
            this.outFileText.TabIndex = 19;
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Font = new System.Drawing.Font("楷体", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.label4.Location = new System.Drawing.Point(3, 162);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(109, 20);
            this.label4.TabIndex = 18;
            this.label4.Text = "输出栅格：";
            // 
            // executeBtn
            // 
            this.executeBtn.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
            this.executeBtn.Font = new System.Drawing.Font("楷体", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.executeBtn.Location = new System.Drawing.Point(346, 217);
            this.executeBtn.Name = "executeBtn";
            this.executeBtn.Size = new System.Drawing.Size(97, 40);
            this.executeBtn.TabIndex = 21;
            this.executeBtn.Text = "执行";
            this.executeBtn.UseVisualStyleBackColor = true;
            this.executeBtn.Click += new System.EventHandler(this.executeBtn_Click);
            // 
            // openFileDialog1
            // 
            this.openFileDialog1.FileName = "openFileDialog1";
            // 
            // CutFillForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(522, 279);
            this.Controls.Add(this.executeBtn);
            this.Controls.Add(this.outFileBtn);
            this.Controls.Add(this.outFileText);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.roiFileBtn);
            this.Controls.Add(this.roiFileText);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.afterRasterBtn);
            this.Controls.Add(this.afterRasterText);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.beforeRasterBtn);
            this.Controls.Add(this.beforeRasterText);
            this.Controls.Add(this.label1);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.SizableToolWindow;
            this.Name = "CutFillForm";
            this.Text = "CutFillForm";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button beforeRasterBtn;
        private System.Windows.Forms.TextBox beforeRasterText;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Button afterRasterBtn;
        private System.Windows.Forms.TextBox afterRasterText;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Button roiFileBtn;
        private System.Windows.Forms.TextBox roiFileText;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Button outFileBtn;
        private System.Windows.Forms.TextBox outFileText;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Button executeBtn;
        private System.Windows.Forms.SaveFileDialog saveFileDialog1;
        private System.Windows.Forms.OpenFileDialog openFileDialog1;
    }
}