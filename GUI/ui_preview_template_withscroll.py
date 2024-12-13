# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'preview_template_withscrollCANLASmtngHJ.ui'
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
from PySide6.QtWidgets import (QApplication, QGraphicsView, QGridLayout, QGroupBox,
    QLabel, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QStatusBar, QTextEdit, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1422, 863)
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
        MainWindow.setStyleSheet(u"color: black;\n"
"background-color: white;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: white;\n"
"color: black;")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(0, 150))
        self.groupBox_2.setStyleSheet(u"border: none;\n"
"background-color: white;\n"
"color: black;")
        self.layoutWidget = QWidget(self.groupBox_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(160, 50, 258, 43))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"background-color: white;\n"
"color: black;")
        self.label_3.setPixmap(QPixmap(u":/images/title2_header1.png"))
        self.label_3.setScaledContents(False)

        self.verticalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"background-color: white;\n"
"color: black;")
        self.label_4.setPixmap(QPixmap(u":/images/title2_header2.png"))

        self.verticalLayout.addWidget(self.label_4)

        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 121, 111))
        self.label.setStyleSheet(u"background-color: white;\n"
"color: black;")
        self.label.setPixmap(QPixmap(u":/images/logo_silliman.png"))
        self.label.setScaledContents(True)

        self.gridLayout_2.addWidget(self.groupBox_2, 0, 0, 1, 1)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
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
"QScrollArea{\n"
"	background-color: white;\n"
""
                        "	color: black;\n"
"}\n"
"\n"
"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -73, 1390, 739))
        self.scrollAreaWidgetContents.setStyleSheet(u"background-color: rgb(241, 241, 241);\n"
"color: black;")
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.civ_status_header = QLabel(self.scrollAreaWidgetContents)
        self.civ_status_header.setObjectName(u"civ_status_header")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.civ_status_header.setFont(font)

        self.gridLayout.addWidget(self.civ_status_header, 14, 0, 1, 1)

        self.acad_record_header = QLabel(self.scrollAreaWidgetContents)
        self.acad_record_header.setObjectName(u"acad_record_header")
        self.acad_record_header.setFont(font)

        self.gridLayout.addWidget(self.acad_record_header, 9, 2, 1, 1)

        self.employee_home_address = QTextEdit(self.scrollAreaWidgetContents)
        self.employee_home_address.setObjectName(u"employee_home_address")
        self.employee_home_address.setMaximumSize(QSize(500, 16777215))
        self.employee_home_address.setStyleSheet(u"border: 1px solid black")

        self.gridLayout.addWidget(self.employee_home_address, 8, 0, 1, 1)

        self.employee_acad_record = QTextEdit(self.scrollAreaWidgetContents)
        self.employee_acad_record.setObjectName(u"employee_acad_record")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.employee_acad_record.sizePolicy().hasHeightForWidth())
        self.employee_acad_record.setSizePolicy(sizePolicy)
        self.employee_acad_record.setMaximumSize(QSize(500, 16777215))
        self.employee_acad_record.setStyleSheet(u"border: 1px solid black")

        self.gridLayout.addWidget(self.employee_acad_record, 10, 2, 1, 1)

        self.spouse_header = QLabel(self.scrollAreaWidgetContents)
        self.spouse_header.setObjectName(u"spouse_header")
        self.spouse_header.setFont(font)

        self.gridLayout.addWidget(self.spouse_header, 16, 0, 1, 1)

        self.employee_address_header = QLabel(self.scrollAreaWidgetContents)
        self.employee_address_header.setObjectName(u"employee_address_header")
        self.employee_address_header.setFont(font)

        self.gridLayout.addWidget(self.employee_address_header, 7, 0, 1, 1)

        self.employee_civil_status = QLabel(self.scrollAreaWidgetContents)
        self.employee_civil_status.setObjectName(u"employee_civil_status")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        self.employee_civil_status.setFont(font1)
        self.employee_civil_status.setStyleSheet(u"border: 1px solid black;")

        self.gridLayout.addWidget(self.employee_civil_status, 15, 0, 1, 1)

        self.employee_father = QLabel(self.scrollAreaWidgetContents)
        self.employee_father.setObjectName(u"employee_father")
        self.employee_father.setFont(font1)
        self.employee_father.setStyleSheet(u"border: 1px solid black;")

        self.gridLayout.addWidget(self.employee_father, 6, 1, 1, 1)

        self.publications_header = QLabel(self.scrollAreaWidgetContents)
        self.publications_header.setObjectName(u"publications_header")
        self.publications_header.setFont(font)

        self.gridLayout.addWidget(self.publications_header, 7, 2, 1, 1)

        self.employee_brother = QTextEdit(self.scrollAreaWidgetContents)
        self.employee_brother.setObjectName(u"employee_brother")
        sizePolicy.setHeightForWidth(self.employee_brother.sizePolicy().hasHeightForWidth())
        self.employee_brother.setSizePolicy(sizePolicy)
        self.employee_brother.setMaximumSize(QSize(500, 16777215))
        self.employee_brother.setStyleSheet(u"border: 1px solid black")

        self.gridLayout.addWidget(self.employee_brother, 10, 1, 1, 1)

        self.sss_header = QLabel(self.scrollAreaWidgetContents)
        self.sss_header.setObjectName(u"sss_header")
        self.sss_header.setFont(font)

        self.gridLayout.addWidget(self.sss_header, 11, 1, 1, 1)

        self.employee_mother = QLabel(self.scrollAreaWidgetContents)
        self.employee_mother.setObjectName(u"employee_mother")
        self.employee_mother.setFont(font1)
        self.employee_mother.setStyleSheet(u"border: 1px solid black;")

        self.gridLayout.addWidget(self.employee_mother, 8, 1, 1, 1)

        self.employee_publications = QTextEdit(self.scrollAreaWidgetContents)
        self.employee_publications.setObjectName(u"employee_publications")
        sizePolicy.setHeightForWidth(self.employee_publications.sizePolicy().hasHeightForWidth())
        self.employee_publications.setSizePolicy(sizePolicy)
        self.employee_publications.setMaximumSize(QSize(500, 16777215))
        self.employee_publications.setStyleSheet(u"border: 1px solid black")

        self.gridLayout.addWidget(self.employee_publications, 8, 2, 1, 1)

        self.employee_duma_address_header = QLabel(self.scrollAreaWidgetContents)
        self.employee_duma_address_header.setObjectName(u"employee_duma_address_header")
        self.employee_duma_address_header.setFont(font)

        self.gridLayout.addWidget(self.employee_duma_address_header, 5, 0, 1, 1)

        self.brother_header = QLabel(self.scrollAreaWidgetContents)
        self.brother_header.setObjectName(u"brother_header")
        self.brother_header.setFont(font)

        self.gridLayout.addWidget(self.brother_header, 9, 1, 1, 1)

        self.employee_philHealth = QLabel(self.scrollAreaWidgetContents)
        self.employee_philHealth.setObjectName(u"employee_philHealth")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.employee_philHealth.sizePolicy().hasHeightForWidth())
        self.employee_philHealth.setSizePolicy(sizePolicy1)
        self.employee_philHealth.setFont(font1)
        self.employee_philHealth.setStyleSheet(u"border: 1px solid black;")

        self.gridLayout.addWidget(self.employee_philHealth, 17, 1, 1, 1)

        self.groupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy2)
        self.groupBox.setMinimumSize(QSize(1000, 200))
        self.groupBox.setStyleSheet(u"border: 0px;")
        self.edit_info_button = QPushButton(self.groupBox)
        self.edit_info_button.setObjectName(u"edit_info_button")
        self.edit_info_button.setGeometry(QRect(10, 150, 131, 30))
        self.edit_info_button.setMinimumSize(QSize(0, 10))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.edit_info_button.setFont(font2)
        self.edit_info_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.edit_info_button.setStyleSheet(u"border-radius: 5px;\n"
"\n"
"background-color: rgb(50, 50, 50);\n"
"color: white;\n"
"font-weight: bold;\n"
"")
        self.archive_button = QPushButton(self.groupBox)
        self.archive_button.setObjectName(u"archive_button")
        self.archive_button.setGeometry(QRect(150, 150, 101, 30))
        self.archive_button.setMinimumSize(QSize(0, 30))
        self.archive_button.setFont(font2)
        self.archive_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.archive_button.setStyleSheet(u"border-radius: 5px;\n"
"\n"
"background-color: rgb(138, 138, 138);\n"
"color: white;\n"
"font-weight: bold;\n"
"")
        self.archive_button_2 = QPushButton(self.groupBox)
        self.archive_button_2.setObjectName(u"archive_button_2")
        self.archive_button_2.setGeometry(QRect(270, 150, 101, 30))
        self.archive_button_2.setMinimumSize(QSize(0, 30))
        self.archive_button_2.setFont(font2)
        self.archive_button_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.archive_button_2.setStyleSheet(u"border-radius: 5px;\n"
"\n"
"background-color: rgb(68, 255, 0);\n"
"color: black;\n"
"font-weight: bold;\n"
"")
        self.employee_name = QLabel(self.groupBox)
        self.employee_name.setObjectName(u"employee_name")
        self.employee_name.setGeometry(QRect(10, 10, 800, 36))
        font3 = QFont()
        font3.setPointSize(20)
        font3.setBold(True)
        self.employee_name.setFont(font3)
        self.employee_position = QLabel(self.groupBox)
        self.employee_position.setObjectName(u"employee_position")
        self.employee_position.setGeometry(QRect(10, 50, 501, 28))
        font4 = QFont()
        font4.setPointSize(16)
        font4.setBold(True)
        self.employee_position.setFont(font4)
        self.employee_department = QLabel(self.groupBox)
        self.employee_department.setObjectName(u"employee_department")
        self.employee_department.setGeometry(QRect(10, 80, 741, 28))
        font5 = QFont()
        font5.setPointSize(16)
        font5.setBold(False)
        self.employee_department.setFont(font5)
        self.employee_hired_date = QLabel(self.groupBox)
        self.employee_hired_date.setObjectName(u"employee_hired_date")
        self.employee_hired_date.setGeometry(QRect(10, 110, 571, 26))
        font6 = QFont()
        font6.setPointSize(14)
        font6.setBold(False)
        self.employee_hired_date.setFont(font6)

        self.gridLayout.addWidget(self.groupBox, 1, 1, 1, 2)

        self.pagibig_header = QLabel(self.scrollAreaWidgetContents)
        self.pagibig_header.setObjectName(u"pagibig_header")
        self.pagibig_header.setFont(font)

        self.gridLayout.addWidget(self.pagibig_header, 14, 1, 1, 1)

        self.Profile_pic_2 = QGraphicsView(self.scrollAreaWidgetContents)
        self.Profile_pic_2.setObjectName(u"Profile_pic_2")
        sizePolicy2.setHeightForWidth(self.Profile_pic_2.sizePolicy().hasHeightForWidth())
        self.Profile_pic_2.setSizePolicy(sizePolicy2)
        self.Profile_pic_2.setStyleSheet(u"border: 1px solid black")

        self.gridLayout.addWidget(self.Profile_pic_2, 1, 0, 1, 1)

        self.mother_header = QLabel(self.scrollAreaWidgetContents)
        self.mother_header.setObjectName(u"mother_header")
        self.mother_header.setFont(font)

        self.gridLayout.addWidget(self.mother_header, 7, 1, 1, 1)

        self.ph_header = QLabel(self.scrollAreaWidgetContents)
        self.ph_header.setObjectName(u"ph_header")
        self.ph_header.setFont(font)

        self.gridLayout.addWidget(self.ph_header, 16, 1, 1, 1)

        self.employee_dumaguete_address = QTextEdit(self.scrollAreaWidgetContents)
        self.employee_dumaguete_address.setObjectName(u"employee_dumaguete_address")
        sizePolicy.setHeightForWidth(self.employee_dumaguete_address.sizePolicy().hasHeightForWidth())
        self.employee_dumaguete_address.setSizePolicy(sizePolicy)
        self.employee_dumaguete_address.setMinimumSize(QSize(0, 0))
        self.employee_dumaguete_address.setMaximumSize(QSize(500, 16777215))
        self.employee_dumaguete_address.setStyleSheet(u"border: 1px solid black")

        self.gridLayout.addWidget(self.employee_dumaguete_address, 6, 0, 1, 1)

        self.employee_email = QLabel(self.scrollAreaWidgetContents)
        self.employee_email.setObjectName(u"employee_email")
        self.employee_email.setFont(font1)
        self.employee_email.setStyleSheet(u"border: 1px solid black;")

        self.gridLayout.addWidget(self.employee_email, 14, 2, 1, 1)

        self.employee_spouse = QLabel(self.scrollAreaWidgetContents)
        self.employee_spouse.setObjectName(u"employee_spouse")
        self.employee_spouse.setFont(font1)
        self.employee_spouse.setStyleSheet(u"border: 1px solid black;")

        self.gridLayout.addWidget(self.employee_spouse, 17, 0, 1, 1)

        self.employee_pagibig = QLabel(self.scrollAreaWidgetContents)
        self.employee_pagibig.setObjectName(u"employee_pagibig")
        self.employee_pagibig.setFont(font1)
        self.employee_pagibig.setStyleSheet(u"border: 1px solid black;")

        self.gridLayout.addWidget(self.employee_pagibig, 15, 1, 1, 1)

        self.citz_header = QLabel(self.scrollAreaWidgetContents)
        self.citz_header.setObjectName(u"citz_header")
        self.citz_header.setFont(font)

        self.gridLayout.addWidget(self.citz_header, 11, 0, 1, 1)

        self.breadcrumb_label = QLabel(self.scrollAreaWidgetContents)
        self.breadcrumb_label.setObjectName(u"breadcrumb_label")
        self.breadcrumb_label.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.breadcrumb_label.setPixmap(QPixmap(u":/images/title2_header3.png"))

        self.gridLayout.addWidget(self.breadcrumb_label, 0, 0, 1, 1)

        self.birthday_header = QLabel(self.scrollAreaWidgetContents)
        self.birthday_header.setObjectName(u"birthday_header")
        self.birthday_header.setFont(font)

        self.gridLayout.addWidget(self.birthday_header, 9, 0, 1, 1)

        self.employee_religion = QLabel(self.scrollAreaWidgetContents)
        self.employee_religion.setObjectName(u"employee_religion")
        self.employee_religion.setFont(font1)
        self.employee_religion.setStyleSheet(u"border: 1px solid black;")

        self.gridLayout.addWidget(self.employee_religion, 27, 0, 1, 1)

        self.employee_birthday = QLabel(self.scrollAreaWidgetContents)
        self.employee_birthday.setObjectName(u"employee_birthday")
        self.employee_birthday.setFont(font1)
        self.employee_birthday.setStyleSheet(u"border: 1px solid black;")

        self.gridLayout.addWidget(self.employee_birthday, 10, 0, 1, 1)

        self.contact_header = QLabel(self.scrollAreaWidgetContents)
        self.contact_header.setObjectName(u"contact_header")
        self.contact_header.setFont(font)

        self.gridLayout.addWidget(self.contact_header, 11, 2, 1, 1)

        self.employee_sss = QLabel(self.scrollAreaWidgetContents)
        self.employee_sss.setObjectName(u"employee_sss")
        self.employee_sss.setFont(font1)
        self.employee_sss.setStyleSheet(u"border: 1px solid black;")

        self.gridLayout.addWidget(self.employee_sss, 12, 1, 1, 1)

        self.father_header = QLabel(self.scrollAreaWidgetContents)
        self.father_header.setObjectName(u"father_header")
        self.father_header.setFont(font)

        self.gridLayout.addWidget(self.father_header, 5, 1, 1, 1)

        self.church_header = QLabel(self.scrollAreaWidgetContents)
        self.church_header.setObjectName(u"church_header")
        self.church_header.setFont(font)

        self.gridLayout.addWidget(self.church_header, 23, 0, 1, 1)

        self.employee_citizenship = QLabel(self.scrollAreaWidgetContents)
        self.employee_citizenship.setObjectName(u"employee_citizenship")
        self.employee_citizenship.setFont(font1)
        self.employee_citizenship.setStyleSheet(u"border: 1px solid black;")

        self.gridLayout.addWidget(self.employee_citizenship, 12, 0, 1, 1)

        self.employee_phonenumber = QLabel(self.scrollAreaWidgetContents)
        self.employee_phonenumber.setObjectName(u"employee_phonenumber")
        self.employee_phonenumber.setFont(font1)
        self.employee_phonenumber.setStyleSheet(u"border: 1px solid black;")

        self.gridLayout.addWidget(self.employee_phonenumber, 12, 2, 1, 1)

        self.children_header = QLabel(self.scrollAreaWidgetContents)
        self.children_header.setObjectName(u"children_header")
        self.children_header.setFont(font)

        self.gridLayout.addWidget(self.children_header, 5, 2, 1, 1)

        self.employee_children = QTextEdit(self.scrollAreaWidgetContents)
        self.employee_children.setObjectName(u"employee_children")
        self.employee_children.setMaximumSize(QSize(500, 16777215))
        self.employee_children.setStyleSheet(u"border: 1px solid black")

        self.gridLayout.addWidget(self.employee_children, 6, 2, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.groupBox_2.setTitle("")
        self.label_3.setText("")
        self.label_4.setText("")
        self.label.setText("")
        self.civ_status_header.setText(QCoreApplication.translate("MainWindow", u"Civil Status", None))
        self.acad_record_header.setText(QCoreApplication.translate("MainWindow", u"Academic Record", None))
        self.spouse_header.setText(QCoreApplication.translate("MainWindow", u"Name of Spouse", None))
        self.employee_address_header.setText(QCoreApplication.translate("MainWindow", u"Home Address", None))
        self.employee_civil_status.setText(QCoreApplication.translate("MainWindow", u"Married in Dumaguete on May 29, 2013", None))
        self.employee_father.setText(QCoreApplication.translate("MainWindow", u"Juanito D. Ela Cruz", None))
        self.publications_header.setText(QCoreApplication.translate("MainWindow", u"Publications", None))
        self.sss_header.setText(QCoreApplication.translate("MainWindow", u"SSS Number", None))
        self.employee_mother.setText(QCoreApplication.translate("MainWindow", u"Juanita D. Ela Cruz", None))
        self.employee_duma_address_header.setText(QCoreApplication.translate("MainWindow", u"Dumaguete Address", None))
        self.brother_header.setText(QCoreApplication.translate("MainWindow", u"Sibling", None))
        self.employee_philHealth.setText(QCoreApplication.translate("MainWindow", u"22-111111-12038", None))
        self.groupBox.setTitle("")
        self.edit_info_button.setText(QCoreApplication.translate("MainWindow", u"Edit Information", None))
        self.archive_button.setText(QCoreApplication.translate("MainWindow", u"Archive", None))
        self.archive_button_2.setText(QCoreApplication.translate("MainWindow", u"Salary", None))
        self.employee_name.setText(QCoreApplication.translate("MainWindow", u"Juan Dela Cruz", None))
        self.employee_position.setText(QCoreApplication.translate("MainWindow", u"Professor", None))
        self.employee_department.setText(QCoreApplication.translate("MainWindow", u"College of Computer Studies", None))
        self.employee_hired_date.setText(QCoreApplication.translate("MainWindow", u"Employed on 08/06/2024", None))
        self.pagibig_header.setText(QCoreApplication.translate("MainWindow", u"Pag-Ibig Number", None))
        self.mother_header.setText(QCoreApplication.translate("MainWindow", u"Mother", None))
        self.ph_header.setText(QCoreApplication.translate("MainWindow", u"Philhealth Number", None))
        self.employee_email.setText(QCoreApplication.translate("MainWindow", u"juandelacruz@su.edu.ph", None))
        self.employee_spouse.setText(QCoreApplication.translate("MainWindow", u"Ada P. Graming", None))
        self.employee_pagibig.setText(QCoreApplication.translate("MainWindow", u"22-111111-12038", None))
        self.citz_header.setText(QCoreApplication.translate("MainWindow", u"Citizenship", None))
        self.breadcrumb_label.setText("")
        self.birthday_header.setText(QCoreApplication.translate("MainWindow", u"Date of Birth", None))
        self.employee_religion.setText(QCoreApplication.translate("MainWindow", u"Church of Pickle Rick", None))
        self.employee_birthday.setText(QCoreApplication.translate("MainWindow", u"May 9, 1945", None))
        self.contact_header.setText(QCoreApplication.translate("MainWindow", u"Contact Information", None))
        self.employee_sss.setText(QCoreApplication.translate("MainWindow", u"22-111111-12038", None))
        self.father_header.setText(QCoreApplication.translate("MainWindow", u"Father", None))
        self.church_header.setText(QCoreApplication.translate("MainWindow", u"Church Affiliation", None))
        self.employee_citizenship.setText(QCoreApplication.translate("MainWindow", u"Filipino", None))
        self.employee_phonenumber.setText(QCoreApplication.translate("MainWindow", u"0920 1337 420", None))
        self.children_header.setText(QCoreApplication.translate("MainWindow", u"Children", None))
    # retranslateUi

