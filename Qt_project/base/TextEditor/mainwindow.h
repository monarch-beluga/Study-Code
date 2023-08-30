#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QProgressBar>
#include <QLabel>
#include <QSpinBox>
#include <QFontComboBox>
#include <QHBoxLayout>
#include <QVBoxLayout>
#include <QWidget>

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
    void on_actToolbarLab_triggered(bool checked);

    void on_actFontBold_triggered(bool checked);

    void on_actFontItalic_triggered(bool checked);

    void on_actFontUnder_triggered(bool checked);

    void on_textEdit_copyAvailable(bool b);

    void on_textEdit_selectionChanged();

    void on_spinFontSize_valueChanged(int aFontSize);

    void on_comboFont_currentIndexChanged(const QString &arg1);

private:
    Ui::MainWindow *ui;
    QLabel *fLabCurFile;
    QProgressBar *progressBar;
    QSpinBox *spinFontSize;
    QFontComboBox *comboFont;

    void initUI();
    void initSingalSlots();
};
#endif // MAINWINDOW_H
