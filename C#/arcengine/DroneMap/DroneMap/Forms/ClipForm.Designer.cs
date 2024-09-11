
namespace DroneMap.Forms
{
    partial class ClipForm
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
            this.inFileBtn = new System.Windows.Forms.Button();
            this.inFileText = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.roiBtn = new System.Windows.Forms.Button();
            this.roiText = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.outFileBtn = new System.Windows.Forms.Button();
            this.outFileText = new System.Windows.Forms.TextBox();
            this.label3 = new System.Windows.Forms.Label();
            this.executeBtn = new System.Windows.Forms.Button();
            this.openFileDialog1 = new System.Windows.Forms.OpenFileDialog();
            this.saveFileDialog1 = new System.Windows.Forms.SaveFileDialog();
            this.SuspendLayout();
            // 
            // inFileBtn
            // 
            this.inFileBtn.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.inFileBtn.Font = new System.Drawing.Font("楷体", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.inFileBtn.Location = new System.Drawing.Point(461, 10);
            this.inFileBtn.Name = "inFileBtn";
            this.inFileBtn.Size = new System.Drawing.Size(54, 30);
            this.inFileBtn.TabIndex = 8;
            this.inFileBtn.Text = "<<<";
            this.inFileBtn.UseVisualStyleBackColor = true;
            this.inFileBtn.Click += new System.EventHandler(this.inFileBtn_Click);
            // 
            // inFileText
            // 
            this.inFileText.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.inFileText.Font = new System.Drawing.Font("楷体", 10.8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.inFileText.Location = new System.Drawing.Point(116, 12);
            this.inFileText.Name = "inFileText";
            this.inFileText.Size = new System.Drawing.Size(338, 28);
            this.inFileText.TabIndex = 7;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("楷体", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.label1.Location = new System.Drawing.Point(14, 16);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(109, 20);
            this.label1.TabIndex = 6;
            this.label1.Text = "输入栅格：";
            // 
            // roiBtn
            // 
            this.roiBtn.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.roiBtn.Font = new System.Drawing.Font("楷体", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.roiBtn.Location = new System.Drawing.Point(461, 55);
            this.roiBtn.Name = "roiBtn";
            this.roiBtn.Size = new System.Drawing.Size(54, 30);
            this.roiBtn.TabIndex = 11;
            this.roiBtn.Text = "<<<";
            this.roiBtn.UseVisualStyleBackColor = true;
            this.roiBtn.Click += new System.EventHandler(this.roiBtn_Click);
            // 
            // roiText
            // 
            this.roiText.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.roiText.Font = new System.Drawing.Font("楷体", 10.8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.roiText.Location = new System.Drawing.Point(116, 56);
            this.roiText.Name = "roiText";
            this.roiText.Size = new System.Drawing.Size(338, 28);
            this.roiText.TabIndex = 10;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("楷体", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.label2.Location = new System.Drawing.Point(14, 60);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(109, 20);
            this.label2.TabIndex = 9;
            this.label2.Text = "裁剪范围：";
            // 
            // outFileBtn
            // 
            this.outFileBtn.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.outFileBtn.Font = new System.Drawing.Font("楷体", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.outFileBtn.Location = new System.Drawing.Point(461, 100);
            this.outFileBtn.Name = "outFileBtn";
            this.outFileBtn.Size = new System.Drawing.Size(54, 30);
            this.outFileBtn.TabIndex = 14;
            this.outFileBtn.Text = "<<<";
            this.outFileBtn.UseVisualStyleBackColor = true;
            this.outFileBtn.Click += new System.EventHandler(this.outFileBtn_Click);
            // 
            // outFileText
            // 
            this.outFileText.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.outFileText.Font = new System.Drawing.Font("楷体", 10.8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.outFileText.Location = new System.Drawing.Point(116, 102);
            this.outFileText.Name = "outFileText";
            this.outFileText.Size = new System.Drawing.Size(338, 28);
            this.outFileText.TabIndex = 13;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Font = new System.Drawing.Font("楷体", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.label3.Location = new System.Drawing.Point(14, 106);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(109, 20);
            this.label3.TabIndex = 12;
            this.label3.Text = "输出栅格：";
            // 
            // executeBtn
            // 
            this.executeBtn.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
            this.executeBtn.Font = new System.Drawing.Font("楷体", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.executeBtn.Location = new System.Drawing.Point(357, 163);
            this.executeBtn.Name = "executeBtn";
            this.executeBtn.Size = new System.Drawing.Size(97, 40);
            this.executeBtn.TabIndex = 15;
            this.executeBtn.Text = "执行";
            this.executeBtn.UseVisualStyleBackColor = true;
            this.executeBtn.Click += new System.EventHandler(this.executeBtn_Click);
            // 
            // openFileDialog1
            // 
            this.openFileDialog1.FileName = "openFileDialog1";
            // 
            // ClipForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(522, 243);
            this.Controls.Add(this.executeBtn);
            this.Controls.Add(this.outFileBtn);
            this.Controls.Add(this.outFileText);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.roiBtn);
            this.Controls.Add(this.roiText);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.inFileBtn);
            this.Controls.Add(this.inFileText);
            this.Controls.Add(this.label1);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.SizableToolWindow;
            this.Name = "ClipForm";
            this.Text = "栅格裁剪";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button inFileBtn;
        private System.Windows.Forms.TextBox inFileText;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Button roiBtn;
        private System.Windows.Forms.TextBox roiText;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Button outFileBtn;
        private System.Windows.Forms.TextBox outFileText;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Button executeBtn;
        private System.Windows.Forms.OpenFileDialog openFileDialog1;
        private System.Windows.Forms.SaveFileDialog saveFileDialog1;
    }
}