#include "mainwindow.h"
#include "./ui_mainwindow.h"
#include <proj.h>

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

void MainWindow::on_pushButton_clicked()
{
    double lat = ui->latText->text().toDouble();
    double lon = ui->lonText->text().toDouble();
    ui->message->append(tr("longitude: %1, latitude: %2\n").arg(lon, 0, 'f', 3).arg(lat, 0, 'f', 3));

    PJ_CONTEXT *C;
    PJ *P;
    PJ *norm;
    PJ_COORD a, b;

    C = proj_context_create();
    P = proj_create_crs_to_crs (C, "EPSG:4326", "EPSG:3857", NULL);
    norm = proj_normalize_for_visualization(C, P);
    proj_destroy(P);
//    P = norm;
    a = proj_coord(lon, lat, 0, 0);
    b = proj_trans(norm, PJ_FWD, a);
    ui->message->append(tr("easting: %1, northing: %2\n").arg(b.enu.e, 0, 'f', 3).arg(b.enu.n, 0, 'f', 3));

    proj_destroy(norm);
    proj_context_destroy(C);
}
