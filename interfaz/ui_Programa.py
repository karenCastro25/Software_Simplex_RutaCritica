# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ProgramaSimplexPERTurrkgv.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(937, 504)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QSize(1024, 720))
        MainWindow.setSizeIncrement(QSize(0, 0))
        MainWindow.setStyleSheet(u"background: #FEFEFE; font-size: 14px; font-weight: bold; font-family: Roboto;\n"
"")
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.actionPrueba = QAction(MainWindow)
        self.actionPrueba.setObjectName(u"actionPrueba")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setStyleSheet(u"padding:0px;")
        self.frameCPM = QFrame(self.centralwidget)
        self.frameCPM.setObjectName(u"frameCPM")
        self.frameCPM.setGeometry(QRect(0, 0, 1341, 821))
        self.frameCPM.setFrameShape(QFrame.StyledPanel)
        self.frameCPM.setFrameShadow(QFrame.Raised)
        self.lblnumActividades = QLabel(self.frameCPM)
        self.lblnumActividades.setObjectName(u"lblnumActividades")
        self.lblnumActividades.setGeometry(QRect(20, 30, 191, 31))
        self.lblnumActividades.setStyleSheet(u"  background: rgba(37, 40,80,0);\n"
"color: rgb(37, 40,80);\n"
"font-size: 12px; ")
        self.lblFondoPert = QLabel(self.frameCPM)
        self.lblFondoPert.setObjectName(u"lblFondoPert")
        self.lblFondoPert.setGeometry(QRect(0, 0, 1031, 731))
        self.lblFondoPert.setStyleSheet(u"background-image: url(\"interfaz/img/fondoPert.png\");")
        self.btnGenerarTbl = QPushButton(self.frameCPM)
        self.btnGenerarTbl.setObjectName(u"btnGenerarTbl")
        self.btnGenerarTbl.setGeometry(QRect(290, 30, 111, 31))
        self.btnGenerarTbl.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnGenerarTbl.setStyleSheet(u"font-size: 12px; font-weight: bold; font-family: Open Sans; color: #009999;\n"
"background: rgb(37, 40,80);\n"
"border-radius: 10px;\n"
"color : rgb(255,255,255)")
        self.spinNumActividades = QSpinBox(self.frameCPM)
        self.spinNumActividades.setObjectName(u"spinNumActividades")
        self.spinNumActividades.setGeometry(QRect(220, 30, 51, 31))
        self.spinNumActividades.setStyleSheet(u"font-size: 14px; \n"
" font-weight: bold; font-family: Kameron;")
        self.tblActividades = QTableWidget(self.frameCPM)
        self.tblActividades.setObjectName(u"tblActividades")
        self.tblActividades.setGeometry(QRect(20, 90, 891, 261))
        self.tblActividades.setStyleSheet(u"font-size: 12px; font-weight: bold;\n"
"color: rgba(0,0,0);\n"
"background: rgb(255, 255,255);\n"
"self.tblVariables.horizontalHeader().setStyleSheet(\"color: #fff\")\n"
"self.tblVariables.setStyleSheet(\"border: none;\")")
        self.tblActividades.horizontalHeader().setVisible(True)
        self.tblActividades.horizontalHeader().setDefaultSectionSize(50)
        self.tblActividades.verticalHeader().setVisible(False)
        self.btnCalcularPert = QPushButton(self.frameCPM)
        self.btnCalcularPert.setObjectName(u"btnCalcularPert")
        self.btnCalcularPert.setGeometry(QRect(490, 30, 141, 31))
        self.btnCalcularPert.setStyleSheet(u"font-size: 12px; font-weight: bold; font-family: Open Sans; color: #009999;\n"
"background: rgb(37, 40,80);\n"
"border-radius: 10px;\n"
"color : rgb(255,255,255)")
        self.btnNuevoPert = QPushButton(self.frameCPM)
        self.btnNuevoPert.setObjectName(u"btnNuevoPert")
        self.btnNuevoPert.setGeometry(QRect(640, 30, 131, 31))
        self.btnNuevoPert.setStyleSheet(u"font-size: 12px; font-weight: bold; font-family: Open Sans; color: #009999;\n"
"background: rgb(37, 40,80);\n"
"border-radius: 10px;\n"
"color : rgb(255,255,255)")
        self.lblnumActividades_3 = QLabel(self.frameCPM)
        self.lblnumActividades_3.setObjectName(u"lblnumActividades_3")
        self.lblnumActividades_3.setGeometry(QRect(20, 420, 101, 31))
        self.lblnumActividades_3.setStyleSheet(u"  background: rgba(37, 40,80,0);\n"
"color: rgb(37, 40,80);\n"
"font-size: 12px; ")
        self.lblFechaIncio = QLabel(self.frameCPM)
        self.lblFechaIncio.setObjectName(u"lblFechaIncio")
        self.lblFechaIncio.setGeometry(QRect(140, 380, 141, 31))
        self.lblFechaIncio.setStyleSheet(u" font-weight: bold; font-family: Kameron;\n"
"background: rgba(255, 255,255,0);\n"
"color: #F44336;\n"
"font-size: 14px; ")
        self.lblFechaFin = QLabel(self.frameCPM)
        self.lblFechaFin.setObjectName(u"lblFechaFin")
        self.lblFechaFin.setGeometry(QRect(140, 420, 131, 31))
        self.lblFechaFin.setStyleSheet(u" font-weight: bold; font-family: Kameron;\n"
"background: rgba(255, 255,255,0);\n"
"color: #F44336;\n"
"font-size: 14px; ")
        self.lblFindes = QLabel(self.frameCPM)
        self.lblFindes.setObjectName(u"lblFindes")
        self.lblFindes.setGeometry(QRect(310, 370, 591, 91))
        self.lblFindes.setStyleSheet(u" font-weight: bold; font-family: Kameron;\n"
"background: rgba(255, 255,255,0);\n"
"color: #F44336;\n"
"font-size: 14px; ")
        self.lblFindes.setWordWrap(True)
        self.lblnumActividades_2 = QLabel(self.frameCPM)
        self.lblnumActividades_2.setObjectName(u"lblnumActividades_2")
        self.lblnumActividades_2.setGeometry(QRect(20, 380, 111, 31))
        self.lblnumActividades_2.setStyleSheet(u"  background: rgba(37, 40,80,0);\n"
"color: rgb(37, 40,80);\n"
"font-size: 12px; ")
        self.lblFondoPert.raise_()
        self.lblnumActividades.raise_()
        self.btnGenerarTbl.raise_()
        self.spinNumActividades.raise_()
        self.tblActividades.raise_()
        self.btnCalcularPert.raise_()
        self.btnNuevoPert.raise_()
        self.lblnumActividades_3.raise_()
        self.lblFechaIncio.raise_()
        self.lblFechaFin.raise_()
        self.lblFindes.raise_()
        self.lblnumActividades_2.raise_()
        self.frameSimplex = QFrame(self.centralwidget)
        self.frameSimplex.setObjectName(u"frameSimplex")
        self.frameSimplex.setGeometry(QRect(0, 0, 1031, 691))
        self.frameSimplex.setFrameShape(QFrame.StyledPanel)
        self.frameSimplex.setFrameShadow(QFrame.Raised)
        self.lblFondo = QLabel(self.frameSimplex)
        self.lblFondo.setObjectName(u"lblFondo")
        self.lblFondo.setGeometry(QRect(-80, 0, 1111, 561))
        self.lblFondo.setStyleSheet(u"")
        self.lblVarriables = QLabel(self.frameSimplex)
        self.lblVarriables.setObjectName(u"lblVarriables")
        self.lblVarriables.setGeometry(QRect(10, 20, 191, 31))
        self.lblVarriables.setStyleSheet(u"  background: rgba(37, 40,80,0);\n"
"color: rgb(37, 40,80);\n"
"font-size: 12px; ")
        self.btnGenerar = QPushButton(self.frameSimplex)
        self.btnGenerar.setObjectName(u"btnGenerar")
        self.btnGenerar.setGeometry(QRect(106, 101, 101, 31))
        font = QFont()
        font.setFamily(u"Open Sans")
        font.setBold(True)
        font.setWeight(75)
        self.btnGenerar.setFont(font)
        self.btnGenerar.setStyleSheet(u"font-size: 12px; font-weight: bold; font-family: Open Sans;\n"
"background: rgb(37, 40,80);\n"
"border-radius: 10px;\n"
"color : rgb(255,255,255)")
        self.lblRestricciones = QLabel(self.frameSimplex)
        self.lblRestricciones.setObjectName(u"lblRestricciones")
        self.lblRestricciones.setGeometry(QRect(10, 60, 201, 31))
        self.lblRestricciones.setStyleSheet(u"  background: rgba(37, 40,80,0);\n"
"color: rgb(37, 40,80);\n"
"font-size: 12px; ")
        self.panelVarRest = QFrame(self.frameSimplex)
        self.panelVarRest.setObjectName(u"panelVarRest")
        self.panelVarRest.setGeometry(QRect(10, 150, 311, 381))
        self.panelVarRest.setCursor(QCursor(Qt.PointingHandCursor))
        self.panelVarRest.setStyleSheet(u"background: rgba(255, 255,255,0);\n"
"self.panelVarRest.setStyleSheet(\"border: none\")\n"
"")
        self.panelVarRest.setFrameShape(QFrame.NoFrame)
        self.panelVarRest.setFrameShadow(QFrame.Raised)
        self.panelVarRest.setLineWidth(0)
        self.tblVariables = QTableWidget(self.panelVarRest)
        self.tblVariables.setObjectName(u"tblVariables")
        self.tblVariables.setGeometry(QRect(10, 30, 281, 61))
        self.tblVariables.setStyleSheet(u"font-size: 12px; font-weight: bold;\n"
"color: rgba(0,0,0);\n"
"background: rgb(255, 255,255);\n"
"self.tblVariables.horizontalHeader().setStyleSheet(\"color: #fff\")\n"
"self.tblVariables.setStyleSheet(\"border: none;\")")
        self.tblVariables.horizontalHeader().setVisible(True)
        self.tblVariables.horizontalHeader().setDefaultSectionSize(50)
        self.tblVariables.verticalHeader().setVisible(False)
        self.tblRestricciones = QTableWidget(self.panelVarRest)
        self.tblRestricciones.setObjectName(u"tblRestricciones")
        self.tblRestricciones.setGeometry(QRect(10, 120, 281, 131))
        self.tblRestricciones.setStyleSheet(u"font-size: 12px; font-weight: bold;\n"
"color: rgba(0,0,0);\n"
"background: rgb(255, 255,255);\n"
"self.tblVariables.horizontalHeader().setStyleSheet(\"color: #fff\")\n"
"self.tblVariables.setStyleSheet(\"border: none;\")")
        self.tblRestricciones.horizontalHeader().setVisible(True)
        self.tblRestricciones.horizontalHeader().setDefaultSectionSize(50)
        self.tblRestricciones.verticalHeader().setVisible(False)
        self.label_3 = QLabel(self.panelVarRest)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 0, 111, 30))
        self.label_3.setStyleSheet(u"  background: rgba(37, 40,80,0);\n"
"color: rgb(37, 40,80);\n"
"font-size: 12px; ")
        self.label_4 = QLabel(self.panelVarRest)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 100, 141, 16))
        self.label_4.setStyleSheet(u"  background: rgba(37, 40,80,0);\n"
"color: rgb(37, 40,80);\n"
"font-size: 12px; ")
        self.btnCalcular = QPushButton(self.panelVarRest)
        self.btnCalcular.setObjectName(u"btnCalcular")
        self.btnCalcular.setGeometry(QRect(97, 270, 101, 31))
        self.btnCalcular.setStyleSheet(u"font-size: 12px; font-weight: bold; font-family: Open Sans; color: #009999;\n"
"background: rgb(37, 40,80);\n"
"border-radius: 10px;\n"
"color : rgb(255,255,255)")
        self.lblFuncionObjetivo = QLabel(self.frameSimplex)
        self.lblFuncionObjetivo.setObjectName(u"lblFuncionObjetivo")
        self.lblFuncionObjetivo.setGeometry(QRect(450, 30, 461, 31))
        self.lblFuncionObjetivo.setStyleSheet(u"  background: rgba(37, 40,80,0);\n"
"color: #F44336;\n"
"font-size: 12px; ")
        self.lblFunObj = QLabel(self.frameSimplex)
        self.lblFunObj.setObjectName(u"lblFunObj")
        self.lblFunObj.setGeometry(QRect(340, 30, 111, 31))
        self.lblFunObj.setStyleSheet(u"  background: rgba(37, 40,80,0);\n"
"color: rgb(37, 40,80);\n"
"font-size: 12px; ")
        self.panelTblU = QFrame(self.frameSimplex)
        self.panelTblU.setObjectName(u"panelTblU")
        self.panelTblU.setEnabled(True)
        self.panelTblU.setGeometry(QRect(340, 70, 591, 371))
        self.panelTblU.setStyleSheet(u"  background: rgba(255, 255,255,0);")
        self.panelTblU.setFrameShape(QFrame.NoFrame)
        self.panelTblU.setFrameShadow(QFrame.Raised)
        self.tbl_U = QTableWidget(self.panelTblU)
        self.tbl_U.setObjectName(u"tbl_U")
        self.tbl_U.setGeometry(QRect(10, 80, 551, 271))
        self.tbl_U.setStyleSheet(u"font-size: 12px; font-weight: bold;\n"
"color: rgba(0,0,0);\n"
"background: rgb(255, 255,255);\n"
"self.tblVariables.horizontalHeader().setStyleSheet(\"color: #fff\")\n"
"self.tblVariables.setStyleSheet(\"border: none;\")")
        self.tbl_U.horizontalHeader().setVisible(False)
        self.tbl_U.horizontalHeader().setDefaultSectionSize(75)
        self.tbl_U.verticalHeader().setVisible(False)
        self.btnIteracion = QPushButton(self.panelTblU)
        self.btnIteracion.setObjectName(u"btnIteracion")
        self.btnIteracion.setGeometry(QRect(180, 20, 121, 31))
        self.btnIteracion.setStyleSheet(u"font-size: 12px; font-weight: bold; font-family: Open Sans; color: #009999;\n"
"background: rgb(37, 40,80);\n"
"border-radius: 10px;\n"
"color : rgb(255,255,255)")
        self.btnPdf = QPushButton(self.panelTblU)
        self.btnPdf.setObjectName(u"btnPdf")
        self.btnPdf.setGeometry(QRect(310, 20, 111, 31))
        self.btnPdf.setStyleSheet(u"font-size: 12px; font-weight: bold; font-family: Open Sans; color: #009999;\n"
"background: rgb(37, 40,80);\n"
"border-radius: 10px;\n"
"color : rgb(255,255,255)")
        self.lblIteracionTexto = QLabel(self.panelTblU)
        self.lblIteracionTexto.setObjectName(u"lblIteracionTexto")
        self.lblIteracionTexto.setGeometry(QRect(10, 20, 81, 31))
        self.lblIteracionTexto.setStyleSheet(u"  background: rgba(37, 40,80,0);\n"
"color: rgb(37, 40,80);\n"
"font-size: 12px; ")
        self.lblIteracion = QLabel(self.panelTblU)
        self.lblIteracion.setObjectName(u"lblIteracion")
        self.lblIteracion.setGeometry(QRect(100, 20, 55, 31))
        self.lblIteracion.setStyleSheet(u"  background: rgba(37, 40,80,0);\n"
"color: #F44336;\n"
"font-size: 12px; ")
        self.txtVar = QSpinBox(self.frameSimplex)
        self.txtVar.setObjectName(u"txtVar")
        self.txtVar.setGeometry(QRect(254, 20, 41, 31))
        self.txtRestr = QSpinBox(self.frameSimplex)
        self.txtRestr.setObjectName(u"txtRestr")
        self.txtRestr.setGeometry(QRect(253, 60, 42, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 937, 23))
        self.menuSimplex = QMenu(self.menubar)
        self.menuSimplex.setObjectName(u"menuSimplex")
        self.menuCPM = QMenu(self.menubar)
        self.menuCPM.setObjectName(u"menuCPM")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuSimplex.menuAction())
        self.menubar.addAction(self.menuCPM.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"M\u00e9todo Simplex y Metodo Ruta cr\u00edtica", None))
        self.actionPrueba.setText(QCoreApplication.translate("MainWindow", u"Prueba", None))
        self.lblnumActividades.setText(QCoreApplication.translate("MainWindow", u"Ingresar el n\u00famero de actividades:", None))
        self.lblFondoPert.setText("")
        self.btnGenerarTbl.setText(QCoreApplication.translate("MainWindow", u"Crear Tabla", None))
        self.btnCalcularPert.setText(QCoreApplication.translate("MainWindow", u"Calcular Ruta Cr\u00edtica", None))
        self.btnNuevoPert.setText(QCoreApplication.translate("MainWindow", u"Nueva Tabla", None))
        self.lblnumActividades_3.setText(QCoreApplication.translate("MainWindow", u"Hasta fecha fin:", None))
        self.lblFechaIncio.setText(QCoreApplication.translate("MainWindow", u"13/08/2021", None))
        self.lblFechaFin.setText(QCoreApplication.translate("MainWindow", u"15/09/2021", None))
        self.lblFindes.setText(QCoreApplication.translate("MainWindow", u"Pasaron X dias sin tomar en cuenta sabados y domingos", None))
        self.lblnumActividades_2.setText(QCoreApplication.translate("MainWindow", u"Desde fecha inicio:", None))
        self.lblFondo.setText("")
        self.lblVarriables.setText(QCoreApplication.translate("MainWindow", u"Ingrese el n\u00famero de variables:", None))
        self.btnGenerar.setText(QCoreApplication.translate("MainWindow", u"Crear Tablas", None))
        self.lblRestricciones.setText(QCoreApplication.translate("MainWindow", u"Ingrese el n\u00famero de restricciones:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Funci\u00f3n Objetivo", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Tabla Restricciones", None))
        self.btnCalcular.setText(QCoreApplication.translate("MainWindow", u"Crear Tabla U", None))
        self.lblFuncionObjetivo.setText("")
        self.lblFunObj.setText(QCoreApplication.translate("MainWindow", u"Funcion Objetivo: ", None))
        self.btnIteracion.setText(QCoreApplication.translate("MainWindow", u"Iteraci\u00f3n", None))
        self.btnPdf.setText(QCoreApplication.translate("MainWindow", u"Exportar a PDF", None))
        self.lblIteracionTexto.setText(QCoreApplication.translate("MainWindow", u"Iteraci\u00f3n N#: ", None))
        self.lblIteracion.setText("")
        self.menuSimplex.setTitle(QCoreApplication.translate("MainWindow", u"Calculadora M\u00e9todo Simplex", None))
        self.menuCPM.setTitle(QCoreApplication.translate("MainWindow", u"M\u00e9todo ruta critica CPM", None))
    # retranslateUi






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())