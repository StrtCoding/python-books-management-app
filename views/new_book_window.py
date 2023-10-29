# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_book_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide6.QtWidgets import *


class NewBookForm(object):
    def setupUi(self, NewBookWindow):
        if not NewBookWindow.objectName():
            NewBookWindow.setObjectName(u"NewBookWindow")
        NewBookWindow.resize(405, 472)
        NewBookWindow.setCursor(QCursor(Qt.PointingHandCursor))
        self.label = QLabel(NewBookWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 381, 20))
        self.label.setFrameShape(QFrame.Box)
        self.label_2 = QLabel(NewBookWindow)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 60, 61, 13))
        self.titleLineEdit = QLineEdit(NewBookWindow)
        self.titleLineEdit.setObjectName(u"titleLineEdit")
        self.titleLineEdit.setGeometry(QRect(30, 80, 351, 20))
        self.label_3 = QLabel(NewBookWindow)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 110, 61, 13))
        self.categoryLineEdit = QLineEdit(NewBookWindow)
        self.categoryLineEdit.setObjectName(u"categoryLineEdit")
        self.categoryLineEdit.setGeometry(QRect(30, 130, 271, 20))
        self.label_4 = QLabel(NewBookWindow)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 160, 121, 16))
        self.pageQtySpinBox = QSpinBox(NewBookWindow)
        self.pageQtySpinBox.setMaximum(2000)
        self.pageQtySpinBox.setObjectName(u"pageQtySpinBox")
        self.pageQtySpinBox.setGeometry(QRect(30, 180, 101, 22))
        self.label_5 = QLabel(NewBookWindow)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 210, 121, 16))
        self.filePathLineEdit = QLineEdit(NewBookWindow)
        self.filePathLineEdit.setObjectName(u"filePathLineEdit")
        self.filePathLineEdit.setGeometry(QRect(30, 230, 191, 20))
        self.selectFileButton = QPushButton(NewBookWindow)
        self.selectFileButton.setObjectName(u"selectFileButton")
        self.selectFileButton.setGeometry(QRect(230, 230, 31, 31))
        self.selectFileButton.setStyleSheet(u"\n"
"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"./assets/icons/select-file.icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.selectFileButton.setIcon(icon)
        self.selectFileButton.setIconSize(QSize(30, 30))
        self.selectFileButton.setFlat(True)
        self.label_6 = QLabel(NewBookWindow)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 280, 121, 16))
        self.descriptionTextedit = QTextEdit(NewBookWindow)
        self.descriptionTextedit.setObjectName(u"descriptionTextedit")
        self.descriptionTextedit.setGeometry(QRect(30, 300, 351, 111))
        self.addButton = QPushButton(NewBookWindow)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(94, 430, 101, 31))
        self.addButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.addButton.setStyleSheet(u"QPushButton\n"
"{	\n"
"	height: 2em;\n"
" 	border-style: solid;\n"
"	border-width: 2px;\n"
" 	border-color: #0069c0;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   	background-color:#0069c0;\n"
"	color:white;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"./assets/icons/add-book-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addButton.setIcon(icon1)
        self.addButton.setIconSize(QSize(30, 30))
        self.addButton.setFlat(True)
        self.cancelButton = QPushButton(NewBookWindow)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(200, 430, 101, 31))
        self.cancelButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancelButton.setStyleSheet(u"QPushButton\n"
"{	\n"
"	height: 2em;\n"
" 	border-style: solid;\n"
"	border-width: 2px;\n"
" 	border-color: grey;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   	background-color:grey;\n"
"	color:white;\n"
"}")
        self.cancelButton.setIconSize(QSize(30, 30))
        self.cancelButton.setFlat(True)

        self.retranslateUi(NewBookWindow)

        QMetaObject.connectSlotsByName(NewBookWindow)
    # setupUi

    def retranslateUi(self, NewBookWindow):
        NewBookWindow.setWindowTitle(QCoreApplication.translate("NewBookWindow", u"Nuevo Libro", None))
        self.label.setText(QCoreApplication.translate("NewBookWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">NUEVO LIBRO</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("NewBookWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Titulo</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("NewBookWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Categoria</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("NewBookWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Cantidad de paginas</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("NewBookWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Seleccionar archivo</span></p></body></html>", None))
        self.selectFileButton.setText("")
        self.label_6.setText(QCoreApplication.translate("NewBookWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Descripcion del libro</span></p></body></html>", None))
        self.addButton.setText(QCoreApplication.translate("NewBookWindow", u"AGREGAR", None))
        self.cancelButton.setText(QCoreApplication.translate("NewBookWindow", u"CANCELAR", None))
    # retranslateUi

