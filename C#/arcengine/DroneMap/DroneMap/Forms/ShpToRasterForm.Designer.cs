
namespace DroneMap.Forms
{
    partial class ShpToRasterForm
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
            this.outFileBtn = new System.Windows.Forms.Button();
            this.outFileText = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.FieldComboBox = new System.Windows.Forms.ComboBox();
            this.label3 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.scaleText = new System.Windows.Forms.TextBox();
            this.openFileDialog1 = new System.Windows.Forms.OpenFileDialog();
            this.saveFileDialog1 = new System.Windows.Forms.SaveFileDialog();
            this.executeBtn = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // inFileBtn
            // 
            this.inFileBtn.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.inFileBtn.Font = new System.Drawing.Font("楷体", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.inFileBtn.Location = new System.Drawing.Point(448, 11);
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
            this.inFileText.Location = new System.Drawing.Point(107, 12);
            this.inFileText.Name = "inFileText";
            this.inFileText.Size = new System.Drawing.Size(334, 28);
            this.inFileText.TabIndex = 7;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("楷体", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.label1.Location = new System.Drawing.Point(5, 16);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(109, 20);
            this.label1.TabIndex = 6;
            this.label1.Text = "输入矢量：";
            // 
            // outFileBtn
            // 
            this.outFileBtn.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.outFileBtn.Font = new System.Drawing.Font("楷体", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.outFileBtn.Location = new System.Drawing.Point(448, 117);
            this.outFileBtn.Name = "outFileBtn";
            this.outFileBtn.Size = new System.Drawing.Size(54, 30);
            this.outFileBtn.TabIndex = 11;
            this.outFileBtn.Text = "<<<";
            this.outFileBtn.UseVisualStyleBackColor = true;
            this.outFileBtn.Click += new System.EventHandler(this.outFileBtn_Click);
            // 
            // outFileText
            // 
            this.outFileText.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.outFileText.Font = new System.Drawing.Font("楷体", 10.8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.outFileText.Location = new System.Drawing.Point(107, 118);
            this.outFileText.Name = "outFileText";
            this.outFileText.Size = new System.Drawing.Size(334, 28);
            this.outFileText.TabIndex = 10;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("楷体", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.label2.Location = new System.Drawing.Point(5, 122);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(109, 20);
            this.label2.TabIndex = 9;
            this.label2.Text = "输出栅格：";
            // 
            // FieldComboBox
            // 
            this.FieldComboBox.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.FieldComboBox.FormattingEnabled = true;
            this.FieldComboBox.Location = new System.Drawing.Point(107, 65);
            this.FieldComboBox.Name = "FieldComboBox";
            this.FieldComboBox.Size = new System.Drawing.Size(334, 28);
            this.FieldComboBox.TabIndex = 13;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Font = new System.Drawing.Font("楷体", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.label3.Location = new System.Drawing.Point(5, 69);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(109, 20);
            this.label3.TabIndex = 12;
            this.label3.Text = "赋值字段：";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Font = new System.Drawing.Font("楷体", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.label4.Location = new System.Drawing.Point(5, 170);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(109, 20);
            this.label4.TabIndex = 14;
            this.label4.Text = "像元大小：";
            // 
            // scaleText
            // 
            this.scaleText.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.scaleText.Font = new System.Drawing.Font("楷体", 10.8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.scaleText.Location = new System.Drawing.Point(107, 169);
            this.scaleText.Name = "scaleText";
            this.scaleText.Size = new System.Drawing.Size(334, 28);
            this.scaleText.TabIndex = 15;
            // 
            // openFileDialog1
            // 
            this.openFileDialog1.FileName = "openFileDialog1";
            // 
            // executeBtn
            // 
            this.executeBtn.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
            this.executeBtn.Font = new System.Drawing.Font("楷体", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.executeBtn.Location = new System.Drawing.Point(344, 236);
            this.executeBtn.Name = "executeBtn";
            this.executeBtn.Size = new System.Drawing.Size(97, 40);
            this.executeBtn.TabIndex = 16;
            this.executeBtn.Text = "执行";
            this.executeBtn.UseVisualStyleBackColor = true;
            // 
            // ShpToRasterForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(10F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(522, 313);
            this.Controls.Add(this.executeBtn);
            this.Controls.Add(this.scaleText);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.FieldComboBox);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.outFileBtn);
            this.Controls.Add(this.outFileText);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.inFileBtn);
            this.Controls.Add(this.inFileText);
            this.Controls.Add(this.label1);
            this.Font = new System.Drawing.Font("楷体", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.SizableToolWindow;
            this.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.Name = "ShpToRasterForm";
            this.Text = "矢量转栅格";
            this.FormClosed += new System.Windows.Forms.FormClosedEventHandler(this.ShpToRasterForm_FormClosed);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button inFileBtn;
        private System.Windows.Forms.TextBox inFileText;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Button outFileBtn;
        private System.Windows.Forms.TextBox outFileText;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.ComboBox FieldComboBox;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.TextBox scaleText;
        private System.Windows.Forms.OpenFileDialog openFileDialog1;
        private System.Windows.Forms.SaveFileDialog saveFileDialog1;
        private System.Windows.Forms.Button executeBtn;
    }
}