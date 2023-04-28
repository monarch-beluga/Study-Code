#ifndef VISDIALOG_H
#define VISDIALOG_H

#include <QDialog>

QT_BEGIN_NAMESPACE
namespace Ui { class VisDialog; }
QT_END_NAMESPACE

class VisDialog : public QDialog
{
    Q_OBJECT

public:
    VisDialog(QWidget *parent = nullptr);
    ~VisDialog();

private slots:
    void on_checkBoxUnderline_clicked(bool checked);

    void on_checkBoxItalic_clicked(bool checked);

    void on_checkBoxBold_clicked(bool checked);

    void setTextFontColor();


private:
    Ui::VisDialog *ui;
};
#endif // VISDIALOG_H
