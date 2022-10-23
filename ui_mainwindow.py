# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1285, 630)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 10, 1261, 571))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.salida = QPlainTextEdit(self.tab)
        self.salida.setObjectName(u"salida")
        self.salida.setGeometry(QRect(80, 310, 251, 161))
        self.Mostrar_pushButton = QPushButton(self.tab)
        self.Mostrar_pushButton.setObjectName(u"Mostrar_pushButton")
        self.Mostrar_pushButton.setGeometry(QRect(80, 510, 241, 23))
        self.groupBox_3 = QGroupBox(self.tab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(140, 250, 120, 51))
        self.widget = QWidget(self.groupBox_3)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 20, 102, 22))
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.Velocidad_spinBox_3 = QSpinBox(self.widget)
        self.Velocidad_spinBox_3.setObjectName(u"Velocidad_spinBox_3")
        self.Velocidad_spinBox_3.setMaximum(1000)

        self.horizontalLayout_4.addWidget(self.Velocidad_spinBox_3)

        self.Particulas_graphicsView = QGraphicsView(self.tab)
        self.Particulas_graphicsView.setObjectName(u"Particulas_graphicsView")
        self.Particulas_graphicsView.setGeometry(QRect(350, 40, 881, 431))
        self.widget1 = QWidget(self.tab)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(160, 10, 80, 22))
        self.horizontalLayout_2 = QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.widget1)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_2.addWidget(self.label_7)

        self.ID_pinBox = QSpinBox(self.widget1)
        self.ID_pinBox.setObjectName(u"ID_pinBox")
        self.ID_pinBox.setMaximum(500000)

        self.horizontalLayout_2.addWidget(self.ID_pinBox)

        self.widget2 = QWidget(self.tab)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(80, 40, 251, 201))
        self.verticalLayout = QVBoxLayout(self.widget2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox_4 = QGroupBox(self.widget2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.widget3 = QWidget(self.groupBox_4)
        self.widget3.setObjectName(u"widget3")
        self.widget3.setGeometry(QRect(10, 20, 176, 22))
        self.horizontalLayout_5 = QHBoxLayout(self.widget3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.widget3)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_5.addWidget(self.label_8)

        self.OrigenX_spinBox = QSpinBox(self.widget3)
        self.OrigenX_spinBox.setObjectName(u"OrigenX_spinBox")

        self.horizontalLayout_5.addWidget(self.OrigenX_spinBox)

        self.label_9 = QLabel(self.widget3)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_5.addWidget(self.label_9)

        self.OrigenY_spinBox_2 = QSpinBox(self.widget3)
        self.OrigenY_spinBox_2.setObjectName(u"OrigenY_spinBox_2")

        self.horizontalLayout_5.addWidget(self.OrigenY_spinBox_2)


        self.verticalLayout.addWidget(self.groupBox_4)

        self.groupBox = QGroupBox(self.widget2)
        self.groupBox.setObjectName(u"groupBox")
        self.widget4 = QWidget(self.groupBox)
        self.widget4.setObjectName(u"widget4")
        self.widget4.setGeometry(QRect(10, 20, 196, 22))
        self.horizontalLayout_3 = QHBoxLayout(self.widget4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget4)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.DesX_pinBox = QSpinBox(self.widget4)
        self.DesX_pinBox.setObjectName(u"DesX_pinBox")
        self.DesX_pinBox.setMaximum(500)

        self.horizontalLayout_3.addWidget(self.DesX_pinBox)

        self.label_2 = QLabel(self.widget4)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.DesY_spinBox_2 = QSpinBox(self.widget4)
        self.DesY_spinBox_2.setObjectName(u"DesY_spinBox_2")
        self.DesY_spinBox_2.setMaximum(500)

        self.horizontalLayout_3.addWidget(self.DesY_spinBox_2)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.widget2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.widget5 = QWidget(self.groupBox_2)
        self.widget5.setObjectName(u"widget5")
        self.widget5.setGeometry(QRect(10, 20, 229, 22))
        self.horizontalLayout = QHBoxLayout(self.widget5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.widget5)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.Red_spinBox_4 = QSpinBox(self.widget5)
        self.Red_spinBox_4.setObjectName(u"Red_spinBox_4")
        self.Red_spinBox_4.setMaximum(255)

        self.horizontalLayout.addWidget(self.Red_spinBox_4)

        self.label_5 = QLabel(self.widget5)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout.addWidget(self.label_5)

        self.Green_spinBox_5 = QSpinBox(self.widget5)
        self.Green_spinBox_5.setObjectName(u"Green_spinBox_5")
        self.Green_spinBox_5.setMaximum(255)

        self.horizontalLayout.addWidget(self.Green_spinBox_5)

        self.label_6 = QLabel(self.widget5)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout.addWidget(self.label_6)

        self.Blue_spinBox_6 = QSpinBox(self.widget5)
        self.Blue_spinBox_6.setObjectName(u"Blue_spinBox_6")
        self.Blue_spinBox_6.setMaximum(255)

        self.horizontalLayout.addWidget(self.Blue_spinBox_6)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.widget6 = QWidget(self.tab)
        self.widget6.setObjectName(u"widget6")
        self.widget6.setGeometry(QRect(80, 480, 241, 25))
        self.horizontalLayout_6 = QHBoxLayout(self.widget6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.AgragrInicio_pushButton = QPushButton(self.widget6)
        self.AgragrInicio_pushButton.setObjectName(u"AgragrInicio_pushButton")

        self.horizontalLayout_6.addWidget(self.AgragrInicio_pushButton)

        self.agregarFinal_pushButton = QPushButton(self.widget6)
        self.agregarFinal_pushButton.setObjectName(u"agregarFinal_pushButton")

        self.horizontalLayout_6.addWidget(self.agregarFinal_pushButton)

        self.widget7 = QWidget(self.tab)
        self.widget7.setObjectName(u"widget7")
        self.widget7.setGeometry(QRect(380, 490, 311, 25))
        self.horizontalLayout_7 = QHBoxLayout(self.widget7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.Dibujar_pushButton = QPushButton(self.widget7)
        self.Dibujar_pushButton.setObjectName(u"Dibujar_pushButton")

        self.horizontalLayout_7.addWidget(self.Dibujar_pushButton)

        self.Limpiar_pushButton_2 = QPushButton(self.widget7)
        self.Limpiar_pushButton_2.setObjectName(u"Limpiar_pushButton_2")

        self.horizontalLayout_7.addWidget(self.Limpiar_pushButton_2)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout = QGridLayout(self.tab_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Tabla = QTableWidget(self.tab_2)
        self.Tabla.setObjectName(u"Tabla")

        self.gridLayout.addWidget(self.Tabla, 0, 0, 1, 3)

        self.Buscar_lineEdit = QLineEdit(self.tab_2)
        self.Buscar_lineEdit.setObjectName(u"Buscar_lineEdit")

        self.gridLayout.addWidget(self.Buscar_lineEdit, 1, 0, 1, 1)

        self.buscar_pushButton = QPushButton(self.tab_2)
        self.buscar_pushButton.setObjectName(u"buscar_pushButton")

        self.gridLayout.addWidget(self.buscar_pushButton, 1, 1, 1, 1)

        self.Mostrar_Tabla_pushButton_2 = QPushButton(self.tab_2)
        self.Mostrar_Tabla_pushButton_2.setObjectName(u"Mostrar_Tabla_pushButton_2")

        self.gridLayout.addWidget(self.Mostrar_Tabla_pushButton_2, 1, 2, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1285, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionAbrir)
        self.menuFile.addAction(self.actionGuardar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.Mostrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Velocidad", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Velocidad:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Origenes", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Origen X:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Origen Y:", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Destino", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Destino X:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Destino Y:", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Colores", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Red:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Green:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Blue:", None))
        self.AgragrInicio_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar al Inicio", None))
        self.agregarFinal_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar al final", None))
        self.Dibujar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.Limpiar_pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.Buscar_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.buscar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.Mostrar_Tabla_pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Mostra", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

