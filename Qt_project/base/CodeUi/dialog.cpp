#include "dialog.h"

#include <QHBoxLayout>
#include <QVBoxLayout>

Dialog::Dialog(QWidget *parent)
    : QDialog(parent)
{
    resize(300, 400);
    initUi();
    iniSignalSlots();
}

Dialog::~Dialog()
{
}

void Dialog::initUi()
{
    groupFontStyle = new QGroupBox(tr("字体样式"), this);
    groupFontColor = new QGroupBox(tr("字体颜色"), this);

    checkBoxUnderLine = new QCheckBox("Underline");
    checkBoxBold = new QCheckBox("Bold");
    checkBoxItalic = new QCheckBox("Italic");
    // 设置局部控件布局
    QHBoxLayout *hBoxLayout1 = new QHBoxLayout;
    hBoxLayout1->addWidget(checkBoxUnderLine);
    hBoxLayout1->addWidget(checkBoxBold);
    hBoxLayout1->addWidget(checkBoxItalic);
    groupFontStyle->setLayout(hBoxLayout1);

    radioButtonBlack = new QRadioButton("Black");
    radioButtonBlue = new QRadioButton("Blue");
    radioButtonRed = new QRadioButton("Red");
    QHBoxLayout *hBoxLayout2 = new QHBoxLayout;
    hBoxLayout2->addWidget(radioButtonBlack);
    hBoxLayout2->addWidget(radioButtonBlue);
    hBoxLayout2->addWidget(radioButtonRed);
    groupFontColor->setLayout(hBoxLayout2);

    spacer1 = new QSpacerItem(60, 30);
    spacer2 = new QSpacerItem(60, 30);
    buttonCancel = new QPushButton("取消");
    buttonQuit = new QPushButton("退出");
    buttonSure = new QPushButton("确定");
    QHBoxLayout *hBoxLayout3 = new QHBoxLayout;
    hBoxLayout3->addItem(spacer1);
    hBoxLayout3->addWidget(buttonSure);
    hBoxLayout3->addWidget(buttonCancel);
    hBoxLayout3->addItem(spacer2);
    hBoxLayout3->addWidget(buttonQuit);

    textEdit = new QPlainTextEdit();
    QFont font = textEdit->font();
    font.setPointSize(20);
    textEdit->setFont(font);
    textEdit->setPlainText("Hello World\n\nThis is Monarch");

    // 设置总体布局
    QVBoxLayout *vBoxLayout = new QVBoxLayout;
    vBoxLayout->addWidget(groupFontStyle);
    vBoxLayout->addWidget(groupFontColor);
    vBoxLayout->addWidget(textEdit);
    vBoxLayout->addLayout(hBoxLayout3);
    this->setLayout(vBoxLayout);
}

void Dialog::iniSignalSlots()
{
    // 关联qt自带槽
    connect(buttonSure, SIGNAL(clicked()), this, SLOT(accept()));
    connect(buttonQuit, SIGNAL(clicked()), this, SLOT(reject()));
    connect(buttonCancel, SIGNAL(clicked()), this, SLOT(close()));

    // 关联自定义槽
    connect(checkBoxUnderLine, SIGNAL(clicked(bool)), this, SLOT(on_checkBoxUnderLine(bool)));
    connect(checkBoxBold, SIGNAL(clicked(bool)), this, SLOT(on_checkBoxBold(bool)));
    connect(checkBoxItalic, SIGNAL(clicked(bool)), this, SLOT(on_checkBoxItalic(bool)));

    // 多控件绑定一个槽
    connect(radioButtonBlack, SIGNAL(clicked()), this, SLOT(setTextFontColor()));
    connect(radioButtonRed, SIGNAL(clicked()), this, SLOT(setTextFontColor()));
    connect(radioButtonBlue, SIGNAL(clicked()), this, SLOT(setTextFontColor()));

}

void Dialog::on_checkBoxUnderLine(bool checked)
{
    QFont font = textEdit->font();
    font.setUnderline(checked);
    textEdit->setFont(font);
}

void Dialog::on_checkBoxBold(bool checked)
{
    QFont font = textEdit->font();
    font.setBold(checked);
    textEdit->setFont(font);
}

void Dialog::on_checkBoxItalic(bool checked)
{
    QFont font = textEdit->font();
    font.setItalic(checked);
    textEdit->setFont(font);
}

void Dialog::setTextFontColor()
{
    // 获取文本框的Palette
    QPalette plet = textEdit->palette();
    // 默认情况下设置颜色为black
    plet.setColor(QPalette::Text, Qt::black);

    // 判断三个控件的选取情况
    if(radioButtonBlack->isChecked())                   // 判断是否勾选
        plet.setColor(QPalette::Text, Qt::black);           // 设置颜色为black
    else if(radioButtonRed->isChecked())
        plet.setColor(QPalette::Text, Qt::red);             // 设置颜色为red
    else if(radioButtonBlue->isChecked())
        plet.setColor(QPalette::Text, Qt::blue);            // 设置颜色为blue

    // 设置文本框的Palette
    textEdit->setPalette(plet);
}



