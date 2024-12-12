# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'editCANLASEKoinm.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QGroupBox, QLabel, QLayout, QMainWindow,
    QPlainTextEdit, QPushButton, QScrollArea, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1234, 715)
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(0, 0, 0, 128))
        brush2.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        MainWindow.setPalette(palette)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color: white;\n"
"color: black;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 100))
        self.groupBox.setStyleSheet(u"background-color: white;\n"
"color: black;")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 20, 251, 26))
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: white;\n"
"color: black;")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(120, 50, 241, 31))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"background-color: white;\n"
"color: black;")
        self.label_12 = QLabel(self.groupBox)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 10, 91, 81))
        self.label_12.setStyleSheet(u"background-color: white;\n"
"color: black;")
        self.label_12.setPixmap(QPixmap(u":/images/logo_silliman.png"))
        self.label_12.setScaledContents(True)

        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setEnabled(True)
        self.scrollArea.setMinimumSize(QSize(0, 0))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.scrollArea.setPalette(palette1)
        self.scrollArea.setAutoFillBackground(True)
        self.scrollArea.setStyleSheet(u"QScrollBar:vertical {\n"
"    border: 0px solid #dcdcdc; /* Border around the scrollbar */\n"
"    background: #f5f5f5;       /* Background of the scrollbar area */\n"
"    width: 12px;               /* Width of the scrollbar */\n"
"    margin: 0px 0px 0px 0px;   /* Margins around the scrollbar */\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #888;          /* Color of the scrollbar handle */\n"
"    min-height: 10px;          /* Minimum height of the scrollbar handle */\n"
"    border-radius: 5px;        /* Rounded corners of the scrollbar handle */\n"
"}\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical {\n"
"    background: #dcdcdc;       /* Background color of arrow buttons */\n"
"    border: 1px solid #aaa;    /* Border around the arrow buttons */\n"
"    height: 12px;              /* Height of arrow buttons */\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top;  /* Positions at top and bottom */\n"
"}\n"
"QScrollArea {\n"
"    background: none; /* Ba"
                        "ckground color for the scroll area */\n"
"    border: 2px solid black; /* Optional border */\n"
"  \n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1200, 2904))
        self.scrollAreaWidgetContents.setStyleSheet(u"background-color: white;\n"
"color: black;")
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"padding-left: 10px;\n"
"")

        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 4)

        self.update_picture_btn = QPushButton(self.scrollAreaWidgetContents)
        self.update_picture_btn.setObjectName(u"update_picture_btn")
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        brush3 = QBrush(QColor(128, 178, 65, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush3)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush3)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush3)
        brush4 = QBrush(QColor(255, 255, 255, 128))
        brush4.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush4)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush4)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.update_picture_btn.setPalette(palette2)
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.update_picture_btn.setFont(font2)
        self.update_picture_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.update_picture_btn.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(128, 178, 65);\n"
"color: rgb(255, 255, 255);\n"
"padding:5px;")

        self.gridLayout_3.addWidget(self.update_picture_btn, 2, 0, 1, 1)

        self.employee_image_name = QLabel(self.scrollAreaWidgetContents)
        self.employee_image_name.setObjectName(u"employee_image_name")

        self.gridLayout_3.addWidget(self.employee_image_name, 1, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 3)

        self.edit_examination_place = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.edit_examination_place.setObjectName(u"edit_examination_place")
        self.edit_examination_place.setMinimumSize(QSize(0, 0))
        self.edit_examination_place.setStyleSheet(u"border:1px solid black;")

        self.gridLayout_2.addWidget(self.edit_examination_place, 62, 3, 1, 1)

        self.edit_spouse = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.edit_spouse.setObjectName(u"edit_spouse")
        self.edit_spouse.setMinimumSize(QSize(0, 0))
        self.edit_spouse.setStyleSheet(u"border:1px solid black;")

        self.gridLayout_2.addWidget(self.edit_spouse, 38, 1, 1, 1)

        self.label_32 = QLabel(self.scrollAreaWidgetContents)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font2)
        self.label_32.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.label_32, 34, 1, 1, 1)

        self.label_22 = QLabel(self.scrollAreaWidgetContents)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font2)
        self.label_22.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.label_22, 21, 0, 1, 1)

        self.label_18 = QLabel(self.scrollAreaWidgetContents)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font2)
        self.label_18.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.label_18, 17, 0, 1, 1)

        self.label_36 = QLabel(self.scrollAreaWidgetContents)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font2)
        self.label_36.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.label_36, 37, 2, 1, 1)

        self.edit_staff_name = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.edit_staff_name.setObjectName(u"edit_staff_name")
        self.edit_staff_name.setMinimumSize(QSize(0, 0))
        self.edit_staff_name.setStyleSheet(u"border:1px solid black;")

        self.gridLayout_2.addWidget(self.edit_staff_name, 50, 0, 1, 1)

        self.label_17 = QLabel(self.scrollAreaWidgetContents)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font2)
        self.label_17.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.label_17, 15, 2, 1, 1)

        self.label_13 = QLabel(self.scrollAreaWidgetContents)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font2)
        self.label_13.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.label_13, 10, 1, 1, 1)

        self.label_10 = QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)
        self.label_10.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.label_10, 10, 0, 1, 1)

        self.label_49 = QLabel(self.scrollAreaWidgetContents)
        self.label_49.setObjectName(u"label_49")
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(False)
        self.label_49.setFont(font3)
        self.label_49.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.label_49, 46, 2, 1, 1)

        self.edit_school_pub = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.edit_school_pub.setObjectName(u"edit_school_pub")
        self.edit_school_pub.setMinimumSize(QSize(0, 0))
        self.edit_school_pub.setStyleSheet(u"border:1px solid black;")

        self.gridLayout_2.addWidget(self.edit_school_pub, 54, 0, 1, 3)

        self.label_63 = QLabel(self.scrollAreaWidgetContents)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setFont(font3)
        self.label_63.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.label_63, 61, 0, 1, 1)

        self.edit_mother_occ = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.edit_mother_occ.setObjectName(u"edit_mother_occ")
        self.edit_mother_occ.setMinimumSize(QSize(0, 0))
        self.edit_mother_occ.setStyleSheet(u"border:1px solid black;")

        self.gridLayout_2.addWidget(self.edit_mother_occ, 31, 2, 1, 1)

        self.label_11 = QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font2)
        self.label_11.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.label_11, 15, 0, 1, 1)

        self.label_31 = QLabel(self.scrollAreaWidgetContents)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font2)
        self.label_31.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.label_31, 34, 0, 1, 1)

        self.edit_children = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.edit_children.setObjectName(u"edit_children")
        self.edit_children.setMinimumSize(QSize(0, 0))
        self.edit_children.setStyleSheet(u"background-color: white;\n"
"color: black;border:1px solid black;")

        self.gridLayout_2.addWidget(self.edit_children, 40, 0, 1, 2)

        self.edit_department = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.edit_department.setObjectName(u"edit_department")
        self.edit_department.setMinimumSize(QSize(0, 0))
        self.edit_department.setStyleSheet(u"background-color: white;\n"
"color: black;border:1px solid black;")

        self.gridLayout_2.addWidget(self.edit_department, 5, 0, 1, 3)

        self.edit_previous_name = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.edit_previous_name.setObjectName(u"edit_previous_name")
        self.edit_previous_name.setMinimumSize(QSize(0, 0))
        self.edit_previous_name.setStyleSheet(u"border:1px solid black;")

        self.gridLayout_2.addWidget(self.edit_previous_name, 57, 0, 1, 1)

        self.label_45 = QLabel(self.scrollAreaWidgetContents)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setFont(font3)
        self.label_45.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.label_45, 44, 1, 1, 1)

        self.edit_elem_date = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.edit_elem_date.setObjectName(u"edit_elem_date")
        self.edit_elem_date.setMinimumSize(QSize(0, 0))
        self.edit_elem_date.setStyleSheet(u"background-color: white;\n"
"color: black;border:1px solid black;")

        self.gridLayout_2.addWidget(self.edit_elem_date, 43, 2, 1, 1)

        self.label_52 = QLabel(self.scrollAreaWidgetContents)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setFont(font3)
        self.label_52.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.label_52, 49, 0, 1, 1)

        self.editRecord_btn = QPushButton(self.scrollAreaWidgetContents)
        self.editRecord_btn.setObjectName(u"editRecord_btn")
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush3)
        palette3.setBrush(QPalette.Active, QPalette.Light, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush3)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush4)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        palette3.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush4)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush3)
        palette3.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush3)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.editRecord_btn.setPalette(palette3)
        font4 = QFont()
        font4.setPointSize(12)
        self.editRecord_btn.setFont(font4)
        self.editRecord_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.editRecord_btn.setMouseTracking(False)
        self.editRecord_btn.setAutoFillBackground(False)
        self.editRecord_btn.setStyleSheet(u"background-color: rgb(128, 178, 65);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px; \n"
"padding-left: 30px;\n"
"padding-right: 30px;\n"
"padding-top: 5px;\n"
"padding-bottom: 5px;")

        self.gridLayout_2.addWidget(self.editRecord_btn, 66, 3, 1, 1)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 3)

        self.label_34 = QLabel(self.scrollAreaWidgetContents)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font2)
        self.label_34.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.label_34, 37, 0, 1, 1)

        self.edit_marriage_place = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.edit_marriage_place.setObjectName(u"edit_marriage_place")
        self.edit_marriage_place.setMinimumSize(QSize(0, 0))
        self.edit_marriage_place.setStyleSheet(u"border:1px solid black;")

        self.gridLayout_2.addWidget(self.edit_marriage_place, 38, 2, 1, 1)

        self.edit_elem_address = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.edit_elem_address.setObjectName(u"edit_elem_address")
        self.edit_elem_address.setMinimumSize(QSize(0, 0))
        self.edit_elem_address.setStyleSheet(u"background-color: white;\n"
"color: black;border:1px solid black;")

        self.gridLayout_2.addWidget(self.edit_elem_address, 43, 1, 1, 1)

        self.label_20 = QLabel(self.scrollAreaWidgetContents)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font2)
        self.label_20.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.label_20, 19, 0, 1, 1)

        self.edit_staff_relation = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.edit_staff_relation.setObjectName(u"edit_staff_relation")
        self.edit_staff_relation.setMinimumSize(QSize(0, 0))
        self.edit_staff_relation.setStyleSheet(u"border:1px solid black;")

        self.gridLayout_2.addWidget(self.edit_staff_relation, 50, 1, 1, 1)

        self.edit_siblings_occ = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.edit_siblings_occ.setObjectName(u"edit_siblings_occ")
        self.edit_siblings_occ.setMinimumSize(QSize(0, 0))
        self.edit_siblings_occ.setStyleSheet(u"border:1px solid black;")

        self.gridLayout_2.addWidget(self.edit_siblings_occ, 35, 1, 1, 1)

        self.label_67 = QLabel(self.scrollAreaWidgetContents)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setFont(font2)
        self.label_67.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.label_67, 64, 0, 1, 3)

        self.edit_staff_pos = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.edit_staff_pos.setObjectName(u"edit_staff_pos")
        self.edit_staff_pos.setMinimumSize(QSize(0, 0))
        self.edit_staff_pos.setStyleSheet(u"border:1px solid black;")

        self.gridLayout_2.addWidget(self.edit_staff_pos, 50, 2, 1, 1)

        self.label_42 = QLabel(self.scrollAreaWidgetContents)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setFont(font3)
        self.label_42.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.label_42, 42, 1, 1, 1)

        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 20))
        self.frame.setStyleSheet(u"background-color: white;\n"
"color: black;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.gridLayout_2.addWidget(self.frame, 12, 0, 1, 3)

        self.label_66 = QLabel(self.scrollAreaWidgetContents)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setFont(font3)
        self.label_66.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.label_66, 61, 3, 1, 1)

        self.edit_college = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.edit_college.setObjectName(u"edit_college")
        self.edit_college.setMinimumSize(QSize(0, 0))
        self.edit_college.setStyleSheet(u"background-color: white;\n"
"color: black;border:1px solid black;")

        self.gridLayout_2.addWidget(self.edit_college, 47, 0, 1, 1)

        self.edit_father_address = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.edit_father_address.setObjectName(u"edit_father_address")
        self.edit_father_address.setMinimumSize(QSize(0, 0))
        self.edit_father_address.setStyleSheet(u"border:1px solid black;")

        self.gridLayout_2.addWidget(self.edit_father_address, 33, 0, 1, 3)

        self.label_26 = QLabel(self.scrollAreaWidgetContents)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font2)
        self.label_26.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.label_26, 25, 2, 1, 1)

        self.label_25 = QLabel(self.scrollAreaWidgetContents)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font2)
        self.label_25.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.label_25, 25, 0, 1, 1)

        self.edit_father_occ = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.edit_father_occ.setObjectName(u"edit_father_occ")
        self.edit_father_occ.setMinimumSize(QSize(0, 0))
        self.edit_father_occ.setStyleSheet(u"border:1px solid black;")

        self.gridLayout_2.addWidget(self.edit_father_occ, 26, 2, 1, 1)

        self.edit_SSS = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.edit_SSS.setObjectName(u"edit_SSS")
        self.edit_SSS.setMinimumSize(QSize(0, 0))
        self.edit_SSS.setStyleSheet(u"background-color: white;\n"
"color: black;border:1px solid black;")

        self.gridLayout_2.addWidget(self.edit_SSS, 20, 1, 1, 2)

        self.edit_TIN = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.edit_TIN.setObjectName(u"edit_TIN")
        self.edit_TIN.setMinimumSize(QSize(0, 0))
        self.edit_TIN.setStyleSheet(u"background-color: white;\n"
"color: black;border:1px solid black;")

        self.gridLayout_2.addWidget(self.edit_TIN, 20, 0, 1, 1)

        self.label_14 = QLabel(self.scrollAreaWidgetContents)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font2)
        self.label_14.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.label_14, 10, 2, 1, 1)

        self.edit_pagibig = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.edit_pagibig.setObjectName(u"edit_pagibig")
        self.edit_pagibig.setMinimumSize(QSize(0, 0))
        self.edit_pagibig.setStyleSheet(u"border:1px solid black;")

        self.gridLayout_2.addWidget(self.edit_pagibig, 22, 0, 1, 1)

        self.edit_elem = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.edit_elem.setObjectName(u"edit_elem")
        self.edit_elem.setMinimumSize(QSize(0, 0))
        self.edit_elem.setStyleSheet(u"background-color: white;\n"
"color: black;border:1px solid black;")

        self.gridLayout_2.addWidget(self.edit_elem, 43, 0, 1, 1)

        self.edit_acrNo = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.edit_acrNo.setObjectName(u"edit_acrNo")
        self.edit_acrNo.setStyleSheet(u"background-color: white;\n"
"color: black;border:1px solid black;")

        self.gridLayout_2.addWidget(self.edit_acrNo, 16, 1, 1, 1)

        self.edit_middleName = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.edit_middleName.setObjectName(u"edit_middleName")
        self.edit_middleName.setMinimumSize(QSize(0, 0))
        self.edit_middleName.setStyleSheet(u"border:1px solid black;")

        self.gridLayout_2.addWidget(self.edit_middleName, 1, 1, 1, 1)

        self.label_35 = QLabel(self.scrollAreaWidgetContents)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font2)
        self.label_35.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.label_35, 37, 1, 1, 1)

        self.edit_date_issued = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.edit_date_issued.setObjectName(u"edit_date_issued")
        self.edit_date_issued.setStyleSheet(u"background-color: white;\n"
"color: black;border:1px solid black;")

        self.gridLayout_2.addWidget(self.edit_date_issued, 16, 2, 1, 1)

        self.label_59 = QLabel(self.scrollAreaWidgetContents)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setFont(font3)
        self.label_59.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.label_59, 56, 2, 1, 1)

        self.edit_Position = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.edit_Position.setObjectName(u"edit_Position")
        self.edit_Position.setMinimumSize(QSize(0, 0))
        self.edit_Position.setStyleSheet(u"background-color: white;\n"
"color: black;border:1px solid black;")

        self.gridLayout_2.addWidget(self.edit_Position, 3, 0, 1, 3)

        self.edit_school_dist = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.edit_school_dist.setObjectName(u"edit_school_dist")
        self.edit_school_dist.setMinimumSize(QSize(0, 0))
        self.edit_school_dist.setStyleSheet(u"border:1px solid black;")

        self.gridLayout_2.addWidget(self.edit_school_dist, 52, 0, 1, 3)

        self.edit_citizen = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.edit_citizen.setObjectName(u"edit_citizen")
        self.edit_citizen.setMinimumSize(QSize(0, 0))
        self.edit_citizen.setStyleSheet(u"background-color: white;\n"
"color: black;border:1px solid black;")

        self.gridLayout_2.addWidget(self.edit_citizen, 11, 2, 1, 1)

        self.checkBox_4 = QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.checkBox_4, 55, 3, 1, 1)

        self.label_64 = QLabel(self.scrollAreaWidgetContents)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setFont(font3)
        self.label_64.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.label_64, 61, 1, 1, 1)

        self.label_9 = QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)
        self.label_9.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.label_9, 8, 0, 1, 3)

        self.edit_case = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.edit_case.setObjectName(u"edit_case")
        self.edit_case.setMinimumSize(QSize(0, 0))
        self.edit_case.setStyleSheet(u"background-color: white;\n"
"color: black;border:1px solid black;")

        self.gridLayout_2.addWidget(self.edit_case, 65, 0, 1, 4)

        self.edit_mother_name = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.edit_mother_name.setObjectName(u"edit_mother_name")
        self.edit_mother_name.setMinimumSize(QSize(0, 0))
        self.edit_mother_name.setStyleSheet(u"border:1px solid black;")

        self.gridLayout_2.addWidget(self.edit_mother_name, 31, 0, 1, 2)

        self.edit_college_date = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.edit_college_date.setObjectName(u"edit_college_date")
        self.edit_college_date.setMinimumSize(QSize(0, 0))
        self.edit_college_date.setStyleSheet(u"background-color: white;\n"
"color: black;border:1px solid black;")

        self.gridLayout_2.addWidget(self.edit_college_date, 47, 2, 1, 1)

        self.edit_email_add = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.edit_email_add.setObjectName(u"edit_email_add")
        self.edit_email_add.setMinimumSize(QSize(0, 0))
        self.edit_email_add.setStyleSheet(u"background-color: white;\n"
"color: black;border:1px solid black;")

        self.gridLayout_2.addWidget(self.edit_email_add, 18, 1, 1, 2)

        self.edit_lastName = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.edit_lastName.setObjectName(u"edit_lastName")
        self.edit_lastName.setMinimumSize(QSize(0, 0))
        self.edit_lastName.setStyleSheet(u"border:1px solid black;")

        self.gridLayout_2.addWidget(self.edit_lastName, 1, 2, 1, 1)

        self.edit_high_address = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.edit_high_address.setObjectName(u"edit_high_address")
        self.edit_high_address.setMinimumSize(QSize(0, 0))
        self.edit_high_address.setStyleSheet(u"border:1px solid black;")

        self.gridLayout_2.addWidget(self.edit_high_address, 45, 1, 1, 1)

        self.edit_PoB = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.edit_PoB.setObjectName(u"edit_PoB")
        self.edit_PoB.setMinimumSize(QSize(0, 0))
        self.edit_PoB.setStyleSheet(u"background-color: white;\n"
"color: black;border:1px solid black;")

        self.gridLayout_2.addWidget(self.edit_PoB, 11, 1, 1, 1)

        self.label_33 = QLabel(self.scrollAreaWidgetContents)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font2)
        self.label_33.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.label_33, 34, 2, 1, 1)

        self.label_47 = QLabel(self.scrollAreaWidgetContents)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setFont(font3)
        self.label_47.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.label_47, 46, 0, 1, 1)

        self.edit_workplace_address = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.edit_workplace_address.setObjectName(u"edit_workplace_address")
        self.edit_workplace_address.setMinimumSize(QSize(0, 0))
        self.edit_workplace_address.setStyleSheet(u"border:1px solid black;")

        self.gridLayout_2.addWidget(self.edit_workplace_address, 59, 0, 1, 4)

        self.edit_children_DoB = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.edit_children_DoB.setObjectName(u"edit_children_DoB")
        self.edit_children_DoB.setMinimumSize(QSize(0, 0))
        self.edit_children_DoB.setStyleSheet(u"background-color: white;\n"
"color: black;border:1px solid black;")

        self.gridLayout_2.addWidget(self.edit_children_DoB, 40, 2, 1, 1)

        self.label_51 = QLabel(self.scrollAreaWidgetContents)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setFont(font3)
        self.label_51.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.label_51, 49, 1, 1, 1)

        self.label_8 = QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)
        self.label_8.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.label_8, 6, 0, 1, 3)

        self.checkBox_6 = QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.checkBox_6, 64, 3, 1, 1)

        self.edit_philhealth = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.edit_philhealth.setObjectName(u"edit_philhealth")
        self.edit_philhealth.setMinimumSize(QSize(0, 0))
        self.edit_philhealth.setStyleSheet(u"border:1px solid black;")

        self.gridLayout_2.addWidget(self.edit_philhealth, 22, 1, 1, 2)

        self.edit_examination = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.edit_examination.setObjectName(u"edit_examination")
        self.edit_examination.setMinimumSize(QSize(0, 0))
        self.edit_examination.setStyleSheet(u"background-color: white;\n"
"color: black;border:1px solid black;")

        self.gridLayout_2.addWidget(self.edit_examination, 62, 0, 1, 1)

        self.label_60 = QLabel(self.scrollAreaWidgetContents)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setFont(font3)
        self.label_60.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.label_60, 56, 3, 1, 1)

        self.edit_marriage_date = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.edit_marriage_date.setObjectName(u"edit_marriage_date")
        self.edit_marriage_date.setStyleSheet(u"border:1px solid black;")

        self.gridLayout_2.addWidget(self.edit_marriage_date, 38, 3, 1, 1)

        self.label_62 = QLabel(self.scrollAreaWidgetContents)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setFont(font3)
        self.label_62.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.label_62, 58, 0, 1, 4)

        self.label_27 = QLabel(self.scrollAreaWidgetContents)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font2)
        self.label_27.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.label_27, 27, 0, 1, 1)

        self.label_30 = QLabel(self.scrollAreaWidgetContents)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font2)
        self.label_30.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.label_30, 32, 0, 1, 1)

        self.label_38 = QLabel(self.scrollAreaWidgetContents)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font2)
        self.label_38.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.label_38, 39, 0, 1, 1)

        self.edit_previous_position = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.edit_previous_position.setObjectName(u"edit_previous_position")
        self.edit_previous_position.setMinimumSize(QSize(0, 0))
        self.edit_previous_position.setStyleSheet(u"border:1px solid black;")

        self.gridLayout_2.addWidget(self.edit_previous_position, 57, 1, 1, 1)

        self.label_40 = QLabel(self.scrollAreaWidgetContents)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font2)
        self.label_40.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.label_40, 41, 0, 1, 1)

        self.label_28 = QLabel(self.scrollAreaWidgetContents)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font2)
        self.label_28.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.label_28, 30, 0, 1, 2)

        self.edit_DoB = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.edit_DoB.setObjectName(u"edit_DoB")
        self.edit_DoB.setMinimumSize(QSize(0, 0))
        self.edit_DoB.setStyleSheet(u"background-color: white;\n"
"color: black;border:1px solid black;")

        self.gridLayout_2.addWidget(self.edit_DoB, 11, 0, 1, 1)

        self.edit_rating = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.edit_rating.setObjectName(u"edit_rating")
        self.edit_rating.setMinimumSize(QSize(0, 0))
        self.edit_rating.setStyleSheet(u"border:1px solid black;")

        self.gridLayout_2.addWidget(self.edit_rating, 62, 1, 1, 1)

        self.label_37 = QLabel(self.scrollAreaWidgetContents)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font2)
        self.label_37.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.label_37, 37, 3, 1, 1)

        self.edit_civil = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.edit_civil.setObjectName(u"edit_civil")
        self.edit_civil.setMinimumSize(QSize(0, 0))
        self.edit_civil.setStyleSheet(u"background-color: white;\n"
"color: black;border:1px solid black;")

        self.gridLayout_2.addWidget(self.edit_civil, 38, 0, 1, 1)

        self.checkBox = QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.checkBox, 23, 2, 1, 1)

        self.label_61 = QLabel(self.scrollAreaWidgetContents)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setFont(font2)
        self.label_61.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.label_61, 60, 0, 1, 3)

        self.edit_examination_date = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.edit_examination_date.setObjectName(u"edit_examination_date")
        self.edit_examination_date.setMinimumSize(QSize(0, 0))
        self.edit_examination_date.setStyleSheet(u"border:1px solid black;")

        self.gridLayout_2.addWidget(self.edit_examination_date, 62, 2, 1, 1)

        self.label_19 = QLabel(self.scrollAreaWidgetContents)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font2)
        self.label_19.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.label_19, 17, 1, 1, 2)

        self.label_58 = QLabel(self.scrollAreaWidgetContents)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setFont(font3)
        self.label_58.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.label_58, 56, 1, 1, 1)

        self.edit_father_name = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.edit_father_name.setObjectName(u"edit_father_name")
        self.edit_father_name.setMinimumSize(QSize(0, 0))
        self.edit_father_name.setStyleSheet(u"border:1px solid black;")

        self.gridLayout_2.addWidget(self.edit_father_name, 26, 0, 1, 2)

        self.label_65 = QLabel(self.scrollAreaWidgetContents)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setFont(font3)
        self.label_65.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.label_65, 61, 2, 1, 1)

        self.label_43 = QLabel(self.scrollAreaWidgetContents)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setFont(font3)
        self.label_43.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.label_43, 42, 2, 1, 1)

        self.edit_siblings_name = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.edit_siblings_name.setObjectName(u"edit_siblings_name")
        self.edit_siblings_name.setMinimumSize(QSize(0, 0))
        self.edit_siblings_name.setStyleSheet(u"border:1px solid black;")

        self.gridLayout_2.addWidget(self.edit_siblings_name, 35, 0, 1, 1)

        self.label_56 = QLabel(self.scrollAreaWidgetContents)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setFont(font2)
        self.label_56.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.label_56, 55, 0, 1, 3)

        self.edit_previous_period = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.edit_previous_period.setObjectName(u"edit_previous_period")
        self.edit_previous_period.setMinimumSize(QSize(0, 0))
        self.edit_previous_period.setStyleSheet(u"border:1px solid black;")

        self.gridLayout_2.addWidget(self.edit_previous_period, 57, 2, 1, 1)

        self.label_21 = QLabel(self.scrollAreaWidgetContents)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font2)
        self.label_21.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.label_21, 19, 1, 1, 2)

        self.edit_firstName = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.edit_firstName.setObjectName(u"edit_firstName")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit_firstName.sizePolicy().hasHeightForWidth())
        self.edit_firstName.setSizePolicy(sizePolicy)
        self.edit_firstName.setMinimumSize(QSize(0, 0))
        self.edit_firstName.setStyleSheet(u"border:1px solid black;")

        self.gridLayout_2.addWidget(self.edit_firstName, 1, 0, 1, 1)

        self.label_55 = QLabel(self.scrollAreaWidgetContents)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setFont(font2)
        self.label_55.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.label_55, 53, 0, 1, 3)

        self.label_29 = QLabel(self.scrollAreaWidgetContents)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font2)
        self.label_29.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.label_29, 30, 2, 1, 1)

        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.label_7, 4, 0, 1, 3)

        self.label_53 = QLabel(self.scrollAreaWidgetContents)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setFont(font3)
        self.label_53.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.label_53, 49, 2, 1, 1)

        self.edit_college_address = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.edit_college_address.setObjectName(u"edit_college_address")
        self.edit_college_address.setMinimumSize(QSize(0, 0))
        self.edit_college_address.setStyleSheet(u"background-color: white;\n"
"color: black;border:1px solid black;")

        self.gridLayout_2.addWidget(self.edit_college_address, 47, 1, 1, 1)

        self.label_16 = QLabel(self.scrollAreaWidgetContents)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font2)
        self.label_16.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.label_16, 15, 1, 1, 1)

        self.label_48 = QLabel(self.scrollAreaWidgetContents)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setFont(font3)
        self.label_48.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.label_48, 46, 1, 1, 1)

        self.checkBox_3 = QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.checkBox_3, 39, 3, 1, 1)

        self.edit_home_address = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.edit_home_address.setObjectName(u"edit_home_address")
        self.edit_home_address.setMinimumSize(QSize(0, 0))
        self.edit_home_address.setStyleSheet(u"border:1px solid black;")

        self.gridLayout_2.addWidget(self.edit_home_address, 9, 0, 1, 3)

        self.edit_passportNo = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.edit_passportNo.setObjectName(u"edit_passportNo")
        self.edit_passportNo.setMinimumSize(QSize(0, 0))
        self.edit_passportNo.setStyleSheet(u"border:1px solid black;")

        self.gridLayout_2.addWidget(self.edit_passportNo, 16, 0, 1, 1)

        self.label_57 = QLabel(self.scrollAreaWidgetContents)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setFont(font3)
        self.label_57.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.label_57, 56, 0, 1, 1)

        self.edit_high = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.edit_high.setObjectName(u"edit_high")
        self.edit_high.setMinimumSize(QSize(0, 0))
        self.edit_high.setStyleSheet(u"border:1px solid black;")

        self.gridLayout_2.addWidget(self.edit_high, 45, 0, 1, 1)

        self.edit_previous_leaving = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.edit_previous_leaving.setObjectName(u"edit_previous_leaving")
        self.edit_previous_leaving.setMinimumSize(QSize(0, 0))
        self.edit_previous_leaving.setStyleSheet(u"border:1px solid black;")

        self.gridLayout_2.addWidget(self.edit_previous_leaving, 57, 3, 1, 1)

        self.edit_contactNo = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.edit_contactNo.setObjectName(u"edit_contactNo")
        self.edit_contactNo.setMinimumSize(QSize(0, 0))
        self.edit_contactNo.setStyleSheet(u"background-color: white;\n"
"color: black;border:1px solid black;")

        self.gridLayout_2.addWidget(self.edit_contactNo, 18, 0, 1, 1)

        self.edit_church = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.edit_church.setObjectName(u"edit_church")
        self.edit_church.setMinimumSize(QSize(0, 0))
        self.edit_church.setStyleSheet(u"background-color: white;\n"
"color: black;border:1px solid black;")

        self.gridLayout_2.addWidget(self.edit_church, 24, 0, 1, 3)

        self.checkBox_2 = QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.checkBox_2, 13, 2, 1, 1)

        self.label_23 = QLabel(self.scrollAreaWidgetContents)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font2)
        self.label_23.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.label_23, 21, 1, 1, 2)

        self.edit_high_date = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.edit_high_date.setObjectName(u"edit_high_date")
        self.edit_high_date.setMinimumSize(QSize(0, 0))
        self.edit_high_date.setStyleSheet(u"border:1px solid black;")

        self.gridLayout_2.addWidget(self.edit_high_date, 45, 2, 1, 1)

        self.label_24 = QLabel(self.scrollAreaWidgetContents)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font2)
        self.label_24.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.label_24, 23, 0, 1, 2)

        self.label_46 = QLabel(self.scrollAreaWidgetContents)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setFont(font3)
        self.label_46.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.label_46, 44, 2, 1, 1)

        self.edit_dgte_address = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.edit_dgte_address.setObjectName(u"edit_dgte_address")
        self.edit_dgte_address.setMinimumSize(QSize(0, 0))
        self.edit_dgte_address.setStyleSheet(u"background-color: white;\n"
"color: black;border:1px solid black;")

        self.gridLayout_2.addWidget(self.edit_dgte_address, 7, 0, 1, 3)

        self.label_39 = QLabel(self.scrollAreaWidgetContents)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font2)
        self.label_39.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.label_39, 39, 2, 1, 1)

        self.label_44 = QLabel(self.scrollAreaWidgetContents)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setFont(font3)
        self.label_44.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.label_44, 44, 0, 1, 1)

        self.label_54 = QLabel(self.scrollAreaWidgetContents)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setFont(font2)
        self.label_54.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.label_54, 51, 0, 1, 3)

        self.edit_siblings_address = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.edit_siblings_address.setObjectName(u"edit_siblings_address")
        self.edit_siblings_address.setMinimumSize(QSize(0, 0))
        self.edit_siblings_address.setStyleSheet(u"border:1px solid black;")

        self.gridLayout_2.addWidget(self.edit_siblings_address, 35, 2, 1, 1)

        self.label_41 = QLabel(self.scrollAreaWidgetContents)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setFont(font3)
        self.label_41.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.label_41, 42, 0, 1, 1)

        self.checkBox_5 = QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.checkBox_5, 60, 3, 1, 1)

        self.label_15 = QLabel(self.scrollAreaWidgetContents)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font3)
        self.label_15.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.label_15, 13, 0, 1, 2)

        self.label_50 = QLabel(self.scrollAreaWidgetContents)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setFont(font2)
        self.label_50.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.label_50, 48, 0, 1, 1)

        self.edit_father_home = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.edit_father_home.setObjectName(u"edit_father_home")
        self.edit_father_home.setMinimumSize(QSize(0, 0))
        self.edit_father_home.setStyleSheet(u"border:1px solid black;")

        self.gridLayout_2.addWidget(self.edit_father_home, 29, 0, 1, 3)

        self.checkBox_8 = QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_8.setObjectName(u"checkBox_8")
        self.checkBox_8.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.gridLayout_2.addWidget(self.checkBox_8, 66, 2, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 7, 3, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_3)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.edit_footer = QGroupBox(self.scrollAreaWidgetContents)
        self.edit_footer.setObjectName(u"edit_footer")
        self.edit_footer.setMinimumSize(QSize(0, 100))
        self.edit_footer.setStyleSheet(u"background-color: white;\n"
"color: black;")
        self.label_68 = QLabel(self.edit_footer)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setGeometry(QRect(760, 40, 411, 26))
        self.label_68.setFont(font)
        self.label_68.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.verticalLayout_2.addWidget(self.edit_footer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Silliman University", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Personal Record Dashboard", None))
        self.label_12.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Editing Employee Information", None))
        self.update_picture_btn.setText(QCoreApplication.translate("MainWindow", u"Update Employee Picture", None))
        self.employee_image_name.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Position(s)", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Occupation", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Pag-Ibig Number", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Contact number", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Place of marriage", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Date issued*", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Place of Birth", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Date of Birth", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Year Graduated", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Examination", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Passport number*", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Sibling(s)", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.editRecord_btn.setText(QCoreApplication.translate("MainWindow", u"Edit Record", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Full Name", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Civil Status", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Tax Identification Number", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Involvement in criminal/civil case*", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"Place", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Father's occupation", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Father", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Citizenship", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Name of spouse", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Period of employment", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"Employee has no record of prior employment", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Rating", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Home Address", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"College", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Relationship", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Dumaguete Address", None))
        self.checkBox_6.setText(QCoreApplication.translate("MainWindow", u"Does not apply", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Reason for leaving", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Address of workplace", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Home Address", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Home Address", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Children (if any)", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Academic record", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Mother", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Date of marriage", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Employee has no church affiliation", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Government examination(s) passed", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Email address", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Position", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Date of examination", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Year Graduated", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Record of previous employment", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"SSS Number", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Publication(s)", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Mother's occupation", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Department(s)", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Position", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"ACR number*", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Employee has no children.", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Ignore fields*", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Philhealth Number", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Church Affiliation", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Year Graduated", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Date of birth", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"High School", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"School or college distinction(s)", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Elementary School", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"Does not apply", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"If non-Filipino*, please indicate the following:", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Related staff member(s)", None))
        self.checkBox_8.setText(QCoreApplication.translate("MainWindow", u"This confirms all details listed are true.", None))
        self.edit_footer.setTitle("")
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Silliman University Personnel Record Dashboard", None))
    # retranslateUi

