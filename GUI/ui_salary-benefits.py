# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'salary-benefitstKnLiN.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QLabel,
    QPlainTextEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(380, 500)
        Dialog.setStyleSheet(u"font: 700 9pt \"Segoe UI\";")
        self.apply = QPushButton(Dialog)
        self.apply.setObjectName(u"apply")
        self.apply.setGeometry(QRect(10, 460, 111, 31))
        self.apply.setStyleSheet(u"\n"
"font: 700 9pt \"Segoe UI\";")
        self.salary_Monthly = QPlainTextEdit(Dialog)
        self.salary_Monthly.setObjectName(u"salary_Monthly")
        self.salary_Monthly.setGeometry(QRect(10, 50, 361, 31))
        self.salary_Monthly.setStyleSheet(u"font: 300 9pt \"Outfit\";")
        self.Monthly = QLabel(Dialog)
        self.Monthly.setObjectName(u"Monthly")
        self.Monthly.setGeometry(QRect(10, 30, 101, 16))
        self.Monthly.setStyleSheet(u"font: 9pt \"Segoe UI\";")
        self.benefits_Edu = QPlainTextEdit(Dialog)
        self.benefits_Edu.setObjectName(u"benefits_Edu")
        self.benefits_Edu.setGeometry(QRect(10, 260, 361, 61))
        self.benefits_Edu.setStyleSheet(u"font: 300 9pt \"Outfit\";")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 240, 121, 16))
        self.label_3.setStyleSheet(u"font: 300 9pt \"Segoe UI\";\n"
"font: 9pt \"Segoe UI\";")
        self.apply_confirm = QCheckBox(Dialog)
        self.apply_confirm.setObjectName(u"apply_confirm")
        self.apply_confirm.setGeometry(QRect(10, 440, 75, 20))
        self.apply_confirm.setStyleSheet(u"font: 600 9pt \"Segoe UI\";")
        self.salary_Overtime = QPlainTextEdit(Dialog)
        self.salary_Overtime.setObjectName(u"salary_Overtime")
        self.salary_Overtime.setGeometry(QRect(10, 110, 361, 31))
        self.salary_Overtime.setStyleSheet(u"font: 300 9pt \"Outfit\";")
        self.salary_Total = QPlainTextEdit(Dialog)
        self.salary_Total.setObjectName(u"salary_Total")
        self.salary_Total.setGeometry(QRect(10, 170, 361, 31))
        self.salary_Total.setStyleSheet(u"font: 300 9pt \"Outfit\";")
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 90, 101, 16))
        self.label_4.setStyleSheet(u"font: 300 9pt \"Segoe UI\";\n"
"font: 9pt \"Segoe UI\";")
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 150, 101, 16))
        self.label_5.setStyleSheet(u"font: 300 9pt \"Segoe UI\";\n"
"font: 9pt \"Segoe UI\";")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 49, 16))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 220, 71, 16))
        self.benefits_Med = QPlainTextEdit(Dialog)
        self.benefits_Med.setObjectName(u"benefits_Med")
        self.benefits_Med.setGeometry(QRect(10, 350, 361, 61))
        self.benefits_Med.setStyleSheet(u"font: 300 9pt \"Outfit\";")
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 330, 121, 16))
        self.label_6.setStyleSheet(u"font: 300 9pt \"Segoe UI\";\n"
"font: 9pt \"Segoe UI\";")
        self.close = QPushButton(Dialog)
        self.close.setObjectName(u"close")
        self.close.setGeometry(QRect(260, 460, 111, 31))
        self.close.setStyleSheet(u"font: 9pt \"Segoe UI\";")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.apply.setText(QCoreApplication.translate("Dialog", u"Apply", None))
        self.salary_Monthly.setPlainText(QCoreApplication.translate("Dialog", u"0.00", None))
        self.Monthly.setText(QCoreApplication.translate("Dialog", u"Monthly salary", None))
        self.benefits_Edu.setPlainText("")
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Education benefits", None))
        self.apply_confirm.setText(QCoreApplication.translate("Dialog", u"Confirm", None))
        self.salary_Overtime.setPlainText(QCoreApplication.translate("Dialog", u"0.00", None))
        self.salary_Total.setPlainText(QCoreApplication.translate("Dialog", u"0.00", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Overtime salary", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Total salary", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"SALARY", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"BENEFITS", None))
        self.benefits_Med.setPlainText("")
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Medical benefits", None))
        self.close.setText(QCoreApplication.translate("Dialog", u"Close", None))
    # retranslateUi

