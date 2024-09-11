
namespace DroneMap.Forms
{
    partial class DroneForm
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
            this.label1 = new System.Windows.Forms.Label();
            this.imgPathText = new System.Windows.Forms.TextBox();
            this.imgPathBtn = new System.Windows.Forms.Button();
            this.folderBrowserDialog1 = new System.Windows.Forms.FolderBrowserDialog();
            this.outPathBtn = new System.Windows.Forms.Button();
            this.outPathText = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.checkBoxDom = new System.Windows.Forms.CheckBox();
            this.label5 = new System.Windows.Forms.Label();
            this.checkBoxDsm = new System.Windows.Forms.CheckBox();
            this.checkBox25D = new System.Windows.Forms.CheckBox();
            this.checkBox3D = new System.Windows.Forms.CheckBox();
            this.resolutionText = new System.Windows.Forms.TextBox();
            this.label6 = new System.Windows.Forms.Label();
            this.executeBtn = new System.Windows.Forms.Button();
            this.maxConcurrencyText = new System.Windows.Forms.TextBox();
            this.label7 = new System.Windows.Forms.Label();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.checkBoxProcess = new System.Windows.Forms.CheckBox();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("楷体", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.label1.Location = new System.Drawing.Point(13, 13);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(109, 20);
            this.label1.TabIndex = 0;
            this.label1.Text = "影像路径：";
            // 
            // imgPathText
            // 
            this.imgPathText.Font = new System.Drawing.Font("楷体", 10.8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.imgPathText.Location = new System.Drawing.Point(17, 41);
            this.imgPathText.Name = "imgPathText";
            this.imgPathText.Size = new System.Drawing.Size(313, 28);
            this.imgPathText.TabIndex = 1;
            // 
            // imgPathBtn
            // 
            this.imgPathBtn.Font = new System.Drawing.Font("楷体", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.imgPathBtn.Location = new System.Drawing.Point(336, 41);
            this.imgPathBtn.Name = "imgPathBtn";
            this.imgPathBtn.Size = new System.Drawing.Size(54, 30);
            this.imgPathBtn.TabIndex = 2;
            this.imgPathBtn.Text = "<<<";
            this.imgPathBtn.UseVisualStyleBackColor = true;
            this.imgPathBtn.Click += new System.EventHandler(this.imgPathBtn_Click);
            // 
            // outPathBtn
            // 
            this.outPathBtn.Font = new System.Drawing.Font("楷体", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.outPathBtn.Location = new System.Drawing.Point(336, 109);
            this.outPathBtn.Name = "outPathBtn";
            this.outPathBtn.Size = new System.Drawing.Size(54, 30);
            this.outPathBtn.TabIndex = 5;
            this.outPathBtn.Text = "<<<";
            this.outPathBtn.UseVisualStyleBackColor = true;
            this.outPathBtn.Click += new System.EventHandler(this.outPathBtn_Click);
            // 
            // outPathText
            // 
            this.outPathText.Font = new System.Drawing.Font("楷体", 10.8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.outPathText.Location = new System.Drawing.Point(17, 109);
            this.outPathText.Name = "outPathText";
            this.outPathText.Size = new System.Drawing.Size(313, 28);
            this.outPathText.TabIndex = 4;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("楷体", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.label2.Location = new System.Drawing.Point(13, 81);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(109, 20);
            this.label2.TabIndex = 3;
            this.label2.Text = "输出路径：";
            // 
            // label3
            // 
            this.label3.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.label3.AutoSize = true;
            this.label3.Font = new System.Drawing.Font("楷体", 15F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.label3.Location = new System.Drawing.Point(430, 38);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(142, 25);
            this.label3.TabIndex = 7;
            this.label3.Text = "信息输出：";
            // 
            // label4
            // 
            this.label4.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.label4.AutoSize = true;
            this.label4.Font = new System.Drawing.Font("楷体", 15F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.label4.Location = new System.Drawing.Point(14, 400);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(142, 25);
            this.label4.TabIndex = 8;
            this.label4.Text = "参数设置：";
            // 
            // checkBoxDom
            // 
            this.checkBoxDom.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.checkBoxDom.AutoSize = true;
            this.checkBoxDom.Checked = true;
            this.checkBoxDom.CheckState = System.Windows.Forms.CheckState.Checked;
            this.checkBoxDom.Font = new System.Drawing.Font("楷体", 10.8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.checkBoxDom.Location = new System.Drawing.Point(19, 473);
            this.checkBoxDom.Name = "checkBoxDom";
            this.checkBoxDom.Size = new System.Drawing.Size(61, 23);
            this.checkBoxDom.TabIndex = 9;
            this.checkBoxDom.Text = "DOM";
            this.checkBoxDom.UseVisualStyleBackColor = true;
            // 
            // label5
            // 
            this.label5.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.label5.AutoSize = true;
            this.label5.Font = new System.Drawing.Font("楷体", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.label5.Location = new System.Drawing.Point(14, 441);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(169, 20);
            this.label5.TabIndex = 10;
            this.label5.Text = "需要生成的产品：";
            // 
            // checkBoxDsm
            // 
            this.checkBoxDsm.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.checkBoxDsm.AutoSize = true;
            this.checkBoxDsm.Checked = true;
            this.checkBoxDsm.CheckState = System.Windows.Forms.CheckState.Checked;
            this.checkBoxDsm.Font = new System.Drawing.Font("楷体", 10.8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.checkBoxDsm.Location = new System.Drawing.Point(153, 473);
            this.checkBoxDsm.Name = "checkBoxDsm";
            this.checkBoxDsm.Size = new System.Drawing.Size(61, 23);
            this.checkBoxDsm.TabIndex = 11;
            this.checkBoxDsm.Text = "DSM";
            this.checkBoxDsm.UseVisualStyleBackColor = true;
            // 
            // checkBox25D
            // 
            this.checkBox25D.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.checkBox25D.AutoSize = true;
            this.checkBox25D.Font = new System.Drawing.Font("楷体", 10.8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.checkBox25D.Location = new System.Drawing.Point(19, 511);
            this.checkBox25D.Name = "checkBox25D";
            this.checkBox25D.Size = new System.Drawing.Size(111, 23);
            this.checkBox25D.TabIndex = 12;
            this.checkBox25D.Text = "2.5D模型";
            this.checkBox25D.UseVisualStyleBackColor = true;
            // 
            // checkBox3D
            // 
            this.checkBox3D.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.checkBox3D.AutoSize = true;
            this.checkBox3D.Checked = true;
            this.checkBox3D.CheckState = System.Windows.Forms.CheckState.Checked;
            this.checkBox3D.Font = new System.Drawing.Font("楷体", 10.8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.checkBox3D.Location = new System.Drawing.Point(153, 511);
            this.checkBox3D.Name = "checkBox3D";
            this.checkBox3D.Size = new System.Drawing.Size(91, 23);
            this.checkBox3D.TabIndex = 13;
            this.checkBox3D.Text = "3D模型";
            this.checkBox3D.UseVisualStyleBackColor = true;
            // 
            // resolutionText
            // 
            this.resolutionText.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.resolutionText.Font = new System.Drawing.Font("楷体", 10.8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.resolutionText.Location = new System.Drawing.Point(211, 549);
            this.resolutionText.Name = "resolutionText";
            this.resolutionText.Size = new System.Drawing.Size(99, 28);
            this.resolutionText.TabIndex = 15;
            this.resolutionText.Text = "5";
            // 
            // label6
            // 
            this.label6.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.label6.AutoSize = true;
            this.label6.Font = new System.Drawing.Font("楷体", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.label6.Location = new System.Drawing.Point(14, 550);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(209, 20);
            this.label6.TabIndex = 14;
            this.label6.Text = "输出影像分辨率(cm)：";
            // 
            // executeBtn
            // 
            this.executeBtn.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
            this.executeBtn.Font = new System.Drawing.Font("楷体", 13.8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.executeBtn.Location = new System.Drawing.Point(750, 643);
            this.executeBtn.Name = "executeBtn";
            this.executeBtn.Size = new System.Drawing.Size(97, 40);
            this.executeBtn.TabIndex = 16;
            this.executeBtn.Text = "执行";
            this.executeBtn.UseVisualStyleBackColor = true;
            this.executeBtn.Click += new System.EventHandler(this.executeBtn_Click);
            // 
            // maxConcurrencyText
            // 
            this.maxConcurrencyText.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.maxConcurrencyText.Font = new System.Drawing.Font("楷体", 10.8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.maxConcurrencyText.Location = new System.Drawing.Point(212, 596);
            this.maxConcurrencyText.Name = "maxConcurrencyText";
            this.maxConcurrencyText.Size = new System.Drawing.Size(99, 28);
            this.maxConcurrencyText.TabIndex = 18;
            // 
            // label7
            // 
            this.label7.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.label7.AutoSize = true;
            this.label7.Font = new System.Drawing.Font("楷体", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.label7.Location = new System.Drawing.Point(14, 597);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(129, 20);
            this.label7.TabIndex = 17;
            this.label7.Text = "最大并发数：";
            // 
            // richTextBox1
            // 
            this.richTextBox1.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.richTextBox1.BackColor = System.Drawing.SystemColors.Info;
            this.richTextBox1.Location = new System.Drawing.Point(435, 82);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.ReadOnly = true;
            this.richTextBox1.Size = new System.Drawing.Size(484, 538);
            this.richTextBox1.TabIndex = 19;
            this.richTextBox1.Text = "";
            // 
            // checkBoxProcess
            // 
            this.checkBoxProcess.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.checkBoxProcess.AutoSize = true;
            this.checkBoxProcess.Checked = true;
            this.checkBoxProcess.CheckState = System.Windows.Forms.CheckState.Checked;
            this.checkBoxProcess.Font = new System.Drawing.Font("楷体", 10.8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.checkBoxProcess.Location = new System.Drawing.Point(799, 43);
            this.checkBoxProcess.Name = "checkBoxProcess";
            this.checkBoxProcess.Size = new System.Drawing.Size(111, 23);
            this.checkBoxProcess.TabIndex = 20;
            this.checkBoxProcess.Text = "后台处理";
            this.checkBoxProcess.UseVisualStyleBackColor = true;
            // 
            // DroneForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(971, 722);
            this.Controls.Add(this.checkBoxProcess);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.maxConcurrencyText);
            this.Controls.Add(this.label7);
            this.Controls.Add(this.executeBtn);
            this.Controls.Add(this.resolutionText);
            this.Controls.Add(this.label6);
            this.Controls.Add(this.checkBox3D);
            this.Controls.Add(this.checkBox25D);
            this.Controls.Add(this.checkBoxDsm);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.checkBoxDom);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.outPathBtn);
            this.Controls.Add(this.outPathText);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.imgPathBtn);
            this.Controls.Add(this.imgPathText);
            this.Controls.Add(this.label1);
            this.Name = "DroneForm";
            this.Text = "DroneForm";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox imgPathText;
        private System.Windows.Forms.Button imgPathBtn;
        private System.Windows.Forms.FolderBrowserDialog folderBrowserDialog1;
        private System.Windows.Forms.Button outPathBtn;
        private System.Windows.Forms.TextBox outPathText;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.CheckBox checkBoxDom;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.CheckBox checkBoxDsm;
        private System.Windows.Forms.CheckBox checkBox25D;
        private System.Windows.Forms.CheckBox checkBox3D;
        private System.Windows.Forms.TextBox resolutionText;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.Button executeBtn;
        private System.Windows.Forms.TextBox maxConcurrencyText;
        private System.Windows.Forms.Label label7;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.CheckBox checkBoxProcess;
    }
}