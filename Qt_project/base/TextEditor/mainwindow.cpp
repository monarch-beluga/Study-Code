#include "mainwindow.h"
#include "./ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    initUI();
    initSingalSlots();
}

MainWindow::~MainWindow()
{
    delete ui;
}


void MainWindow::on_actToolbarLab_triggered(bool checked)
{
    if(checked)
        ui->toolBar->setToolButtonStyle(Qt::ToolButtonTextUnderIcon);
    else
        ui->toolBar->setToolButtonStyle(Qt::ToolButtonIconOnly);
}

void MainWindow::initUI()
{
    setCentralWidget(ui->textEdit);
    ui->textEdit->setFontPointSize(10);

    fLabCurFile = new QLabel;
    fLabCurFile->setMidLineWidth(150);
    fLabCurFile->setText("当前文件: ");
    // 状态栏左侧添加组件
    ui->statusbar->addWidget(fLabCurFile);

    progressBar = new QProgressBar;
    // 设置值区间
    progressBar->setMaximum(50);
    progressBar->setMinimum(5);
    progressBar->setMaximumWidth(200);
    progressBar->setValue(ui->textEdit->font().pointSize());
    // 状态栏右侧添加组件
    ui->statusbar->addPermanentWidget(progressBar);

    spinFontSize = new QSpinBox;
    spinFontSize->setMaximumWidth(80);
    // 设置值区间
    spinFontSize->setMaximum(50);
    spinFontSize->setMinimum(5);
    // 设置默认值
    spinFontSize->setValue(10);
    ui->toolBar->addWidget(new QLabel("字体大小"));
    ui->toolBar->addWidget(spinFontSize);

    comboFont = new QFontComboBox;
    ui->toolBar->addWidget(new QLabel("字体"));
    comboFont->setMaximumWidth(80);
    ui->toolBar->addWidget(comboFont);
}

void MainWindow::initSingalSlots()
{
    connect(spinFontSize, SIGNAL(valueChanged(int)),
            this, SLOT(on_spinFontSize_valueChanged(int)));

    connect(comboFont, SIGNAL(currentIndexChanged(const QString&)),
            this, SLOT(on_comboFont_currentIndexChanged(const QString&)));
}

void MainWindow::on_actFontBold_triggered(bool checked)
{
    if (checked)
        ui->textEdit->setFontWeight(QFont::Bold);
    else
        ui->textEdit->setFontWeight(QFont::Normal);
}

void MainWindow::on_actFontItalic_triggered(bool checked)
{
    ui->textEdit->setFontItalic(checked);
}

void MainWindow::on_actFontUnder_triggered(bool checked)
{
    ui->textEdit->setFontUnderline(checked);
}

void MainWindow::on_textEdit_copyAvailable(bool b)
{
    ui->actCut->setEnabled(b);
    ui->actCopy->setEnabled(b);
    ui->actPaste->setEnabled(ui->textEdit->canPaste());
}

void MainWindow::on_textEdit_selectionChanged()
{
    QTextCharFormat fmt;
    fmt = ui->textEdit->currentCharFormat();
    ui->actFontBold->setChecked(fmt.font().bold());
    ui->actFontItalic->setChecked(fmt.fontItalic());
    ui->actFontUnder->setChecked(fmt.fontUnderline());
}

void MainWindow::on_spinFontSize_valueChanged(int aFontSize)
{
    QTextCharFormat fmt;
    fmt.setFontPointSize(aFontSize);
    ui->textEdit->mergeCurrentCharFormat(fmt);
    progressBar->setValue(aFontSize);
}

void MainWindow::on_comboFont_currentIndexChanged(const QString &arg1)
{
    QTextCharFormat fmt;
    fmt.setFontFamily(arg1);
    ui->textEdit->mergeCurrentCharFormat(fmt);
}
