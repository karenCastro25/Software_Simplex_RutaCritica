from PyQt5.Qt import QAbstractItemModel, QApplication, QBrush, QColor, QComboBox, QStyleFactory, QTableWidgetItem
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import uic
from PyQt5.QtGui import QIcon
import os
import sys

#Importacion de clases
import ClassSimplex
import ClassCPM
import Fraccion


from PyQt5.QtCore import QObject

from interfaz.ui_Programa import Ui_MainWindow



class VentanaPrincipal(QMainWindow):
    
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ventPert = ClassCPM.ClassCPM(self.ui)
        self.ventSimplex = ClassSimplex.ClassSimplex(self.ui)
        self.eventosFrame()
    
    def eventosFrame(self):
        self.ui.menuSimplex.aboutToShow.connect(self.cargarFrame)
        self.ui.menuCPM.aboutToShow.connect(self.cargarFrame)
            
    def cargarFrame(self):
        ventana = self.sender()

        if ventana == self.ui.menuCPM:
            self.ui.frameSimplex.setVisible(False)
            self.ui.frameCPM.setVisible(True)
       
        else:      
            self.ui.frameCPM.setVisible(False)
            self.ui.frameSimplex.setVisible(True)
           

    def resolver_direccion(self, ruta_relativa):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, ruta_relativa)
        return os.path.join(os.path.abspath('.'), ruta_relativa)



 


# Inicia la aplicación
if __name__ == '__main__':
    app = QApplication([])
    app.setStyle(QStyleFactory.create('Fusion'))
    mi_App = VentanaPrincipal()
    dirIcono = mi_App.resolver_direccion("interfaz/img/logo.ico")
    mi_App.setWindowIcon(QIcon(dirIcono))
    
    mi_App.show()
    sys.exit(app.exec_())
