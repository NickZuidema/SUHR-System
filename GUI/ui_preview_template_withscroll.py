# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'preview_template_withscrolltLhpru.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGraphicsView, QGridLayout,
    QGroupBox, QLabel, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QStatusBar, QTextEdit,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1422, 734)
        MainWindow.setStyleSheet(u"color: black;\n"
"background-color: rgb(208, 208, 208)")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 30, 91, 81))
        self.label.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.label.setPixmap(QPixmap(u":/images/logo_silliman.png"))
        self.label.setScaledContents(True)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(150, 30, 161, 41))
        self.label_3.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.label_3.setPixmap(QPixmap(u":/images/title2_header1.png"))
        self.label_3.setScaledContents(False)
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(-10, 140, 1461, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, -10, 1451, 161))
        self.label_2.setPixmap(QPixmap(u":/images/background2_header.png"))
        self.label_2.setScaledContents(True)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(150, 90, 271, 16))
        self.label_4.setStyleSheet(u"background-color: white;")
        self.label_4.setPixmap(QPixmap(u":/images/title2_header2.png"))
        self.home_button = QPushButton(self.centralwidget)
        self.home_button.setObjectName(u"home_button")
        self.home_button.setGeometry(QRect(1250, 60, 41, 31))
        self.home_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.home_button.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        icon = QIcon()
        icon.addFile(u":/images/button_home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_button.setIcon(icon)
        self.home_button.setIconSize(QSize(256, 256))
        self.logout_button = QPushButton(self.centralwidget)
        self.logout_button.setObjectName(u"logout_button")
        self.logout_button.setGeometry(QRect(1310, 60, 75, 24))
        self.logout_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.logout_button.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        icon1 = QIcon()
        icon1.addFile(u":/images/button_logout.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logout_button.setIcon(icon1)
        self.logout_button.setIconSize(QSize(500, 500))
        self.breadcrumb_label = QLabel(self.centralwidget)
        self.breadcrumb_label.setObjectName(u"breadcrumb_label")
        self.breadcrumb_label.setGeometry(QRect(10, 160, 381, 31))
        self.breadcrumb_label.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.breadcrumb_label.setPixmap(QPixmap(u":/images/title2_header3.png"))
        self.home_button_2 = QPushButton(self.centralwidget)
        self.home_button_2.setObjectName(u"home_button_2")
        self.home_button_2.setGeometry(QRect(30, 670, 41, 31))
        self.home_button_2.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.home_button_2.setIcon(icon)
        self.home_button_2.setIconSize(QSize(256, 256))
        self.logout_button_2 = QPushButton(self.centralwidget)
        self.logout_button_2.setObjectName(u"logout_button_2")
        self.logout_button_2.setGeometry(QRect(100, 680, 75, 24))
        self.logout_button_2.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.logout_button_2.setIcon(icon1)
        self.logout_button_2.setIconSize(QSize(500, 500))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(1030, 660, 361, 41))
        font = QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setPixmap(QPixmap(u":/images/title2_header2.png"))
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(10, 200, 1401, 401))
        self.scrollArea.setStyleSheet(u"background-color: rgb(208, 208, 208)")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1382, 977))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.acad_record_header = QLabel(self.scrollAreaWidgetContents)
        self.acad_record_header.setObjectName(u"acad_record_header")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.acad_record_header.setFont(font1)

        self.gridLayout.addWidget(self.acad_record_header, 10, 2, 1, 1)

        self.employee_history = QTextEdit(self.scrollAreaWidgetContents)
        self.employee_history.setObjectName(u"employee_history")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.employee_history.sizePolicy().hasHeightForWidth())
        self.employee_history.setSizePolicy(sizePolicy)
        self.employee_history.setStyleSheet(u"border: 1px solid black")

        self.gridLayout.addWidget(self.employee_history, 9, 2, 1, 1)

        self.sss_header = QLabel(self.scrollAreaWidgetContents)
        self.sss_header.setObjectName(u"sss_header")
        self.sss_header.setFont(font1)

        self.gridLayout.addWidget(self.sss_header, 10, 1, 1, 1)

        self.employee_birthday = QLabel(self.scrollAreaWidgetContents)
        self.employee_birthday.setObjectName(u"employee_birthday")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        self.employee_birthday.setFont(font2)

        self.gridLayout.addWidget(self.employee_birthday, 7, 0, 1, 1)

        self.employee_pagibig = QLabel(self.scrollAreaWidgetContents)
        self.employee_pagibig.setObjectName(u"employee_pagibig")
        self.employee_pagibig.setFont(font2)

        self.gridLayout.addWidget(self.employee_pagibig, 13, 1, 1, 1)

        self.employee_phonenumber = QLabel(self.scrollAreaWidgetContents)
        self.employee_phonenumber.setObjectName(u"employee_phonenumber")
        self.employee_phonenumber.setFont(font2)

        self.gridLayout.addWidget(self.employee_phonenumber, 19, 1, 1, 1)

        self.citz_header = QLabel(self.scrollAreaWidgetContents)
        self.citz_header.setObjectName(u"citz_header")
        self.citz_header.setFont(font1)

        self.gridLayout.addWidget(self.citz_header, 8, 0, 1, 1)

        self.employee_school_distinctions = QTextEdit(self.scrollAreaWidgetContents)
        self.employee_school_distinctions.setObjectName(u"employee_school_distinctions")
        sizePolicy.setHeightForWidth(self.employee_school_distinctions.sizePolicy().hasHeightForWidth())
        self.employee_school_distinctions.setSizePolicy(sizePolicy)
        self.employee_school_distinctions.setStyleSheet(u"border: 1px solid black")

        self.gridLayout.addWidget(self.employee_school_distinctions, 5, 2, 1, 1)

        self.employee_dumaguete_address = QTextEdit(self.scrollAreaWidgetContents)
        self.employee_dumaguete_address.setObjectName(u"employee_dumaguete_address")
        sizePolicy.setHeightForWidth(self.employee_dumaguete_address.sizePolicy().hasHeightForWidth())
        self.employee_dumaguete_address.setSizePolicy(sizePolicy)
        self.employee_dumaguete_address.setMinimumSize(QSize(0, 0))
        self.employee_dumaguete_address.setStyleSheet(u"border: 1px solid black")

        self.gridLayout.addWidget(self.employee_dumaguete_address, 3, 0, 1, 1)

        self.employee_spouse = QLabel(self.scrollAreaWidgetContents)
        self.employee_spouse.setObjectName(u"employee_spouse")
        self.employee_spouse.setFont(font2)

        self.gridLayout.addWidget(self.employee_spouse, 13, 0, 1, 1)

        self.children_header = QLabel(self.scrollAreaWidgetContents)
        self.children_header.setObjectName(u"children_header")
        self.children_header.setFont(font1)

        self.gridLayout.addWidget(self.children_header, 14, 0, 1, 1)

        self.employee_publications = QTextEdit(self.scrollAreaWidgetContents)
        self.employee_publications.setObjectName(u"employee_publications")
        sizePolicy.setHeightForWidth(self.employee_publications.sizePolicy().hasHeightForWidth())
        self.employee_publications.setSizePolicy(sizePolicy)
        self.employee_publications.setStyleSheet(u"border: 1px solid black")

        self.gridLayout.addWidget(self.employee_publications, 7, 2, 1, 1)

        self.employee_religion = QLabel(self.scrollAreaWidgetContents)
        self.employee_religion.setObjectName(u"employee_religion")
        self.employee_religion.setFont(font2)

        self.gridLayout.addWidget(self.employee_religion, 19, 0, 1, 1)

        self.employee_father = QLabel(self.scrollAreaWidgetContents)
        self.employee_father.setObjectName(u"employee_father")
        self.employee_father.setFont(font2)

        self.gridLayout.addWidget(self.employee_father, 3, 1, 1, 1)

        self.employee_sister = QTextEdit(self.scrollAreaWidgetContents)
        self.employee_sister.setObjectName(u"employee_sister")
        sizePolicy.setHeightForWidth(self.employee_sister.sizePolicy().hasHeightForWidth())
        self.employee_sister.setSizePolicy(sizePolicy)
        self.employee_sister.setStyleSheet(u"border: 1px solid black")

        self.gridLayout.addWidget(self.employee_sister, 9, 1, 1, 1)

        self.employee_brother = QTextEdit(self.scrollAreaWidgetContents)
        self.employee_brother.setObjectName(u"employee_brother")
        sizePolicy.setHeightForWidth(self.employee_brother.sizePolicy().hasHeightForWidth())
        self.employee_brother.setSizePolicy(sizePolicy)
        self.employee_brother.setStyleSheet(u"border: 1px solid black")

        self.gridLayout.addWidget(self.employee_brother, 7, 1, 1, 1)

        self.mother_header = QLabel(self.scrollAreaWidgetContents)
        self.mother_header.setObjectName(u"mother_header")
        self.mother_header.setFont(font1)

        self.gridLayout.addWidget(self.mother_header, 4, 1, 1, 1)

        self.groupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.groupBox.setMinimumSize(QSize(1000, 200))
        self.groupBox.setStyleSheet(u"border: 0px;")
        self.edit_info_button = QPushButton(self.groupBox)
        self.edit_info_button.setObjectName(u"edit_info_button")
        self.edit_info_button.setGeometry(QRect(10, 150, 131, 16))
        self.edit_info_button.setCursor(QCursor(Qt.ArrowCursor))
        self.edit_info_button.setStyleSheet(u"border-radius: 5px;\n"
"\n"
"background-color: rgb(50, 50, 50);\n"
"color: white;\n"
"font-weight: bold;\n"
"")
        self.archive_button = QPushButton(self.groupBox)
        self.archive_button.setObjectName(u"archive_button")
        self.archive_button.setGeometry(QRect(150, 150, 101, 16))
        self.archive_button.setStyleSheet(u"border-radius: 5px;\n"
"\n"
"background-color: rgb(138, 138, 138);\n"
"color: white;\n"
"font-weight: bold;\n"
"")
        self.archive_button_2 = QPushButton(self.groupBox)
        self.archive_button_2.setObjectName(u"archive_button_2")
        self.archive_button_2.setGeometry(QRect(270, 150, 101, 16))
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

        self.gridLayout.addWidget(self.groupBox, 0, 1, 1, 2)

        self.spouse_header = QLabel(self.scrollAreaWidgetContents)
        self.spouse_header.setObjectName(u"spouse_header")
        self.spouse_header.setFont(font1)

        self.gridLayout.addWidget(self.spouse_header, 12, 0, 1, 1)

        self.employee_philHealth = QLabel(self.scrollAreaWidgetContents)
        self.employee_philHealth.setObjectName(u"employee_philHealth")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.employee_philHealth.sizePolicy().hasHeightForWidth())
        self.employee_philHealth.setSizePolicy(sizePolicy2)
        self.employee_philHealth.setFont(font2)

        self.gridLayout.addWidget(self.employee_philHealth, 15, 1, 1, 1)

        self.contact_header = QLabel(self.scrollAreaWidgetContents)
        self.contact_header.setObjectName(u"contact_header")
        self.contact_header.setFont(font1)

        self.gridLayout.addWidget(self.contact_header, 18, 1, 1, 1)

        self.employee_citizenship = QLabel(self.scrollAreaWidgetContents)
        self.employee_citizenship.setObjectName(u"employee_citizenship")
        self.employee_citizenship.setFont(font2)

        self.gridLayout.addWidget(self.employee_citizenship, 9, 0, 1, 1)

        self.ph_header = QLabel(self.scrollAreaWidgetContents)
        self.ph_header.setObjectName(u"ph_header")
        self.ph_header.setFont(font1)

        self.gridLayout.addWidget(self.ph_header, 14, 1, 1, 1)

        self.employee_civil_status = QLabel(self.scrollAreaWidgetContents)
        self.employee_civil_status.setObjectName(u"employee_civil_status")
        self.employee_civil_status.setFont(font2)

        self.gridLayout.addWidget(self.employee_civil_status, 11, 0, 1, 1)

        self.employee_sss = QLabel(self.scrollAreaWidgetContents)
        self.employee_sss.setObjectName(u"employee_sss")
        self.employee_sss.setFont(font2)

        self.gridLayout.addWidget(self.employee_sss, 11, 1, 1, 1)

        self.Profile_pic_2 = QGraphicsView(self.scrollAreaWidgetContents)
        self.Profile_pic_2.setObjectName(u"Profile_pic_2")
        sizePolicy1.setHeightForWidth(self.Profile_pic_2.sizePolicy().hasHeightForWidth())
        self.Profile_pic_2.setSizePolicy(sizePolicy1)
        self.Profile_pic_2.setStyleSheet(u"border: 1px solid black")

        self.gridLayout.addWidget(self.Profile_pic_2, 0, 0, 1, 1)

        self.prev_employment_header = QLabel(self.scrollAreaWidgetContents)
        self.prev_employment_header.setObjectName(u"prev_employment_header")
        self.prev_employment_header.setFont(font1)

        self.gridLayout.addWidget(self.prev_employment_header, 8, 2, 1, 1)

        self.brother_header_2 = QLabel(self.scrollAreaWidgetContents)
        self.brother_header_2.setObjectName(u"brother_header_2")
        self.brother_header_2.setFont(font1)

        self.gridLayout.addWidget(self.brother_header_2, 8, 1, 1, 1)

        self.schoolheader = QLabel(self.scrollAreaWidgetContents)
        self.schoolheader.setObjectName(u"schoolheader")
        self.schoolheader.setFont(font1)

        self.gridLayout.addWidget(self.schoolheader, 4, 2, 1, 1)

        self.employee_children = QTextEdit(self.scrollAreaWidgetContents)
        self.employee_children.setObjectName(u"employee_children")
        self.employee_children.setStyleSheet(u"border: 1px solid black")

        self.gridLayout.addWidget(self.employee_children, 15, 0, 1, 1)

        self.church_header = QLabel(self.scrollAreaWidgetContents)
        self.church_header.setObjectName(u"church_header")
        self.church_header.setFont(font1)

        self.gridLayout.addWidget(self.church_header, 18, 0, 1, 1)

        self.employee_home_address = QTextEdit(self.scrollAreaWidgetContents)
        self.employee_home_address.setObjectName(u"employee_home_address")
        self.employee_home_address.setStyleSheet(u"border: 1px solid black")

        self.gridLayout.addWidget(self.employee_home_address, 5, 0, 1, 1)

        self.relation_header = QLabel(self.scrollAreaWidgetContents)
        self.relation_header.setObjectName(u"relation_header")
        self.relation_header.setFont(font1)

        self.gridLayout.addWidget(self.relation_header, 2, 2, 1, 1)

        self.brother_header = QLabel(self.scrollAreaWidgetContents)
        self.brother_header.setObjectName(u"brother_header")
        self.brother_header.setFont(font1)

        self.gridLayout.addWidget(self.brother_header, 6, 1, 1, 1)

        self.father_header = QLabel(self.scrollAreaWidgetContents)
        self.father_header.setObjectName(u"father_header")
        self.father_header.setFont(font1)

        self.gridLayout.addWidget(self.father_header, 2, 1, 1, 1)

        self.employee_mother = QLabel(self.scrollAreaWidgetContents)
        self.employee_mother.setObjectName(u"employee_mother")
        self.employee_mother.setFont(font2)

        self.gridLayout.addWidget(self.employee_mother, 5, 1, 1, 1)

        self.publications_header = QLabel(self.scrollAreaWidgetContents)
        self.publications_header.setObjectName(u"publications_header")
        self.publications_header.setFont(font1)

        self.gridLayout.addWidget(self.publications_header, 6, 2, 1, 1)

        self.birthday_header = QLabel(self.scrollAreaWidgetContents)
        self.birthday_header.setObjectName(u"birthday_header")
        self.birthday_header.setFont(font1)

        self.gridLayout.addWidget(self.birthday_header, 6, 0, 1, 1)

        self.employee_acad_record = QTextEdit(self.scrollAreaWidgetContents)
        self.employee_acad_record.setObjectName(u"employee_acad_record")
        sizePolicy.setHeightForWidth(self.employee_acad_record.sizePolicy().hasHeightForWidth())
        self.employee_acad_record.setSizePolicy(sizePolicy)
        self.employee_acad_record.setStyleSheet(u"border: 1px solid black")

        self.gridLayout.addWidget(self.employee_acad_record, 11, 2, 1, 1)

        self.pagibig_header = QLabel(self.scrollAreaWidgetContents)
        self.pagibig_header.setObjectName(u"pagibig_header")
        self.pagibig_header.setFont(font1)

        self.gridLayout.addWidget(self.pagibig_header, 12, 1, 1, 1)

        self.employee_address_header = QLabel(self.scrollAreaWidgetContents)
        self.employee_address_header.setObjectName(u"employee_address_header")
        self.employee_address_header.setFont(font1)

        self.gridLayout.addWidget(self.employee_address_header, 4, 0, 1, 1)

        self.employee_email = QLabel(self.scrollAreaWidgetContents)
        self.employee_email.setObjectName(u"employee_email")
        self.employee_email.setFont(font2)

        self.gridLayout.addWidget(self.employee_email, 20, 1, 1, 1)

        self.civ_status_header = QLabel(self.scrollAreaWidgetContents)
        self.civ_status_header.setObjectName(u"civ_status_header")
        self.civ_status_header.setFont(font1)

        self.gridLayout.addWidget(self.civ_status_header, 10, 0, 1, 1)

        self.employee_duma_address_header = QLabel(self.scrollAreaWidgetContents)
        self.employee_duma_address_header.setObjectName(u"employee_duma_address_header")
        self.employee_duma_address_header.setFont(font1)

        self.gridLayout.addWidget(self.employee_duma_address_header, 2, 0, 1, 1)

        self.employee_relation = QLabel(self.scrollAreaWidgetContents)
        self.employee_relation.setObjectName(u"employee_relation")
        self.employee_relation.setFont(font2)

        self.gridLayout.addWidget(self.employee_relation, 3, 2, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.edit_info_button_2 = QPushButton(self.centralwidget)
        self.edit_info_button_2.setObjectName(u"edit_info_button_2")
        self.edit_info_button_2.setGeometry(QRect(20, 620, 131, 16))
        self.edit_info_button_2.setStyleSheet(u"border-radius: 5px;\n"
"\n"
"background-color: rgb(50, 50, 50);\n"
"color: white;\n"
"font-weight: bold;\n"
"")
        self.archive_button_3 = QPushButton(self.centralwidget)
        self.archive_button_3.setObjectName(u"archive_button_3")
        self.archive_button_3.setGeometry(QRect(170, 620, 101, 16))
        self.archive_button_3.setStyleSheet(u"border-radius: 5px;\n"
"\n"
"background-color: rgb(138, 138, 138);\n"
"color: white;\n"
"font-weight: bold;\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)
        self.label_2.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.line.raise_()
        self.label_4.raise_()
        self.home_button.raise_()
        self.logout_button.raise_()
        self.breadcrumb_label.raise_()
        self.home_button_2.raise_()
        self.logout_button_2.raise_()
        self.label_5.raise_()
        self.scrollArea.raise_()
        self.edit_info_button_2.raise_()
        self.archive_button_3.raise_()
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.label.setText("")
        self.label_3.setText("")
        self.label_2.setText("")
        self.label_4.setText("")
        self.home_button.setText("")
        self.logout_button.setText("")
        self.breadcrumb_label.setText("")
        self.home_button_2.setText("")
        self.logout_button_2.setText("")
        self.label_5.setText("")
        self.acad_record_header.setText(QCoreApplication.translate("MainWindow", u"Academic Record", None))
        self.sss_header.setText(QCoreApplication.translate("MainWindow", u"SSS Number", None))
        self.employee_birthday.setText(QCoreApplication.translate("MainWindow", u"May 9, 1945", None))
        self.employee_pagibig.setText(QCoreApplication.translate("MainWindow", u"22-111111-12038", None))
        self.employee_phonenumber.setText(QCoreApplication.translate("MainWindow", u"0920 1337 420", None))
        self.citz_header.setText(QCoreApplication.translate("MainWindow", u"Citizenship", None))
        self.employee_spouse.setText(QCoreApplication.translate("MainWindow", u"Ada P. Graming", None))
        self.children_header.setText(QCoreApplication.translate("MainWindow", u"Children", None))
        self.employee_religion.setText(QCoreApplication.translate("MainWindow", u"Church of Pickle Rick", None))
        self.employee_father.setText(QCoreApplication.translate("MainWindow", u"Juanito D. Ela Cruz", None))
        self.mother_header.setText(QCoreApplication.translate("MainWindow", u"Mother", None))
        self.groupBox.setTitle("")
        self.edit_info_button.setText(QCoreApplication.translate("MainWindow", u"Edit Information", None))
        self.archive_button.setText(QCoreApplication.translate("MainWindow", u"Archive", None))
        self.archive_button_2.setText(QCoreApplication.translate("MainWindow", u"Salary", None))
        self.employee_name.setText(QCoreApplication.translate("MainWindow", u"Juan Dela Cruz", None))
        self.employee_position.setText(QCoreApplication.translate("MainWindow", u"Professor", None))
        self.employee_department.setText(QCoreApplication.translate("MainWindow", u"College of Computer Studies", None))
        self.employee_hired_date.setText(QCoreApplication.translate("MainWindow", u"Employed on 08/06/2024", None))
        self.spouse_header.setText(QCoreApplication.translate("MainWindow", u"Name of Spouse", None))
        self.employee_philHealth.setText(QCoreApplication.translate("MainWindow", u"22-111111-12038", None))
        self.contact_header.setText(QCoreApplication.translate("MainWindow", u"Contact Information", None))
        self.employee_citizenship.setText(QCoreApplication.translate("MainWindow", u"Filipino", None))
        self.ph_header.setText(QCoreApplication.translate("MainWindow", u"Philhealth Number", None))
        self.employee_civil_status.setText(QCoreApplication.translate("MainWindow", u"Married in Dumaguete on May 29, 2013", None))
        self.employee_sss.setText(QCoreApplication.translate("MainWindow", u"22-111111-12038", None))
        self.prev_employment_header.setText(QCoreApplication.translate("MainWindow", u"Record of Previous Employment", None))
        self.brother_header_2.setText(QCoreApplication.translate("MainWindow", u"Sister", None))
        self.schoolheader.setText(QCoreApplication.translate("MainWindow", u"School or College Distinctions", None))
        self.church_header.setText(QCoreApplication.translate("MainWindow", u"Church Affiliation", None))
        self.relation_header.setText(QCoreApplication.translate("MainWindow", u"Related Staff Member(s)", None))
        self.brother_header.setText(QCoreApplication.translate("MainWindow", u"Brother", None))
        self.father_header.setText(QCoreApplication.translate("MainWindow", u"Father", None))
        self.employee_mother.setText(QCoreApplication.translate("MainWindow", u"Juanita D. Ela Cruz", None))
        self.publications_header.setText(QCoreApplication.translate("MainWindow", u"Publications", None))
        self.birthday_header.setText(QCoreApplication.translate("MainWindow", u"Date of Birth", None))
        self.pagibig_header.setText(QCoreApplication.translate("MainWindow", u"Pag-Ibig Number", None))
        self.employee_address_header.setText(QCoreApplication.translate("MainWindow", u"Home Address", None))
        self.employee_email.setText(QCoreApplication.translate("MainWindow", u"juandelacruz@su.edu.ph", None))
        self.civ_status_header.setText(QCoreApplication.translate("MainWindow", u"Civil Status", None))
        self.employee_duma_address_header.setText(QCoreApplication.translate("MainWindow", u"Dumaguete Address", None))
        self.employee_relation.setText(QCoreApplication.translate("MainWindow", u"Juanita D. Ela Cruz, Wife, Professor", None))
        self.edit_info_button_2.setText(QCoreApplication.translate("MainWindow", u"Edit Information", None))
        self.archive_button_3.setText(QCoreApplication.translate("MainWindow", u"Archive", None))
    # retranslateUi

