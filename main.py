from PyQt5 import QtCore, QtWidgets
from pl1 import PL1_Ui
from PLNE_Knapsack import KnapsackUI



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 650)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: #DDDBDE; color: #000;")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 430, 150, 50))
        self.pushButton.setStyleSheet("font-family: Arial; font-size: 15px; font-weight: bold;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(400, 430, 150, 50))
        self.pushButton2.setStyleSheet("font-family: Arial; font-size: 15px; font-weight: bold;")
        self.pushButton2.setObjectName("pushButton")
       
        
       
        
       
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(20, 390, 761, 2))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setStyleSheet("border: 1px solid black;")
        self.line_2.setObjectName("line_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 20, 600, 75))
        self.label.setStyleSheet("font-family: Arial; font-size: 40px; font-weight: bold; color: #000;")
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(90, 90, 620, 2))
        self.line.setStyleSheet("border: 1px solid black;")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setStyleSheet("border: 1px solid black;")
        self.line_2.setObjectName("line_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 110, 180, 40))
        self.label_2.setStyleSheet("font-family: Arial; font-size: 25px; color: #8AB6F9;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 150, 270, 50))
        self.label_3.setStyleSheet("font-family: Arial; font-size: 25px; font-weight: bold; color: #000;")
        self.label_3.setObjectName("label_3")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(520, 320, 200, 50))
        self.label_7.setStyleSheet("font-family: Arial; font-size: 25px; font-weight: bold; color: #000;")
        self.label_7.setObjectName("label_7")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setStyleSheet("font-family: Arial; font-size: 25px; font-weight: bold; color: #000;")        
        self.label_5.setGeometry(QtCore.QRect(110, 230, 270, 50))
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(520, 150, 200, 50))
        self.label_4.setStyleSheet("font-family: Arial; font-size: 25px; font-weight: bold; color: #000;")
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setStyleSheet("font-family: Arial; font-size: 25px; font-weight: bold; color: #000;")
        self.label_6.setGeometry(QtCore.QRect(520, 230, 230, 50))
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.open_exercice_1)
        self.pushButton2.clicked.connect(self.open_PLNE)
        
    


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Exercice PL"))
        self.pushButton2.setText(_translate("MainWindow", "Exercice PLNE"))
       
        self.label.setText(_translate("MainWindow", "Projet : Recherche Opérationnelle"))
        self.label_2.setText(_translate("MainWindow", "Elaboré par :"))
        self.label_3.setText(_translate("MainWindow", "Masmoudi Mohamed"))
        self.label_4.setText(_translate("MainWindow", "Gharbi Chaima"))
        self.label_5.setText(_translate("MainWindow", "Adel Mohamed Fedi"))
        self.label_6.setText(_translate("MainWindow", "???????????????"))
      
    def open_exercice_1(self):
        self.exercice_1_window = PL1_Ui()
        self.exercice_1_window.setupUi(self.exercice_1_window)
        self.exercice_1_window.show()
    
    def open_PLNE(self):
        self.PLNE_Knapsack_window = KnapsackUI()
       
        self.PLNE_Knapsack_window.show()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
