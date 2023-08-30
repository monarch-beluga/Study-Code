#ifndef DIALOG_H
#define DIALOG_H

#include <QDialog>
#include <QPushButton>
#include <QCheckBox>
#include <QRadioButton>
#include <QPlainTextEdit>
#include <QGroupBox>
#include <QSpacerItem>

class Dialog : public QDialog
{
    Q_OBJECT

public:
    Dialog(QWidget *parent = nullptr);
    ~Dialog();

private:
    QGroupBox *groupFontStyle;
    QGroupBox *groupFontColor;

    QCheckBox *checkBoxUnderLine;
    QCheckBox *checkBoxBold;
    QCheckBox *checkBoxItalic;

    QRadioButton *radioButtonBlack;
    QRadioButton *radioButtonBlue;
    QRadioButton *radioButtonRed;

    QPushButton *buttonCancel;
    QPushButton *buttonQuit;
    QPushButton *buttonSure;

    QPlainTextEdit *textEdit;

    QSpacerItem *spacer1;
    QSpacerItem *spacer2;

    void initUi();
    void iniSignalSlots();

private slots:
    void on_checkBoxUnderLine(bool checked);
    void on_checkBoxBold(bool checked);
    void on_checkBoxItalic(bool checked);

    void setTextFontColor();

};
#endif // DIALOG_H
