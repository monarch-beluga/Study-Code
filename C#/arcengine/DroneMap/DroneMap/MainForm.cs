using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using DroneMap.Forms;
using Map_GIS;

namespace DroneMap
{
    public partial class MainForm : Form
    {
        private Button currentBtn;
        private Form currentForm;
        private DroneForm droneForm;
        private Form2D form2D;
        private Form3D form3D;

        public MainForm()
        {
            InitializeComponent();
            form2D = new Form2D();
            OpenChildForm(form2D);
        }

        private void ActivateButton(object senderBtn)
        {
            if (senderBtn != null)
            {
                DisableButton();
                currentBtn = (Button)senderBtn;
                currentBtn.BackColor = Color.DeepSkyBlue;
                currentBtn.ForeColor = Color.Black;
                currentBtn.Font = new Font(currentBtn.Font, FontStyle.Bold);
                
            }
        }

        private void DisableButton()
        {
            if (currentBtn != null)
            {
                currentBtn.BackColor = Color.DodgerBlue;
                currentBtn.ForeColor = Color.Transparent;
                currentBtn.Font = new Font(currentBtn.Font, FontStyle.Regular);
            }
        }

        private void OpenChildForm(Form childForm)
        {
            if (currentForm != null)
                currentForm.Visible = false;
            currentForm = childForm;
            childForm.TopLevel = false;
            childForm.FormBorderStyle = FormBorderStyle.None;
            childForm.Dock = DockStyle.Fill;
            DesktopPanel.Controls.Add(childForm);
            DesktopPanel.Tag = childForm;
            childForm.BringToFront();
            childForm.Show();
        }

        private void ActivateChildForm(Form childForm)
        {
            if (currentForm != null)
                currentForm.Visible = false;
            currentForm = childForm;
            currentForm.Visible = true;
        }

        private void MainBtn_Click(object sender, EventArgs e)
        {
            ActivateButton(sender);
            if (currentForm != null)
                currentForm.Visible = false;
        }

        private void Btn2D_Click(object sender, EventArgs e)
        {
            ActivateButton(sender);
            if (form2D == null)
            {
                form2D = new Form2D();
                OpenChildForm(form2D);
            }
            else
                ActivateChildForm(form2D);
        }

        private void DroneBtn_Click(object sender, EventArgs e)
        {
            ActivateButton(sender);
            if (droneForm == null)
            {
                droneForm = new DroneForm();
                OpenChildForm(droneForm);
            }
            else
                ActivateChildForm(droneForm);
        }

        private void Btn3D_Click(object sender, EventArgs e)
        {
            ActivateButton(sender);
            if (form3D == null)
            {
                form3D = new Form3D();
                OpenChildForm(form3D);
            }
            else
                ActivateChildForm(form3D);
        }

        private void MainForm_FormClosed(object sender, FormClosedEventArgs e)
        {
            WindowManager.CloseWindow();
        }
    }
}