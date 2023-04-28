#include "visdialog.h"

#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    VisDialog w;
    w.show();
    return a.exec();
}
