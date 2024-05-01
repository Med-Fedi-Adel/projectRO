from PyQt5 import QtCore, QtWidgets
import gurobipy as gp
from PyQt5.QtGui import QPixmap
import sys
class ResultsDialog(QtWidgets.QDialog):
    def __init__(self, results, parent=None):
        super(ResultsDialog, self).__init__(parent)
        self.setWindowTitle("Résultats de l'optimisation")
        self.setGeometry(500, 400, 500, 300)

        # Create a QTextEdit widget to display the results
        text_edit = QtWidgets.QTextEdit(self)
        text_edit.setGeometry(10, 10, 480, 250)

        # Set the font style for the text in the results window
        font_style = "font-weight: bold; font-size: 14px; color: black;"
        text_edit.setStyleSheet(font_style)

        # Display the results in the QTextEdit
        text = "Résultats de l'optimisation :\n\n"
        for key, value in results.items():
            text += f"{key}: {value}\n"

        text_edit.setPlainText(text)
        text_edit.setReadOnly(True)
class PL3_Ui(QtWidgets.QMainWindow):  # Change QWidget to QMainWindow
    def setupUi(self, PL3_Ui):
        PL3_Ui.setObjectName("PL3_Ui")
        PL3_Ui.resize(1200, 900)
        self.centralwidget = QtWidgets.QWidget(PL3_Ui)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: #DDFFDD; color: black;")
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 10, 150, 100))
        self.label.setStyleSheet("color:red ; font-size: 40px; font-weight: bold;")

        self.image_label = QtWidgets.QLabel(self.centralwidget)
        self.image_label.setGeometry(QtCore.QRect(200, 10, 900, 350))
        self.image_label.setObjectName("image_label")
        image_path = "pl3.png"  # Replace with the actual path to your image file
        pixmap = QPixmap(image_path)
        self.image_label.setPixmap(pixmap)
        self.image_label.setScaledContents(True)
        self.resoudre1 = QtWidgets.QPushButton(self.centralwidget)
        self.resoudre1.setGeometry(QtCore.QRect(800, 500, 150, 50))
        self.resoudre1.setStyleSheet("background-color: #39FF14; color: white; border: 4px solid black; font-size: 16px; font-weight: bold;")
        self.resoudre1.setObjectName("resoudre1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 450, 91, 20))
        self.label_2.setObjectName("label_2")
        self.x_lundi_req = QtWidgets.QLineEdit(self.centralwidget)
        self.x_lundi_req.setGeometry(QtCore.QRect(400, 450, 113, 22))
        self.x_lundi_req.setObjectName("x_lundi_req")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(200, 500, 91, 20))
        self.label_3.setObjectName("label_3")
        self.x_mardi_req = QtWidgets.QLineEdit(self.centralwidget)
        self.x_mardi_req.setGeometry(QtCore.QRect(400, 500, 113, 22))
        self.x_mardi_req.setObjectName("x_mardi_req")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(200, 550, 101, 20))
        self.label_4.setObjectName("label_4")
        self.x_mercredi_req = QtWidgets.QLineEdit(self.centralwidget)
        self.x_mercredi_req.setGeometry(QtCore.QRect(400, 550, 113, 22))
        self.x_mercredi_req.setObjectName("x_mercredi_req")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(200, 600, 91, 20))
        self.label_5.setObjectName("label_5")
        self.x_jeudi_req = QtWidgets.QLineEdit(self.centralwidget)
        self.x_jeudi_req.setGeometry(QtCore.QRect(400, 600, 113, 22))
        self.x_jeudi_req.setObjectName("x_jeudi_req")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(200, 650, 91, 20))
        self.label_6.setObjectName("label_6")
        self.x_vendredi_req = QtWidgets.QLineEdit(self.centralwidget)
        self.x_vendredi_req.setGeometry(QtCore.QRect(400, 650, 113, 22))
        self.x_vendredi_req.setObjectName("x_vendredi_req")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(200, 700, 91, 20))
        self.label_7.setObjectName("label_7")
        self.x_samedi_req = QtWidgets.QLineEdit(self.centralwidget)
        self.x_samedi_req.setGeometry(QtCore.QRect(400, 700, 113, 22))
        self.x_samedi_req.setObjectName("x_samedi_req")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(200, 750, 91, 20))
        self.label_8.setObjectName("label_8")
        self.x_dimanche_req = QtWidgets.QLineEdit(self.centralwidget)
        self.x_dimanche_req.setGeometry(QtCore.QRect(400, 750, 113, 22))
        self.x_dimanche_req.setObjectName("x_dimanche_req")
        PL3_Ui.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(PL3_Ui)
        self.statusbar.setObjectName("statusbar")
        PL3_Ui.setStatusBar(self.statusbar)
        self.default_values_button = QtWidgets.QPushButton(self.centralwidget)
        self.default_values_button.setGeometry(QtCore.QRect(800, 600, 150, 50))
        self.default_values_button.setStyleSheet("background-color: #4CAF50; color: white; border: 4px solid black; font-size: 16px; font-weight: bold;")
        self.default_values_button.setObjectName("default_values_button")
        self.default_values_button.setText("Default Values")
        self.default_values_button.clicked.connect(self.set_default_values)
        self.x_lundi_req.setStyleSheet("background-color: white;")
        self.x_mardi_req.setStyleSheet("background-color: white;")
        self.x_mercredi_req.setStyleSheet("background-color: white;")
        self.x_jeudi_req.setStyleSheet("background-color: white;")
        self.x_vendredi_req.setStyleSheet("background-color: white;")
        self.x_samedi_req.setStyleSheet("background-color: white;")
        self.x_dimanche_req.setStyleSheet("background-color: white;")
        self.resoudre1.clicked.connect(self.show_results_dialog)
        label_font_style = "font-weight: bold; font-size: 14px;"
        self.label.setStyleSheet(label_font_style)
        self.label_2.setStyleSheet(label_font_style)
        self.label_3.setStyleSheet(label_font_style)
        self.label_4.setStyleSheet(label_font_style)
        self.label_5.setStyleSheet(label_font_style)
        self.label_6.setStyleSheet(label_font_style)
        self.label_7.setStyleSheet(label_font_style)
        self.label_8.setStyleSheet(label_font_style)

        self.retranslateUi(PL3_Ui)
        QtCore.QMetaObject.connectSlotsByName(PL3_Ui)
    def set_default_values(self):
        default_values = [17,13,15,19,14,16,11]  
        for i, line_edit in enumerate([self.x_lundi_req,self.x_mardi_req,self.x_mercredi_req,self.x_jeudi_req,self.x_vendredi_req,self.x_samedi_req,self.x_dimanche_req]):
            line_edit.setText(str(default_values[i]))
    def show_results_dialog(self):

        input_values = [
        self.x_lundi_req.text(),
        self.x_mardi_req.text(),
        self.x_mercredi_req.text(),
        self.x_jeudi_req.text(),
        self.x_vendredi_req.text(),
        self.x_samedi_req.text(),
        self.x_dimanche_req.text(),
    ]

        try:
        # Convert input values to integers and check if they are greater than or equal to 0
            x_values = [int(value) for value in input_values]
            if any(x < 0 for x in x_values):
                raise ValueError("Input values must be greater than or equal to 0.")
        except ValueError as e:
            QtWidgets.QMessageBox.critical(
            self,
            "Input Validation Error",
            f"Invalid input values. {str(e)}",
            QtWidgets.QMessageBox.Ok,
        )
            return

        x1, x2, x3, x4, x5, x6, x7 = x_values

        jour = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']

        PL3 = gp.Model("PL3")
        d1 = PL3.addVar(lb=0.0, vtype=gp.GRB.INTEGER, name='d1')
        d2 = PL3.addVar(lb=0.0, vtype=gp.GRB.INTEGER, name='d2')
        d3 = PL3.addVar(lb=0.0, vtype=gp.GRB.INTEGER, name='d3')
        d4 = PL3.addVar(lb=0.0, vtype=gp.GRB.INTEGER, name='d4')
        d5 = PL3.addVar(lb=0.0, vtype=gp.GRB.INTEGER, name='d5')
        d6 = PL3.addVar(lb=0.0, vtype=gp.GRB.INTEGER, name='d6')
        d7 = PL3.addVar(lb=0.0, vtype=gp.GRB.INTEGER, name='d7')
        d=[d1,d2,d3,d4,d5,d6,d7]

        s1=d1+d7+d6+d4+d5
        s2=d2+d1+d7+d5+d6
        s3=d3+d1+d2+d6+d7
        s4=d4+d2+d3+d7+d1
        s5=d5+d3+d4+d1+d2
        s6=d6+d4+d5+d2+d3
        s7=d7+d5+d6+d3+d4

        PL3.addConstr(s1>=x1, name='c1')
        PL3.addConstr(s2>=x2, name='c2')
        PL3.addConstr(s3>=x3, name='c3')
        PL3.addConstr(s4>=x4, name='c4')
        PL3.addConstr(s5>=x5, name='c5')
        PL3.addConstr(s6>=x6, name='c6')
        PL3.addConstr(s7>=x7, name='c7')

        PL3.setObjective(gp.quicksum(d), gp.GRB.MINIMIZE)
        PL3.optimize()
        results = {}
        aux = []
        for i in range(7):
            aux.append(d[i].x)
            results[jour[i]] = round(d[i].x)

        total_optimal_employees = int(PL3.objVal)
        results["Total optimal employees"] = total_optimal_employees

        # Show the results in a dialog
        results_dialog = ResultsDialog(results, self)
        results_dialog.exec_()
    def retranslateUi(self, PL3_Ui):
        _translate = QtCore.QCoreApplication.translate
        PL3_Ui.setWindowTitle(_translate("PL3_Ui", "Exercice3"))
        self.label.setText(_translate("MainWindow", "PL 3:"))
        self.resoudre1.setText(_translate("MainWindow", "Résoudre"))
        self.label_2.setText(_translate("MainWindow", "lundi"))
        self.label_3.setText(_translate("MainWindow", "mardi"))
        self.label_4.setText(_translate("MainWindow", "mercredi"))
        self.label_5.setText(_translate("MainWindow", "jeudi"))
        self.label_6.setText(_translate("MainWindow", "vendredi"))
        self.label_7.setText(_translate("MainWindow", "samedi"))
        self.label_8.setText(_translate("MainWindow", "dimache"))
    def init_interface_(self):
        self.x_lundi_req.setText(str(self.x_lundi_req))
        self.x_mardi_req.setText(str(self.x_mardi_req))
        self.x_mercredi_req.setText(str(self.x_mercredi_req))
        self.x_jeudi_req.setText(str(self.x_jeudi_req))
        self.x_vendredi_req.setText(str(self.x_vendredi_req))
        self.x_samedi_req.setText(str(self.x_samedi_req))
        self.x_dimanche_req.setText(str(self.x_dimanche_req))

    """
        aux = []
        for i in range(7):
            aux.append(d[i])
        with open("Resolutions/PL3.txt", "w") as f:
            sys.stdout = f
            sheet = {}
            print("les nombres des employees qui commencent le jour: ")
            for i in range(7):
                print(jour[i] + "  :" + str(round(aux[i].x)))  
                sheet.update({jour[i]: [round(aux[i].x)]})
            print("le nombre totale optimale des employes est ", int(PL3.objVal))
    """




if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = PL3_Ui()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
