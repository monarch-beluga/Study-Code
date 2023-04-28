#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void on_file1Button_clicked();

    void on_file2Button_clicked();

    void on_outFileButton_clicked();

    void on_execute_clicked();

private:
    Ui::MainWindow *ui;
    bool open_dir = true;
};
#endif // MAINWINDOW_H
