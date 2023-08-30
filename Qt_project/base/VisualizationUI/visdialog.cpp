#include "visdialog.h"
#include "ui_visdialog.h"

VisDialog::VisDialog(QWidget *parent)
    : QDialog(parent)
    , ui(new Ui::VisDialog)
{
    ui->setupUi(this);
    // 三个控件绑定一函数
    QObject::connect(ui->radioButtonBlack, SIGNAL(clicked()), this, SLOT(setTextFontColor()));
    QObject::connect(ui->radioButtonBlue, SIGNAL(clicked()), this, SLOT(setTextFontColor()));
    QObject::connect(ui->radioButtonRed, SIGNAL(clicked()), this, SLOT(setTextFontColor()));
    /*
    四个参数：
        第一个为需要绑定的控件，一般通过ui去查找
        第二个为信号类型，这里选择的是点击信号 clicked()
        第三个为接受窗口，这里的this为VisDialog，表示这个窗体类本身
        第四个为定义的函数
    */
}

VisDialog::~VisDialog()
{
    delete ui;
}


void VisDialog::on_checkBoxUnderline_clicked(bool checked)
{
    QFont font = ui->plainTextEdit->font();                 // 获取字体样式
    font.setUnderline(checked);                             // 设置字体下划线
    ui->plainTextEdit->setFont(font);                       // 修改为新的字体样式
}

void VisDialog::on_checkBoxItalic_clicked(bool checked)
{
    QFont font = ui->plainTextEdit->font();
    font.setItalic(checked);                                // 设置字体斜体
    ui->plainTextEdit->setFont(font);
}

void VisDialog::on_checkBoxBold_clicked(bool checked)
{
    QFont font = ui->plainTextEdit->font();
    font.setBold(checked);                                  // 设置字体粗体
    ui->plainTextEdit->setFont(font);
}

void VisDialog::setTextFontColor()
{
    QPalette pale = ui->plainTextEdit->palette();           // 获取调色板
    // 默认情况下设置颜色为black
    pale.setColor(QPalette::Text, Qt::black);

    // 判断三个控件的选取情况
    if(ui->radioButtonBlack->isChecked())                   // 判断是否勾选
        pale.setColor(QPalette::Text, Qt::black);           // 设置颜色为black
    else if(ui->radioButtonRed->isChecked())
        pale.setColor(QPalette::Text, Qt::red);             // 设置颜色为red
    else if(ui->radioButtonBlue->isChecked())
        pale.setColor(QPalette::Text, Qt::blue);            // 设置颜色为blue

    ui->plainTextEdit->setPalette(pale);
}




