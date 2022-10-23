from base64 import decodebytes
from contextlib import redirect_stderr
from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene
from PySide2.QtCore import Slot
from PySide2.QtGui import QPen, QColor, QTransform
from ui_mainwindow import Ui_MainWindow
from particle_adminstrator import administrador
from particulas import Particula

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.administrador = administrador()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.agregarFinal_pushButton.clicked.connect(self.click_agregar)
        self.ui.AgragrInicio_pushButton.clicked.connect(self.click_agregar_inicio)
        self.ui.Mostrar_pushButton.clicked.connect(self.click_mostrar)

        self.ui.actionAbrir.triggered.connect(self.action_abrir_archivo)
        self.ui.actionGuardar.triggered.connect(self.action_guardar_archivo)

        self.ui.Mostrar_Tabla_pushButton_2.clicked.connect(self.mostrar_tabla)
        self.ui.buscar_pushButton.clicked.connect(self.Buscar)
        self.ui.Limpiar_pushButton_2.clicked.connect(self.Limpiar)
        self.ui.Dibujar_pushButton.clicked.connect(self.Dibujar)

        self.scene = QGraphicsScene()
        self.ui.Particulas_graphicsView.setScene(self.scene)
    
    @Slot()
    def Dibujar(self):
        # print('dibujando')
        Pen = QPen()
        Pen.setWidth(3)
        
        
        for particle in self.administrador:
            r = particle.Red
            g = particle.Green
            b = particle.Blue
            color = QColor(r, g, b)
            Pen.setColor(color)
            self.scene.addEllipse(particle.OrigenX,particle.OrigenY,3,3, Pen)
            self.scene.addEllipse(particle.DestinoX,particle.DestinoY,3,3, Pen)
            self.scene.addLine(particle.OrigenX, particle.OrigenY, particle.DestinoX, particle.DestinoY, Pen)


    
    @Slot()
    def Limpiar(self):
        self.scene.clear()

    @Slot()
    def Buscar(self):
        Codigo_Buscado = self.ui.Buscar_lineEdit.text()
        

        encontrado = False
        for particle in self.administrador:
            if Codigo_Buscado == str(particle.Codigo):
                self.ui.Tabla.clear()
                self.ui.Tabla.setRowCount(1)

                Codigo_Widget = QTableWidgetItem(str(particle.Codigo))
                OrigenesX_Widget = QTableWidgetItem(str(particle.OrigenX))
                OrigenesY_Widget = QTableWidgetItem(str(particle.OrigenY))
                DestinoX_Widget = QTableWidgetItem(str(particle.DestinoX))
                DestinoY_Widget = QTableWidgetItem(str(particle.DestinoY))
                Velocidad_Widget = QTableWidgetItem(str(particle.Velocidad))
                Red_Widget = QTableWidgetItem(str(particle.Red))
                Green_Widget = QTableWidgetItem(str(particle.Green))
                Blue_Widget = QTableWidgetItem(str(particle.Blue))
                Distancia_Widget = QTableWidgetItem(str(particle.Distancia))

                self.ui.Tabla.setItem(0, 0, Codigo_Widget)
                self.ui.Tabla.setItem(0, 1, OrigenesX_Widget)
                self.ui.Tabla.setItem(0, 2, OrigenesY_Widget)
                self.ui.Tabla.setItem(0, 3, DestinoX_Widget)
                self.ui.Tabla.setItem(0, 4, DestinoY_Widget)
                self.ui.Tabla.setItem(0, 5, Velocidad_Widget)
                self.ui.Tabla.setItem(0, 6, Red_Widget)
                self.ui.Tabla.setItem(0, 7, Green_Widget)
                self.ui.Tabla.setItem(0, 8, Blue_Widget)
                self.ui.Tabla.setItem(0, 9, Distancia_Widget)

                encontrado = True
                return
        print(Codigo_Buscado)
        if not encontrado:
            QMessageBox.warning(self,"Atencion", f'Particula "{Codigo_Buscado}"no encontrada')

    @Slot()
    def mostrar_tabla(self):
        self.ui.Tabla.setColumnCount(10)
        headers = ["ID" ,"Origen X" ,"Origen Y" ,"Destino X" ,"Destino Y" ,"Velocidad" ,"Red" ,"Green" ,"Blue" ,"Distancia"]
        self.ui.Tabla.setHorizontalHeaderLabels(headers)

        self.ui.Tabla.setRowCount(len(self.administrador))
        self.ui.Tabla.setColumnWidth(0,50)
        self.ui.Tabla.setColumnWidth(9,200)
        

        row = 0
        for particle in self.administrador:
            Codigo_Widget = QTableWidgetItem(str(particle.Codigo))
            OrigenesX_Widget = QTableWidgetItem(str(particle.OrigenX))
            OrigenesY_Widget = QTableWidgetItem(str(particle.OrigenY))
            DestinoX_Widget = QTableWidgetItem(str(particle.DestinoX))
            DestinoY_Widget = QTableWidgetItem(str(particle.DestinoY))
            Velocidad_Widget = QTableWidgetItem(str(particle.Velocidad))
            Red_Widget = QTableWidgetItem(str(particle.Red))
            Green_Widget = QTableWidgetItem(str(particle.Green))
            Blue_Widget = QTableWidgetItem(str(particle.Blue))
            Distancia_Widget = QTableWidgetItem(str(particle.Distancia))

            self.ui.Tabla.setItem(row, 0, Codigo_Widget)
            self.ui.Tabla.setItem(row, 1, OrigenesX_Widget)
            self.ui.Tabla.setItem(row, 2, OrigenesY_Widget)
            self.ui.Tabla.setItem(row, 3, DestinoX_Widget)
            self.ui.Tabla.setItem(row, 4, DestinoY_Widget)
            self.ui.Tabla.setItem(row, 5, Velocidad_Widget)
            self.ui.Tabla.setItem(row, 6, Red_Widget)
            self.ui.Tabla.setItem(row, 7, Green_Widget)
            self.ui.Tabla.setItem(row, 8, Blue_Widget)
            self.ui.Tabla.setItem(row, 9, Distancia_Widget)

            row += 1
            
    @Slot()
    def action_abrir_archivo(self):
        # print('Abriendo')
        ubicacion = QFileDialog.getOpenFileName(self, 'Abrir', '.', 'JSON (*.json)')[0]
        
        if self.administrador.abrir(ubicacion):
            QMessageBox.information(self, "Exito","Archivo Cargado de: " + ubicacion)
        else:
            QMessageBox.critical(self, "Error", "No se pudo cargar el archivo")
    
    @Slot()
    def action_guardar_archivo(self):
        # print('Guardando')
        ubicacion = QFileDialog.getSaveFileName(self, 'Guardar', '.', 'JSON (*.json)')[0]
        print(ubicacion)
        if self.administrador.guardar(ubicacion):
            QMessageBox.information(self, "Exito","Archivo Guardado en: " + ubicacion)
        else:
            QMessageBox.critical(self, "Error","No se pudo guardar el archivo")

    @Slot()
    def click_mostrar(self):
        # self.administrador.mostrar()
        self.ui.salida.clear()
        self.ui.salida.insertPlainText(str(self.administrador))

    @Slot()
    def click_agregar_inicio(self):
        codigo = self.ui.ID_pinBox.value()
        OrigX = self.ui.OrigenX_spinBox.value()
        OrigY = self.ui.OrigenY_spinBox_2.value()
        desX = self.ui.DesX_pinBox.value()
        desY = self.ui.DesY_spinBox_2.value()
        velocidad = self.ui.Velocidad_spinBox_3.value()
        red = self.ui.Red_spinBox_4.value()
        green = self.ui.Green_spinBox_5.value()
        blue = self.ui.Blue_spinBox_6.value()

        Particle = Particula(id=codigo, origen_x=OrigX, origen_y=OrigY,destino_x=desX, destino_y=desY, velocidad=velocidad, red=red, green=green, blue=blue)
        self.administrador.agregar_incio(Particle)
    
    @Slot()
    def click_agregar(self):
        codigo = self.ui.ID_pinBox.value()
        OrigX = self.ui.OrigenX_spinBox.value()
        OrigY = self.ui.OrigenY_spinBox_2.value()
        desX = self.ui.DesX_pinBox.value()
        desY = self.ui.DesY_spinBox_2.value()
        velocidad = self.ui.Velocidad_spinBox_3.value()
        red = self.ui.Red_spinBox_4.value()
        green = self.ui.Green_spinBox_5.value()
        blue = self.ui.Blue_spinBox_6.value()

        Particle = Particula(id=codigo, origen_x=OrigX, origen_y=OrigY, destino_x=desX, destino_y=desY, velocidad=velocidad, red=red, green=green, blue=blue)
        self.administrador.agregar_final(Particle)

        
