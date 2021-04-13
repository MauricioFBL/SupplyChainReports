from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QDoubleValidator
import pandas as pd
import numpy as np
# import datetime
# from functools import partial
from datetime import datetime, timedelta
import sys
if not sys.warnoptions:
        import warnings
        warnings.simplefilter("ignore")
class Ui_MainWindow(object):
    global fileName_
    global df_
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(614, 301)
        MainWindow.setMaximumSize(QtCore.QSize(614, 301))
        MainWindow.setMinimumSize(QtCore.QSize(614, 301))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../Downloads/a-b-c1.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(255, 166, 171);")
        MainWindow.setIconSize(QtCore.QSize(26, 26))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 591, 271))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 230, 141, 31))
        self.pushButton_2.setStyleSheet("color: rgb(255, 255, 255);\n"
        "alternate-background-color: rgba(255, 0, 0, 215);\n"
        "font: 75 bold 10pt \"MS Shell Dlg 2\";\n"
        "background-color: rgba(255, 4, 4, 213);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 37, 541, 171))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
        "alternate-background-color: rgba(255, 0, 0, 215);\n"
        "font: 75 bold 10pt \"MS Shell Dlg 2\";\n"
        "background-color: rgba(255, 4, 4, 213);")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line_4 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout.addWidget(self.line_4)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setStyleSheet("font: 75 bold 10pt \"Consolas\";")
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.line_6 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.horizontalLayout_4.addWidget(self.line_6)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setStyleSheet("font: 75 bold 10pt \"Consolas\";")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout_2.addWidget(self.comboBox_2)
        self.line_2 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_2.addWidget(self.line_2)
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox.setStyleSheet("")
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.line_5 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout.addWidget(self.line_5)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.line_7 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.horizontalLayout_5.addWidget(self.line_7)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setStyleSheet("font: 75 bold 10pt \"Consolas\";")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setStyleSheet("font: 75 bold 10pt \"Consolas\";")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.verticalLayoutWidget)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.horizontalLayout_3.addWidget(self.dateEdit_2)
        self.line_3 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_3.addWidget(self.line_3)
        self.dateEdit = QtWidgets.QDateEdit(self.verticalLayoutWidget)
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setStyleSheet("QDateEdit { \n"
                                    "padding-right: 5px;\n"
                                    "padding-left: 5px;\n"
                                    "font: 75 10pt \"Arial\";\n"
                                    "color:#000; \n"
                                    "border-radius: 8px;\n"
                                    "border: 2px solid gray\n"
                                    "}\n"
                                    "QDateEdit QCalendarWidget QToolButton {\n"
                                    "height: 20px;\n"
                                    "width: 70px;\n"
                                    "color: white;\n"
                                    "font: 75 10pt \"Arial\";\n"
                                    "background-color:qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 rgb(213,29,63));\n"
                                    "}\n"
                                    "QDateEdit  QCalendarWidget QMenu {\n"
                                    "width: 100px;\n"
                                    "left: 5px;\n"
                                    "color: white;\n"
                                    "font: 75 10pt \"Arial\";\n"
                                    "background-color: rgb(213, 29, 63);\n"
                                    "}\n"
                                    "QDateEdit  QCalendarWidget QSpinBox {\n"
                                    "width: 70px;\n"
                                    "font: 75 12pt \"Arial\";\n"
                                    "color: white;\n"
                                    "background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 rgb(213,29,63));\n"
                                    "selection-background-color: rgb(136, 136, 136);\n"
                                    "selection-color: rgb(255, 255, 255);\n"
                                    "}\n"
                                    "\n"
                                    "QDateEdit  QCalendarWidget QSpinBox::up-button { subcontrol-origin: border; subcontrol-position: top right; width:20px; }\n"
                                    "QCalendarWidget QSpinBox::down-button {subcontrol-origin: border;  subcontrol-position: bottom right; width:20px;}\n"
                                    "QCalendarWidget QSpinBox::up-arrow { width:56px; height:56px; }\n"
                                    "QCalendarWidget QSpinBox::down-arrow { width:56px; height:56px; }\n"
                                    "QDateEdit  QCalendarWidget QAbstractItemView:enabled\n"
                                    "{\n"
                                    "font: 75 8pt \"Arial\";\n"
                                    "selection-background-color: rgb(213,29,62);\n"
                                    "selection-color: rgb(255, 255, 255);\n"
                                    "}\n"
                                    "QDateEdit  QCalendarWidget QWidget \n"
                                    "{\n"
                                    " alternate-background-color: rgba(213,29,62, 40); \n"
                                    "}\n"
                                    "QDateEdit  QCalendarWidget QToolButton#qt_calendar_prevmonth \n"
                                    "{\n"
                                    "    qproperty-icon: url(back.png);\n"
                                    "}\n"
                                    "QDateEdit  QCalendarWidget QToolButton#qt_calendar_nextmonth \n"
                                    "{\n"
                                    "    qproperty-icon: url(forward.png);\n"
                                    "}\n"
                                    "QCalendarWidget QWidget#qt_calendar_navigationbar\n"
                                    "{ \n"
                                    "  background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 rgb(213,29,62)); \n"
                                    "}")
        self.dateEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.dateEdit.setSpecialValueText("")
        self.dateEdit.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QtCore.QDate(2020, 1, 1))
        self.dateEdit_2.setStyleSheet("QDateEdit { \n"
                                    "padding-right: 5px;\n"
                                    "padding-left: 5px;\n"
                                    "font: 75 10pt \"Arial\";\n"
                                    "color:#000; \n"
                                    "border-radius: 8px;\n"
                                    "border: 2px solid gray\n"
                                    "}\n"
                                    "QDateEdit QCalendarWidget QToolButton {\n"
                                    "height: 20px;\n"
                                    "width: 70px;\n"
                                    "color: white;\n"
                                    "font: 75 10pt \"Arial\";\n"
                                    "background-color:qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 rgb(213,29,63));\n"
                                    "}\n"
                                    "QDateEdit  QCalendarWidget QMenu {\n"
                                    "width: 100px;\n"
                                    "left: 5px;\n"
                                    "color: white;\n"
                                    "font: 75 10pt \"Arial\";\n"
                                    "background-color: rgb(213, 29, 63);\n"
                                    "}\n"
                                    "QDateEdit  QCalendarWidget QSpinBox {\n"
                                    "width: 70px;\n"
                                    "font: 75 12pt \"Arial\";\n"
                                    "color: white;\n"
                                    "background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 rgb(213,29,63));\n"
                                    "selection-background-color: rgb(136, 136, 136);\n"
                                    "selection-color: rgb(255, 255, 255);\n"
                                    "}\n"
                                    "\n"
                                    "QDateEdit  QCalendarWidget QSpinBox::up-button { subcontrol-origin: border; subcontrol-position: top right; width:20px; }\n"
                                    "QCalendarWidget QSpinBox::down-button {subcontrol-origin: border;  subcontrol-position: bottom right; width:20px;}\n"
                                    "QCalendarWidget QSpinBox::up-arrow { width:56px; height:56px; }\n"
                                    "QCalendarWidget QSpinBox::down-arrow { width:56px; height:56px; }\n"
                                    "QDateEdit  QCalendarWidget QAbstractItemView:enabled\n"
                                    "{\n"
                                    "font: 75 8pt \"Arial\";\n"
                                    "selection-background-color: rgb(213,29,62);\n"
                                    "selection-color: rgb(255, 255, 255);\n"
                                    "}\n"
                                    "QDateEdit  QCalendarWidget QWidget \n"
                                    "{\n"
                                    " alternate-background-color: rgba(213,29,62, 40); \n"
                                    "}\n"
                                    "QDateEdit  QCalendarWidget QToolButton#qt_calendar_prevmonth \n"
                                    "{\n"
                                    "    qproperty-icon: url(back.png);\n"
                                    "}\n"
                                    "QDateEdit  QCalendarWidget QToolButton#qt_calendar_nextmonth \n"
                                    "{\n"
                                    "    qproperty-icon: url(forward.png);\n"
                                    "}\n"
                                    "QCalendarWidget QWidget#qt_calendar_navigationbar\n"
                                    "{ \n"
                                    "  background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 rgb(213,29,62)); \n"
                                    "}")
        self.dateEdit_2.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.dateEdit_2.setSpecialValueText("")
        self.dateEdit_2.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_2.setDate(QtCore.QDate(2020, 2, 1))
        self.horizontalLayout_3.addWidget(self.dateEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setStyleSheet("background-color: rgb(255, 0, 0);")
        reporte=list(['Seleccione un tipo de reporte','ABC','Top de Productos'])
        metodo=list(['Seleccione un Metodo','Piezas','Precio_Venta','Piezas Y Precio'])
        self.comboBox.clear()
        self.comboBox.addItems(metodo)
        self.comboBox_2.clear()
        self.comboBox_2.addItems(reporte)
        self.comboBox.setStyleSheet(" QComboBox {border: 1px solid gray;border-radius: 3px;padding: 1px 18px 1px 3px;min-width: 6em;background:white;color black;font-size: 9pt;font-weight: bold}"
            "QComboBox:editable {background: rgb(64, 224, 208);color: black}"
            "QComboBox:hover {background: rgba(235, 25, 25,.4)}" )
        self.comboBox_2.setStyleSheet(" QComboBox {border: 1px solid gray;border-radius: 3px;padding: 1px 18px 1px 3px;min-width: 6em;background:white;color black;font-size: 9pt;font-weight: bold}"
            "QComboBox:editable {background: rgb(64, 224, 208);color:black}"
            "QComboBox:hover {background: rgba(235, 25, 25,.4)}" )


        self.statusbar.setObjectName("statusbar")
        self.pushButton.setStyleSheet("QPushButton {background:blue;padding: 2px;text-align:center;background-color: red;font-size: 10pt;color:white;font-weight: bold;border-style: outset;border-width: .5px;border-radius: 4px;border-color: black;}"
            "QPushButton:pressed {background-color:black;font-size: 10pt;font-weight: bold;color:white}"
            "QPushButton:hover {background-color:rgb(215, 15, 15);font-size: 10pt;font-weight: bold;color:white}"
            )
        self.pushButton_2.setStyleSheet("QPushButton {background-color: red;font-size: 10pt;color:white;font-weight: bold;border-style: outset;border-width: .5px;border-radius: 4px;border-color: black;}"
            "QPushButton:pressed {background-color:black;font-size: 10pt;font-weight: bold;color:white}"
            "QPushButton:hover {background-color:rgb(215, 15, 15);font-size: 10pt;font-weight: bold;color:white}"
            )

        
        self.pushButton.clicked.connect(self.openfiles2)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_2.clicked.connect(self.metodo)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ABC"))
        self.pushButton_2.setText(_translate("MainWindow", "Generar reporte"))
        self.pushButton.setText(_translate("MainWindow", "Seleccionar Archivo"))
        self.label.setText(_translate("MainWindow", "Tipo de Reprte"))
        self.label_2.setText(_translate("MainWindow", "Metodo de Seleccion"))
        self.label_3.setText(_translate("MainWindow", "Fecha de Inicio"))
        self.label_4.setText(_translate("MainWindow", "Fecha Fin"))
    
    def filtro(self):
        pd.set_option('display.max_columns', 10)
        pd.set_option('display.max_rows', None)
        global fileName_
        global df_
        df=pd.read_csv(fileName_,low_memory=True , encoding='utf-8')        
        datos=df       
        print(len(datos))
        df2=df[df['Estatus_Reza'] == 'Autorizado']
        print('aautorizdos')
        print(len(df2))
        estatus_p=['Cancelado','Cancelado por Validación Telefónica','Dictaminado Fraude','Intento','Pendiente por Validación Telefónica','Rechazo validación manual','Reembolso realizado','Rechazado','Reembolso autorizado','TDC rechazada']
        for x in range(len(estatus_p)):
            df2=df2[df2['Estatus_Pedido_Desc']!=estatus_p[x]]
            print(estatus_p[x])
            print(len(df2))

        estatus_pr=['Cancelado','Solicita Cancelacion','En disputa']
        for x in range(len(estatus_pr)):
            df2=df2[df2['EstatusProducto']!=estatus_pr[x]]
            print(estatus_pr[x])
            print(len(df2))
        df2['Motivo']=df2['Motivo'].fillna(0)

        df2=df2[df2['Motivo']==0]

        print('Motivo')
        print(len(df2))
        df2.to_csv("Entregados.csv",encoding='utf-8-sig')
        df_=df2
        
    def openfiles2(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        
        fileName, _ = QFileDialog.getOpenFileName(None,"Buscar CSV", "","csv file (*.csv)",options=options)
        if fileName:
            global fileName_
            fileName_ = fileName
            self.lineEdit.setText(fileName)
            df=pd.read_csv(fileName, low_memory=True , encoding='utf-8')
            df2=pd.DataFrame(df)
            fileName=str(fileName)
            ARCH=fileName
            print(fileName)
            self.lineEdit.setEnabled(False)
            self.fileName=fileName
            self.filtro()
            
    def abcXPiezas(self):
        global df_
        datos=df_
        datosa=pd.DataFrame(datos.groupby(['Id_Producto','Nombre_Producto']).count().reset_index())
        datosa=pd.DataFrame(datosa.sort_values(by=['Indice'],ascending=False))
        d1=pd.DataFrame(datosa.head(round(.2*len(datosa))))
        mau=(list(d1.columns.values.tolist()))
        d3=d1.iloc[:,[mau.index('Id_Producto'),mau.index('Nombre_Producto'),mau.index('Indice')]]
        d3['Piezas']=d3['Indice']
        d3['Clasificacion']='A'
        d3.drop(['Indice'], axis='columns', inplace=True)             
        ###productos clase b
        db=pd.DataFrame(datosa.tail(len(datosa)-round(len(d3))))
        prB=pd.DataFrame(db.head(round(len(datosa)*.3)))
        mau=(list(prB.columns.values.tolist()))
        db2=prB.iloc[:,[mau.index('Id_Producto'),mau.index('Nombre_Producto'),mau.index('Indice')]]
        db2['Piezas']=db2['Indice']
        db2['Clasificacion']='B'
        db2.drop(['Indice'], axis='columns', inplace=True)
        vertical_stack = pd.concat([d3, db2], axis=0)
        ####clase c
        prc=pd.DataFrame(datosa.tail((len(datosa)-len(d3)-len(db2))))
        mau=(list(prc.columns.values.tolist()))
        dc2=prc.iloc[:,[mau.index('Id_Producto'),mau.index('Nombre_Producto'),mau.index('Indice')]]
        dc2['Piezas']=dc2['Indice']
        dc2['Clasificacion']='C'
        dc2.drop(['Indice'], axis='columns', inplace=True)        
        vertical_stack = pd.concat([vertical_stack, dc2], axis=0) 
        x=range(0,len(vertical_stack))
        nn=list(x)
        vertical_stack=vertical_stack.set_index(np.asarray(nn)) 
        today = datetime.now()
        d1 = today.strftime("%d%m%Y%H%M%S")
        ruta=('ABCxPiezas'+d1+'.csv')
        vertical_stack.to_csv(ruta, index=True,encoding='utf-8-sig')
        mb = QMessageBox()
        mb.setIcon(QMessageBox.Information)
        mb.setWindowTitle('reporte Generado')
        mb.setText('REPORTE GENERADO EXITOSAMENTE EN: '+ruta)
        mb.setStandardButtons(QMessageBox.Ok)
        mb.exec_() 
                
    def abcXPesos(self):
        global df_
        datos=df_
        datosa=pd.DataFrame(datos.groupby(['Id_Producto','Nombre_Producto'])['Precio_Venta_Producto'].sum().reset_index())
        datosa=pd.DataFrame(datosa.sort_values(by=['Precio_Venta_Producto'],ascending=False))
        
        d1=pd.DataFrame(datosa.head(round(.2*len(datosa))))
        mau=(list(d1.columns.values.tolist()))
        d3=d1.iloc[:,[mau.index('Id_Producto'),mau.index('Nombre_Producto'),mau.index('Precio_Venta_Producto')]]
        d3['Total_Venta']=d3['Precio_Venta_Producto']
        d3['Clasificacion']='A'
        d3.drop(['Precio_Venta_Producto'], axis='columns', inplace=True)             
        ###productos clase b
        db=pd.DataFrame(datosa.tail(len(datosa)-round(len(d3))))
        prB=pd.DataFrame(db.head(round(len(datosa)*.3)))
        mau=(list(prB.columns.values.tolist()))
        db2=prB.iloc[:,[mau.index('Id_Producto'),mau.index('Nombre_Producto'),mau.index('Precio_Venta_Producto')]]
        db2['Total_Venta']=db2['Precio_Venta_Producto']
        db2['Clasificacion']='B'
        db2.drop(['Precio_Venta_Producto'], axis='columns', inplace=True)
        vertical_stack = pd.concat([d3, db2], axis=0)
        ####clase c
        prc=pd.DataFrame(datosa.tail((len(datosa)-len(d3)-len(db2))))
        mau=(list(prc.columns.values.tolist()))
        dc2=prc.iloc[:,[mau.index('Id_Producto'),mau.index('Nombre_Producto'),mau.index('Precio_Venta_Producto')]]
        dc2['Total_Venta']=dc2['Precio_Venta_Producto']
        dc2['Clasificacion']='C'
        dc2.drop(['Precio_Venta_Producto'], axis='columns', inplace=True)        
        vertical_stack = pd.concat([vertical_stack, dc2], axis=0) 
        x=range(0,len(vertical_stack))
        nn=list(x)
        vertical_stack=vertical_stack.set_index(np.asarray(nn)) 
        today = datetime.now()
        d1 = today.strftime("%d%m%Y%H%M%S")
        ruta=('ABCxPesos'+d1+'.csv')
        vertical_stack.to_csv(ruta, index=True,encoding='utf-8-sig')
        mb = QMessageBox()
        mb.setIcon(QMessageBox.Information)
        mb.setWindowTitle('reporte Generado')
        mb.setText('REPORTE GENERADO EXITOSAMENTE EN: '+ruta)
        mb.setStandardButtons(QMessageBox.Ok)
        mb.exec_()

    def abcXPyP(self):
        global df_
        datos=df_
        datosa=(datos.groupby(['Id_Producto','Nombre_Producto','Nombre_Tienda','SKU','sku_hijo']).agg({'Indice':'count', 'Precio_Venta_Producto': 'sum'}).reset_index().rename(columns={'Piezas':'Total de Venta'}))
        datosa=pd.DataFrame(datosa.sort_values(by=['Precio_Venta_Producto','Indice'],ascending=False))        # print(datosa2.head(20))
        d1=pd.DataFrame(datosa.head(round(.2*len(datosa))))
        mau=(list(d1.columns.values.tolist()))
        d3=d1.iloc[:,[mau.index('Id_Producto'),mau.index('Nombre_Producto'),mau.index('Nombre_Tienda'),mau.index('SKU'),mau.index('sku_hijo'),mau.index('Indice'),mau.index('Precio_Venta_Producto')]]
        d3['Piezas']=d3['Indice']
        d3['Clasificacion']='A'
        d3.drop(['Indice'], axis='columns', inplace=True)             
        ###productos clase b
        db=pd.DataFrame(datosa.tail(len(datosa)-round(len(d3))))
        prB=pd.DataFrame(db.head(round(len(datosa)*.3)))
        mau=(list(prB.columns.values.tolist()))
        db2=prB.iloc[:,[mau.index('Id_Producto'),mau.index('Nombre_Producto'),mau.index('Nombre_Tienda'),mau.index('SKU'),mau.index('sku_hijo'),mau.index('Indice'),mau.index('Precio_Venta_Producto')]]
        db2['Piezas']=db2['Indice']
        db2['Clasificacion']='B'
        db2.drop(['Indice'], axis='columns', inplace=True)
        vertical_stack = pd.concat([d3, db2], axis=0)
        ####clase c
        prc=pd.DataFrame(datosa.tail((len(datosa)-len(d3)-len(db2))))
        mau=(list(prc.columns.values.tolist()))
        dc2=prc.iloc[:,[mau.index('Id_Producto'),mau.index('Nombre_Producto'),mau.index('Nombre_Tienda'),mau.index('SKU'),mau.index('sku_hijo'),mau.index('Indice'),mau.index('Precio_Venta_Producto')]]
        dc2['Piezas']=dc2['Indice']
        dc2['Clasificacion']='C'
        dc2.drop(['Indice'], axis='columns', inplace=True)        
        vertical_stack = pd.concat([vertical_stack, dc2], axis=0) 
        x=range(0,len(vertical_stack))
        nn=list(x)
        vertical_stack=vertical_stack.set_index(np.asarray(nn)) 
        today = datetime.now()
        d1 = today.strftime("%d%m%Y%H%M%S")
        print(vertical_stack.head(100))
        ruta=('ABCxPesoyPiezas'+d1+'.csv')
        vertical_stack.to_csv(ruta, index=True,encoding='utf-8-sig')
        mb = QMessageBox()
        mb.setIcon(QMessageBox.Information)
        mb.setWindowTitle('reporte Generado')
        mb.setText('REPORTE GENERADO EXITOSAMENTE EN: '+ruta)
        mb.setStandardButtons(QMessageBox.Ok)
        mb.exec_()
        print

    def topXPiezas(self):
        global df_
        datos=df_
        i, okPressed = QInputDialog.getInt(None, "Seleccione el top que desea consultar","TOP: ", 100, 0, 100, 1)
        if okPressed:
            datosa=pd.DataFrame(datos.groupby(['Id_Producto','Nombre_Producto'])['Indice'].count().reset_index())
            datosa=pd.DataFrame(datosa.sort_values(by=['Indice'],ascending=False))
            df1=pd.DataFrame(datosa.head(i)).reset_index()
            x=range(0,i)
            nn=list(x)
            df1.drop(['index'], axis='columns', inplace=True)  
            df1.set_index(np.asarray(nn))
            today = datetime.now()
            d1 = today.strftime("%d%m%Y%H%M%S")
            ruta=('TOPxPiezas'+d1+'.csv')
            print(df1.head(20))
            df1.to_csv(ruta, index=True,encoding='utf-8-sig')
            mb = QMessageBox()
            mb.setIcon(QMessageBox.Information)
            mb.setWindowTitle('reporte Generado')
            mb.setText('REPORTE GENERADO EXITOSAMENTE EN: '+ruta)
            mb.setStandardButtons(QMessageBox.Ok)
            mb.exec_()
                
    def topXPesos(self):
        global df_
        datos=df_
        i, okPressed = QInputDialog.getInt(None, "Seleccione el top que desea consultar","TOP: ", 100, 0, 100, 1)
        if okPressed:
            datosa=pd.DataFrame(datos.groupby(['Id_Producto','Nombre_Producto'])['Precio_Venta_Producto'].sum().reset_index())
            datosa=pd.DataFrame(datosa.sort_values(by=['Precio_Venta_Producto'],ascending=False))
            df1=pd.DataFrame(datosa.head(i)) 
            print(df1.head(20))
            x=range(0,i)
            nn=list(x)
            # df1.drop(['index'], axis='columns', inplace=True)  
            df1.set_index(np.asarray(nn))
            today = datetime.now()
            d1 = today.strftime("%d%m%Y%H%M%S")
            ruta=('TOPxPesos'+d1+'.csv')
            df1.to_csv(ruta, index=False,encoding='utf-8-sig')
            mb = QMessageBox()
            mb.setIcon(QMessageBox.Information)
            mb.setWindowTitle('reporte Generado')
            mb.setText('REPORTE GENERADO EXITOSAMENTE EN: '+ruta)
            mb.setStandardButtons(QMessageBox.Ok)
            mb.exec_()


    def topXPyP(self):
        global df_
        datos=df_
        i, okPressed = QInputDialog.getInt(None, "Seleccione el top que desea consultar","TOP: ", 550, 0, 550, 1)
        if okPressed:
            datosa=(datos.groupby(['Id_Producto','Nombre_Producto','Nombre_Tienda','SKU','sku_hijo']).agg({'Indice':'count', 'Precio_Venta_Producto': 'sum'}).reset_index().rename(columns={'Piezas':'Total de Venta'}))
            datosa=pd.DataFrame(datosa.sort_values(by=['Precio_Venta_Producto','Indice'],ascending=False))
        
            df1=pd.DataFrame(datosa.head(i)) 
            x=range(0,i)
            nn=list(x)
            today = datetime.now()
            d1 = today.strftime("%d%m%Y%H%M%S")
            ruta=('TOPxPesos'+d1+'.csv')
            df1.to_csv(ruta, index=False,encoding='utf-8-sig')
            mb = QMessageBox()
            mb.setIcon(QMessageBox.Information)
            mb.setWindowTitle('reporte Generado')
            mb.setText('REPORTE GENERADO EXITOSAMENTE EN: '+ruta)
            mb.setStandardButtons(QMessageBox.Ok)
            mb.exec_()

    def metodo(self):
        global df_
        df_['Fecha_Pedido_Colocado']=pd.to_datetime(df_['Fecha_Pedido_Colocado'],dayfirst=True)
        print(df_['Fecha_Pedido_Colocado'].tail())
        temp_var = pd.to_datetime(self.dateEdit.date().toPyDate())
        print((temp_var))
        print((temp_var))
        
        ayer = temp_var + timedelta(days=1)
        df_=df_[df_['Fecha_Pedido_Colocado']<=ayer]
        
        temp_var = pd.to_datetime(self.dateEdit_2.date().toPyDate())
        print((temp_var))
        print((temp_var))
        print((temp_var))
        df_=df_[df_['Fecha_Pedido_Colocado']>=temp_var]
        
        print(df_['Fecha_Pedido_Colocado'].tail())
        
        df_.to_csv("Ventas_Entrega.csv",encoding='utf-8-sig')
        
        
        if self.comboBox_2.currentText()=='ABC':
        
            if self.comboBox.currentText()=='Precio_Venta':
                self.abcXPesos()
            elif self.comboBox.currentText()=='Piezas':
                self.abcXPiezas()
            elif self.comboBox.currentText()=='Piezas Y Precio':
                self.abcXPyP()
            else:
                print("Seleccione un metodo")
                mb = QMessageBox()
                mb.setIcon(QMessageBox.Warning)
                mb.setWindowTitle('Operacion no completada')
                mb.setText('DEBE SELECCIONAR UN METODO PARA GENERAR EL REPORTE')
                mb.setStandardButtons(QMessageBox.Ok)
                mb.exec_()
        elif self.comboBox_2.currentText()=='Top de Productos':

            if self.comboBox.currentText()=='Precio_Venta':
                self.topXPesos()
            elif self.comboBox.currentText()=='Piezas':
                self.topXPiezas()
            elif self.comboBox.currentText()=='Piezas Y Precio':
                self.topXPyP()
            else:
                print("Seleccione un metodo")
                mb = QMessageBox()
                mb.setIcon(QMessageBox.Warning)
                mb.setWindowTitle('Operacion no completada')
                mb.setText('DEBE SELECCIONAR UN METODO PARA GENERAR EL REPORTE')
                mb.setStandardButtons(QMessageBox.Ok)
                mb.exec_()
        else:
            print('sELECCIONE UN TIPO DE reporte')
            mb = QMessageBox()
            mb.setIcon(QMessageBox.Warning)
            mb.setWindowTitle('Operacion no completada')
            mb.setText('DEBE SELECCIONAR UN EL TIPO DE REPORTE QUE DESEA GENERAR')
            mb.setStandardButtons(QMessageBox.Ok)
            mb.exec_()

        
        

        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())