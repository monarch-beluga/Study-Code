#ifndef DEMO_MAINWINDOW_H
#define DEMO_MAINWINDOW_H

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui {
class Demo_MainWindow;
}
QT_END_NAMESPACE

class Demo_MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    Demo_MainWindow(QWidget *parent = nullptr);
    ~Demo_MainWindow();

private:
    Ui::Demo_MainWindow *ui;
};
#endif // DEMO_MAINWINDOW_H
