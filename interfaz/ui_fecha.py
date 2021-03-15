# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'modalLaboralestsGMwm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *



class Ui_modalFecha(object):
    def setupUi(self, modalFecha):
        if not modalFecha.objectName():
            modalFecha.setObjectName(u"modalFecha")
        modalFecha.resize(331, 440)
        modalFecha.setStyleSheet(u"border-color: rgb(255,255,255);\n"
"border-width: 7px;\n"
"background-color: rgb(255, 255, 255);")
        self.lbl1 = QLabel(modalFecha)
        self.lbl1.setObjectName(u"lbl1")
        self.lbl1.setGeometry(QRect(10, 10, 271, 21))
        self.lbl1.setStyleSheet(u"  background: rgba(37, 40,80,0);\n"
"color: rgb(37, 40,80);\n"
"font-size: 12px; \n"
"font-weight: bold;\n"
"")
        self.lblFondoModal = QLabel(modalFecha)
        self.lblFondoModal.setObjectName(u"lblFondoModal")
        self.lblFondoModal.setGeometry(QRect(-10, -20, 441, 621))
        self.lblFondoModal.setStyleSheet(u"background-image: url(\"img/FONDO.png\");")
        self.calendarWidget = QCalendarWidget(modalFecha)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(20, 40, 291, 171))
        self.calendarWidget.setStyleSheet(u"font-size: 11px;\n"
"font-weight: bold;\n"
"")
        self.grupoBotones = QGroupBox(modalFecha)
        self.grupoBotones.setObjectName(u"grupoBotones")
        self.grupoBotones.setGeometry(QRect(10, 230, 311, 151))
        self.grupoBotones.setStyleSheet(u"color: rgb(37, 40,80);\n"
"font-size: 12px; \n"
"font-weight: bold;")
        self.checkLunes = QCheckBox(self.grupoBotones)
        self.checkLunes.setObjectName(u"checkLunes")
        self.checkLunes.setGeometry(QRect(20, 30, 81, 20))
        self.checkLunes.setStyleSheet(u"color: rgb(37, 40,80);\n"
"font-size: 12px; \n"
"")
        self.checkMartes = QCheckBox(self.grupoBotones)
        self.checkMartes.setObjectName(u"checkMartes")
        self.checkMartes.setGeometry(QRect(20, 60, 81, 20))
        self.checkMartes.setStyleSheet(u"color: rgb(37, 40,80);\n"
"font-size: 12px; \n"
"")
        self.checkMier = QCheckBox(self.grupoBotones)
        self.checkMier.setObjectName(u"checkMier")
        self.checkMier.setGeometry(QRect(20, 90, 101, 20))
        self.checkMier.setStyleSheet(u"color: rgb(37, 40,80);\n"
"font-size: 12px; \n"
"")
        self.checkSabado = QCheckBox(self.grupoBotones)
        self.checkSabado.setObjectName(u"checkSabado")
        self.checkSabado.setGeometry(QRect(150, 60, 91, 20))
        self.checkSabado.setStyleSheet(u"color: rgb(37, 40,80);\n"
"font-size: 12px; \n"
"")
        self.checkViernes = QCheckBox(self.grupoBotones)
        self.checkViernes.setObjectName(u"checkViernes")
        self.checkViernes.setGeometry(QRect(150, 30, 91, 20))
        self.checkViernes.setStyleSheet(u"color: rgb(37, 40,80);\n"
"font-size: 12px; \n"
"")
        self.checkDom = QCheckBox(self.grupoBotones)
        self.checkDom.setObjectName(u"checkDom")
        self.checkDom.setGeometry(QRect(150, 90, 121, 20))
        self.checkDom.setStyleSheet(u"color: rgb(37, 40,80);\n"
"font-size: 12px; \n"
"")
        self.checkJueves = QCheckBox(self.grupoBotones)
        self.checkJueves.setObjectName(u"checkJueves")
        self.checkJueves.setGeometry(QRect(20, 120, 91, 20))
        self.checkJueves.setStyleSheet(u"color: rgb(37, 40,80);\n"
"font-size: 12px; \n"
"")
        self.btnAceptarFecha = QPushButton(modalFecha)
        self.btnAceptarFecha.setObjectName(u"btnAceptarFecha")
        self.btnAceptarFecha.setGeometry(QRect(110, 390, 91, 31))
        self.btnAceptarFecha.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAceptarFecha.setStyleSheet(u"font-size: 12px; font-weight: bold; font-family: Open Sans; color: #009999;\n"
"background: rgb(37, 40,80);\n"
"border-radius: 10px;\n"
"color : rgb(255,255,255)")
        self.lblFondoModal.raise_()
        self.lbl1.raise_()
        self.calendarWidget.raise_()
        self.grupoBotones.raise_()
        self.btnAceptarFecha.raise_()

        self.retranslateUi(modalFecha)

        QMetaObject.connectSlotsByName(modalFecha)
    # setupUi

    def retranslateUi(self, modalFecha):
        modalFecha.setWindowTitle(QCoreApplication.translate("modalFecha", u"D\u00edas Laborables", None))
        self.lbl1.setText(QCoreApplication.translate("modalFecha", u"Seleccione la fecha incial del proyecto:", None))
        self.lblFondoModal.setText("")
        self.grupoBotones.setTitle(QCoreApplication.translate("modalFecha", u"D\u00edas de la semana que no se trabajar\u00e1n:", None))
        self.checkLunes.setText(QCoreApplication.translate("modalFecha", u"Lunes", None))
        self.checkMartes.setText(QCoreApplication.translate("modalFecha", u"Martes", None))
        self.checkMier.setText(QCoreApplication.translate("modalFecha", u"Mi\u00e9rcoles", None))
        self.checkSabado.setText(QCoreApplication.translate("modalFecha", u"S\u00e1bado", None))
        self.checkViernes.setText(QCoreApplication.translate("modalFecha", u"Viernes", None))
        self.checkDom.setText(QCoreApplication.translate("modalFecha", u"Domingo", None))
        self.checkJueves.setText(QCoreApplication.translate("modalFecha", u"Jueves", None))
        self.btnAceptarFecha.setText(QCoreApplication.translate("modalFecha", u"Aceptar", None))
    # retranslateUi

