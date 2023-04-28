#include "demo_mainwindow.h"
#include "ui_demo_mainwindow.h"

Demo_MainWindow::Demo_MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::Demo_MainWindow)
{
    ui->setupUi(this);
}

Demo_MainWindow::~Demo_MainWindow()
{
    delete ui;
}

