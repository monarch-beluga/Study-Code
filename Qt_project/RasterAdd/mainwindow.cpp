#include "mainwindow.h"
#include "./ui_mainwindow.h"
#include <QFileDialog>
#include <QMessageBox>
#include "gdal_raster_add.h"
#include <ctime>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_file1Button_clicked()
{
    QString path;
    if (open_dir)
    {
        path = "C:/";
        open_dir = false;
    }
    else
        path = "";
    QString fileName = QFileDialog::getOpenFileName(
            this,
            tr("open Tiff."),
            path,
            tr("images(*.tif *.flt);;All files(*.*)"));
    if (fileName.isEmpty())
        QMessageBox::warning(this, "Warning!", "Failed to open the video!");
    else
        ui->file1Text->setText(fileName);
}

void MainWindow::on_file2Button_clicked()
{
    QString path;
    if (open_dir)
    {
        path = "C:/";
        open_dir = false;
    }
    else
        path = "";
    QString fileName = QFileDialog::getOpenFileName(
            this,
            tr("open Tiff."),
            path,
            tr("images(*.tif *.flt);;All files(*.*)"));
    if (fileName.isEmpty())
        QMessageBox::warning(this, "Warning!", "Failed to open the video!");
    else
        ui->file2Text->setText(fileName);
}



void MainWindow::on_outFileButton_clicked()
{
    QString path;
    if (open_dir)
    {
        path = "C:/";
        open_dir = false;
    }
    else
        path = "";
    QString fileName = QFileDialog::getSaveFileName(
            this,
            tr("open Tiff."),
            path,
            tr("images(*.tif *.flt);;All files(*.*)"));
    if (fileName.isEmpty())
        QMessageBox::warning(this, "Warning!", "Failed to open the video!");
    else
        ui->outFileText->setText(fileName);
}

void MainWindow::on_execute_clicked()
{
    string file1 = ui->file1Text->text().toStdString();
    string file2 = ui->file2Text->text().toStdString();
    string outfile = ui->outFileText->text().toStdString();

    double start = clock();
    int err = raster_add(file1, file2, outfile);
    double end = clock();

    if (err)
        ui->result->setText("Failed!");
    else
        ui->result->setText(tr("Success! spend %1s").arg((end - start) / 1000, 0, 'f', 3));
}
