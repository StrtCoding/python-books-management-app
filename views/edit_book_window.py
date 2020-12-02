# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_book_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class EditBookForm(object):
    def setupUi(self, EditBookWindow):
        if not EditBookWindow.objectName():
            EditBookWindow.setObjectName(u"EditBookWindow")
        EditBookWindow.resize(405, 536)
        EditBookWindow.setCursor(QCursor(Qt.PointingHandCursor))
        self.label = QLabel(EditBookWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 381, 20))
        self.label.setFrameShape(QFrame.Box)
        self.label_2 = QLabel(EditBookWindow)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 60, 61, 13))
        self.titleLineEdit = QLineEdit(EditBookWindow)
        self.titleLineEdit.setObjectName(u"titleLineEdit")
        self.titleLineEdit.setGeometry(QRect(30, 80, 351, 20))
        self.label_3 = QLabel(EditBookWindow)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 110, 61, 13))
        self.categoryLineEdit = QLineEdit(EditBookWindow)
        self.categoryLineEdit.setObjectName(u"categoryLineEdit")
        self.categoryLineEdit.setGeometry(QRect(30, 130, 271, 20))
        self.label_4 = QLabel(EditBookWindow)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 160, 121, 16))
        self.pageQtySpinBox = QSpinBox(EditBookWindow)
        self.pageQtySpinBox.setObjectName(u"pageQtySpinBox")
        self.pageQtySpinBox.setGeometry(QRect(30, 180, 101, 22))
        self.label_5 = QLabel(EditBookWindow)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 270, 121, 16))
        self.filePathLineEdit = QLineEdit(EditBookWindow)
        self.filePathLineEdit.setObjectName(u"filePathLineEdit")
        self.filePathLineEdit.setGeometry(QRect(30, 290, 191, 20))
        self.selectFileButton = QPushButton(EditBookWindow)
        self.selectFileButton.setObjectName(u"selectFileButton")
        self.selectFileButton.setGeometry(QRect(230, 290, 31, 31))
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
        self.label_6 = QLabel(EditBookWindow)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 340, 121, 16))
        self.descriptionTextedit = QTextEdit(EditBookWindow)
        self.descriptionTextedit.setObjectName(u"descriptionTextedit")
        self.descriptionTextedit.setGeometry(QRect(30, 360, 351, 111))
        self.editButton = QPushButton(EditBookWindow)
        self.editButton.setObjectName(u"editButton")
        self.editButton.setGeometry(QRect(94, 490, 101, 31))
        self.editButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.editButton.setStyleSheet(u"QPushButton\n"
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
        icon1.addFile(u"./assets/icons/edit-book.png", QSize(), QIcon.Normal, QIcon.Off)
        self.editButton.setIcon(icon1)
        self.editButton.setIconSize(QSize(30, 30))
        self.editButton.setFlat(True)
        self.cancelButton = QPushButton(EditBookWindow)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(200, 490, 101, 31))
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
        self.label_7 = QLabel(EditBookWindow)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(30, 220, 161, 16))
        self.pageReadQtySpinBox = QSpinBox(EditBookWindow)
        self.pageReadQtySpinBox.setObjectName(u"pageReadQtySpinBox")
        self.pageReadQtySpinBox.setGeometry(QRect(30, 240, 101, 22))

        self.retranslateUi(EditBookWindow)

        QMetaObject.connectSlotsByName(EditBookWindow)
    # setupUi

    def retranslateUi(self, EditBookWindow):
        EditBookWindow.setWindowTitle(QCoreApplication.translate("EditBookWindow", u"Editar Libro", None))
        self.label.setText(QCoreApplication.translate("EditBookWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">EDITAR LIBRO</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("EditBookWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Titulo</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("EditBookWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Categoria</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("EditBookWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Cantidad de paginas</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("EditBookWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Seleccionar archivo</span></p></body></html>", None))
        self.selectFileButton.setText("")
        self.label_6.setText(QCoreApplication.translate("EditBookWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Descripcion del libro</span></p></body></html>", None))
        self.editButton.setText(QCoreApplication.translate("EditBookWindow", u"EDITAR", None))
        self.cancelButton.setText(QCoreApplication.translate("EditBookWindow", u"CANCELAR", None))
        self.label_7.setText(QCoreApplication.translate("EditBookWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Cantidad de paginas leidas</span></p></body></html>", None))
    # retranslateUi

