
namespace caj_to_pdf
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
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
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.label1 = new System.Windows.Forms.Label();
            this.cajPathText = new System.Windows.Forms.TextBox();
            this.cajPathbtn = new System.Windows.Forms.Button();
            this.showBtn = new System.Windows.Forms.Button();
            this.label2 = new System.Windows.Forms.Label();
            this.cajFileInfoText = new System.Windows.Forms.RichTextBox();
            this.convertBtn = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(40, 30);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(84, 17);
            this.label1.TabIndex = 0;
            this.label1.Text = "caj文件路径：";
            // 
            // cajPathText
            // 
            this.cajPathText.Location = new System.Drawing.Point(117, 27);
            this.cajPathText.Multiline = true;
            this.cajPathText.Name = "cajPathText";
            this.cajPathText.Size = new System.Drawing.Size(202, 23);
            this.cajPathText.TabIndex = 1;
            // 
            // cajPathbtn
            // 
            this.cajPathbtn.Location = new System.Drawing.Point(325, 27);
            this.cajPathbtn.Name = "cajPathbtn";
            this.cajPathbtn.Size = new System.Drawing.Size(75, 23);
            this.cajPathbtn.TabIndex = 2;
            this.cajPathbtn.Text = "打开";
            this.cajPathbtn.UseVisualStyleBackColor = true;
            this.cajPathbtn.Click += new System.EventHandler(this.cajPathbtn_Click);
            // 
            // showBtn
            // 
            this.showBtn.Location = new System.Drawing.Point(130, 62);
            this.showBtn.Name = "showBtn";
            this.showBtn.Size = new System.Drawing.Size(75, 23);
            this.showBtn.TabIndex = 3;
            this.showBtn.Text = "查看文档信息";
            this.showBtn.UseVisualStyleBackColor = true;
            this.showBtn.Click += new System.EventHandler(this.showBtn_Click);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(67, 92);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(44, 17);
            this.label2.TabIndex = 4;
            this.label2.Text = "信息：";
            // 
            // cajFileInfoText
            // 
            this.cajFileInfoText.Font = new System.Drawing.Font("Microsoft YaHei UI", 6.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point);
            this.cajFileInfoText.Location = new System.Drawing.Point(117, 91);
            this.cajFileInfoText.Name = "cajFileInfoText";
            this.cajFileInfoText.Size = new System.Drawing.Size(264, 117);
            this.cajFileInfoText.TabIndex = 5;
            this.cajFileInfoText.Text = "";
            // 
            // convertBtn
            // 
            this.convertBtn.Location = new System.Drawing.Point(227, 62);
            this.convertBtn.Name = "convertBtn";
            this.convertBtn.Size = new System.Drawing.Size(75, 23);
            this.convertBtn.TabIndex = 6;
            this.convertBtn.Text = "转换";
            this.convertBtn.UseVisualStyleBackColor = true;
            this.convertBtn.Click += new System.EventHandler(this.convertBtn_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 17F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(438, 255);
            this.Controls.Add(this.convertBtn);
            this.Controls.Add(this.cajFileInfoText);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.showBtn);
            this.Controls.Add(this.cajPathbtn);
            this.Controls.Add(this.cajPathText);
            this.Controls.Add(this.label1);
            this.Name = "Form1";
            this.Text = "caj To pdf";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox cajPathText;
        private System.Windows.Forms.Button cajPathbtn;
        private System.Windows.Forms.Button showBtn;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.RichTextBox cajFileInfoText;
        private System.Windows.Forms.Button convertBtn;
    }
}

