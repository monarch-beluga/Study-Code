#include "dialog.h"

#include <QHBoxLayout>
#include <QVBoxLayout>

Dialog::Dialog(QWidget *parent)
    : QDialog(parent)
{
    resize(300, 400);
    initUi();
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
    setLayout(vBoxLayout);
}



