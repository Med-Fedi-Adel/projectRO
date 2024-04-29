import gurobipy as gp
from PyQt5 import QtCore, QtWidgets
import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QDoubleValidator,QValidator


class Culture:
    def __init__(self, nom, R, PU, MO, HM, E, SMO, FX):
    
        self.nom = nom
        self.R = R      #Rendement (Quantité / hectare)
        self.PU = PU    #Prix unité
        self.MO = MO    #Main d'oeuvre (/ hectare)
        self.HM = HM    #Heure machine (/ hectare)
        self.E = E      #Eau (metre cube / hectare )
        self.SMO = SMO  #Salaire annuel (/ouvrier)
        self.FX = FX    #Frais fixce

class ResultsDialog(QtWidgets.QDialog):
    def __init__(self, results, parent=None):
        super(ResultsDialog, self).__init__(parent)
        self.setWindowTitle("Résultats de l'optimisation")
        self.setGeometry(500, 400, 500, 200)

        # Create a QTextEdit widget to display the results
        text_edit = QtWidgets.QTextEdit(self)
        text_edit.setGeometry(10, 10, 480, 150)

        # Set the font style for the text in the results window
        font_style = "font-weight: bold; font-size: 14px;"
        text_edit.setStyleSheet(font_style)

        # Display the results in the QTextEdit
        text = "Résultats de l'optimisation :\n\n"
        for key, value in results.items():
            text += f"{key}: {value}\n"

        text_edit.setPlainText(text)
        text_edit.setReadOnly(True)



class PL1_Ui(QtWidgets.QMainWindow):  # Change QWidget to QMainWindow
    def setupUi(self, PL1_Ui):
        PL1_Ui.setObjectName("PL1_Ui")
        PL1_Ui.resize(1200, 900)
        self.centralwidget = QtWidgets.QWidget(PL1_Ui)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: #DDFFDD; color : #000;")  # Use your preferred shade of gray or white

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 10, 150, 100))
        self.label.setStyleSheet("color:red ; font-size: 40px; font-weight: bold;")

        self.image_label = QtWidgets.QLabel(self.centralwidget)
        self.image_label.setGeometry(QtCore.QRect(200, 10, 900, 350))
        self.image_label.setObjectName("image_label")
        image_path = "pl1.png"  # Replace with the actual path to your image file
        pixmap = QPixmap(image_path)
        self.image_label.setPixmap(pixmap)
        self.image_label.setScaledContents(True)  # Optional: Scale the image to fit the label
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(420, 390, 55, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(500, 390, 55, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(580, 390, 55, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(640, 390, 55, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(720, 390, 61, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(230, 430, 101, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(230, 470, 111, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(230, 510, 101, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(230, 550, 121, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(230, 590, 91, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(230, 630, 131, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(230, 670, 121, 16))
        self.label_13.setObjectName("label_13")
        self.ble1 = QtWidgets.QLineEdit(self.centralwidget)
        self.ble1.setGeometry(QtCore.QRect(400, 420, 61, 22))
        self.ble1.setObjectName("ble1")
        self.orge1 = QtWidgets.QLineEdit(self.centralwidget)
        self.orge1.setGeometry(QtCore.QRect(480, 420, 61, 22))
        self.orge1.setObjectName("orge1")
        self.mais1 = QtWidgets.QLineEdit(self.centralwidget)
        self.mais1.setGeometry(QtCore.QRect(560, 420, 61, 22))
        self.mais1.setObjectName("mais1")
        self.betsucre1 = QtWidgets.QLineEdit(self.centralwidget)
        self.betsucre1.setGeometry(QtCore.QRect(640, 420, 61, 22))
        self.betsucre1.setObjectName("betsucre1")
        self.tournesol1 = QtWidgets.QLineEdit(self.centralwidget)
        self.tournesol1.setGeometry(QtCore.QRect(720, 420, 61, 22))
        self.tournesol1.setObjectName("tournesol1")
        self.ble2 = QtWidgets.QLineEdit(self.centralwidget)
        self.ble2.setGeometry(QtCore.QRect(400, 460, 61, 22))
        self.ble2.setObjectName("ble2")
        self.orge2 = QtWidgets.QLineEdit(self.centralwidget)
        self.orge2.setGeometry(QtCore.QRect(480, 460, 61, 22))
        self.orge2.setObjectName("orge2")
        self.mais2 = QtWidgets.QLineEdit(self.centralwidget)
        self.mais2.setGeometry(QtCore.QRect(560, 460, 61, 22))
        self.mais2.setObjectName("mais2")
        self.betsucre2 = QtWidgets.QLineEdit(self.centralwidget)
        self.betsucre2.setGeometry(QtCore.QRect(640, 460, 61, 22))
        self.betsucre2.setObjectName("betsucre2")
        self.tournesol2 = QtWidgets.QLineEdit(self.centralwidget)
        self.tournesol2.setGeometry(QtCore.QRect(720, 460, 61, 22))
        self.tournesol2.setObjectName("tournesol2")
        self.ble3 = QtWidgets.QLineEdit(self.centralwidget)
        self.ble3.setGeometry(QtCore.QRect(400, 500, 61, 22))
        self.ble3.setObjectName("ble3")
        self.orge3 = QtWidgets.QLineEdit(self.centralwidget)
        self.orge3.setGeometry(QtCore.QRect(480, 500, 61, 22))
        self.orge3.setObjectName("orge3")
        self.mais3 = QtWidgets.QLineEdit(self.centralwidget)
        self.mais3.setGeometry(QtCore.QRect(560, 500, 61, 22))
        self.mais3.setObjectName("mais3")
        self.betsucre3 = QtWidgets.QLineEdit(self.centralwidget)
        self.betsucre3.setGeometry(QtCore.QRect(640, 500, 61, 22))
        self.betsucre3.setObjectName("betsucre3")
        self.tournesol3 = QtWidgets.QLineEdit(self.centralwidget)
        self.tournesol3.setGeometry(QtCore.QRect(720, 500, 61, 22))
        self.tournesol3.setObjectName("tournesol3")
        self.ble4 = QtWidgets.QLineEdit(self.centralwidget)
        self.ble4.setGeometry(QtCore.QRect(400, 540, 61, 22))
        self.ble4.setObjectName("ble4")
        self.orge4 = QtWidgets.QLineEdit(self.centralwidget)
        self.orge4.setGeometry(QtCore.QRect(480, 540, 61, 22))
        self.orge4.setObjectName("orge4")
        self.mais4 = QtWidgets.QLineEdit(self.centralwidget)
        self.mais4.setGeometry(QtCore.QRect(560, 540, 61, 22))
        self.mais4.setObjectName("mais4")
        self.betsucre4 = QtWidgets.QLineEdit(self.centralwidget)
        self.betsucre4.setGeometry(QtCore.QRect(640, 540, 61, 22))
        self.betsucre4.setObjectName("betsucre4")
        self.tournesol4 = QtWidgets.QLineEdit(self.centralwidget)
        self.tournesol4.setGeometry(QtCore.QRect(720, 540, 61, 22))
        self.tournesol4.setObjectName("tournesol4")
        self.ble5 = QtWidgets.QLineEdit(self.centralwidget)
        self.ble5.setGeometry(QtCore.QRect(400, 580, 61, 22))
        self.ble5.setObjectName("ble5")
        self.orge5 = QtWidgets.QLineEdit(self.centralwidget)
        self.orge5.setGeometry(QtCore.QRect(480, 580, 61, 22))
        self.orge5.setObjectName("orge5")
        self.mais5 = QtWidgets.QLineEdit(self.centralwidget)
        self.mais5.setGeometry(QtCore.QRect(560, 580, 61, 22))
        self.mais5.setObjectName("mais5")
        self.betsucre5 = QtWidgets.QLineEdit(self.centralwidget)
        self.betsucre5.setGeometry(QtCore.QRect(640, 580, 61, 22))
        self.betsucre5.setObjectName("betsucre5")
        self.tournesol5 = QtWidgets.QLineEdit(self.centralwidget)
        self.tournesol5.setGeometry(QtCore.QRect(720, 580, 61, 22))
        self.tournesol5.setObjectName("tournesol5")
        self.ble6 = QtWidgets.QLineEdit(self.centralwidget)
        self.ble6.setGeometry(QtCore.QRect(400, 620, 61, 22))
        self.ble6.setObjectName("ble6")
        self.orge6 = QtWidgets.QLineEdit(self.centralwidget)
        self.orge6.setGeometry(QtCore.QRect(480, 620, 61, 22))
        self.orge6.setObjectName("orge6")
        self.mais6 = QtWidgets.QLineEdit(self.centralwidget)
        self.mais6.setGeometry(QtCore.QRect(560, 620, 61, 22))
        self.mais6.setObjectName("mais6")
        self.betsucre6 = QtWidgets.QLineEdit(self.centralwidget)
        self.betsucre6.setGeometry(QtCore.QRect(640, 620, 61, 22))
        self.betsucre6.setObjectName("betsucre6")
        self.tournesol6 = QtWidgets.QLineEdit(self.centralwidget)
        self.tournesol6.setGeometry(QtCore.QRect(720, 620, 61, 22))
        self.tournesol6.setObjectName("tournesol6")
        self.ble7 = QtWidgets.QLineEdit(self.centralwidget)
        self.ble7.setGeometry(QtCore.QRect(400, 660, 61, 22))
        self.ble7.setObjectName("ble7")
        self.orge7 = QtWidgets.QLineEdit(self.centralwidget)
        self.orge7.setGeometry(QtCore.QRect(480, 660, 61, 22))
        self.orge7.setObjectName("orge7")
        self.mais7 = QtWidgets.QLineEdit(self.centralwidget)
        self.mais7.setGeometry(QtCore.QRect(560, 660, 61, 22))
        self.mais7.setObjectName("mais7")
        self.betsucre7 = QtWidgets.QLineEdit(self.centralwidget)
        self.betsucre7.setGeometry(QtCore.QRect(640, 660, 61, 22))
        self.betsucre7.setObjectName("betsucre7")
        self.tournesol7 = QtWidgets.QLineEdit(self.centralwidget)
        self.tournesol7.setGeometry(QtCore.QRect(720, 660, 61, 22))
        self.tournesol7.setObjectName("tournesol7")
        self.resoudre1 = QtWidgets.QPushButton(self.centralwidget)
        self.resoudre1.setGeometry(QtCore.QRect(900, 600, 150, 50))
        self.resoudre1.setStyleSheet("background-color: #39FF14; color: #000; border: 4px solid black; font-size: 16px; font-weight: bold;")
        self.resoudre1.setObjectName("resoudre1")
        self.resoudre1.clicked.connect(self.show_results_dialog)        
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(230, 740, 161, 16))
        self.label_19.setObjectName("label_19")
        self.surface_zone = QtWidgets.QLineEdit(self.centralwidget)
        self.surface_zone.setGeometry(QtCore.QRect(400, 740, 61, 22))
        self.surface_zone.setObjectName("surface_zone")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(230, 780, 101, 16))
        self.label_17.setObjectName("label_17")
        self.main_oeuvre = QtWidgets.QLineEdit(self.centralwidget)
        self.main_oeuvre.setGeometry(QtCore.QRect(400, 780, 61, 22))
        self.main_oeuvre.setObjectName("main_oeuvre")
        self.eau_irrig = QtWidgets.QLineEdit(self.centralwidget)
        self.eau_irrig.setGeometry(QtCore.QRect(720, 740, 61, 22))
        self.eau_irrig.setObjectName("eau_irrig")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(550, 740, 161, 16))
        self.label_18.setObjectName("label_18")
        self.heures_machine = QtWidgets.QLineEdit(self.centralwidget)
        self.heures_machine.setGeometry(QtCore.QRect(720, 780, 61, 22))
        self.heures_machine.setObjectName("heures_machine")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(550, 780, 161, 16))
        self.label_16.setObjectName("label_16")
        self.prix_metre = QtWidgets.QLineEdit(self.centralwidget)
        self.prix_metre.setGeometry(QtCore.QRect(720, 820, 61, 22))
        self.prix_metre.setObjectName("prix_metre")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(230, 820, 131, 16))
        self.label_15.setObjectName("label_15")
        self.cout_heure = QtWidgets.QLineEdit(self.centralwidget)
        self.cout_heure.setGeometry(QtCore.QRect(400, 820, 61, 22))
        self.cout_heure.setObjectName("cout_heure")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(550, 820, 161, 16))
        self.label_14.setObjectName("label_14")
        line_edits = [self.ble1, self.ble2, self.ble3, self.ble4, self.ble5, self.ble6, self.ble7,self.orge1, self.orge2, self.orge3, self.orge4, self.orge5, self.orge6, self.orge7,self.mais1, self.mais2, self.mais3, self.mais4, self.mais5, self.mais6, self.mais7,self.betsucre1, self.betsucre2, self.betsucre3, self.betsucre4, self.betsucre5, self.betsucre6, self.betsucre7,self.tournesol1, self.tournesol2, self.tournesol3, self.tournesol4, self.tournesol5, self.tournesol6, self.tournesol7,self.surface_zone, self.main_oeuvre, self.eau_irrig, self.heures_machine, self.prix_metre, self.cout_heure]
        for line_edit in line_edits:
            line_edit.setStyleSheet("background-color: white;")
        PL1_Ui.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(PL1_Ui)
        self.statusbar.setObjectName("statusbar")
        PL1_Ui.setStatusBar(self.statusbar)
        self.retranslateUi(PL1_Ui)
        QtCore.QMetaObject.connectSlotsByName(PL1_Ui)
        self.default_values_button = QtWidgets.QPushButton(self.centralwidget)
        self.default_values_button.setGeometry(QtCore.QRect(900, 660, 150, 50))
        self.default_values_button.setStyleSheet("background-color: #4CAF50; color: white; border: 4px solid black; font-size: 16px; font-weight: bold;")
        self.default_values_button.setObjectName("default_values_button")
        self.default_values_button.setText("Default Values")
        self.default_values_button.clicked.connect(self.set_default_values)
        font_style = "font-weight: bold; font-size: 11px; color: #000;"
        for label in [self.label_2, self.label_3, self.label_4, self.label_5, self.label_6,
                      self.label_7, self.label_8, self.label_9, self.label_10, self.label_11,
                      self.label_12, self.label_13, self.label_19, self.label_17, self.label_18,
                      self.label_16, self.label_15, self.label_14]:
            label.setStyleSheet(font_style)
    def set_default_values(self):
        default_values = [75,60,2,30,300,500,250,60,50,1,24,200,500,180,55,66,2,20,250,600,190,50,110,3,28,380,700,310,60,60,2,25,320,550,320,1000,3000,25000000,24000,1,30]  
        for i, line_edit in enumerate([self.ble1, self.ble2, self.ble3, self.ble4, self.ble5, self.ble6, self.ble7,
                                       self.orge1, self.orge2, self.orge3, self.orge4, self.orge5, self.orge6, self.orge7,
                                       self.mais1, self.mais2, self.mais3, self.mais4, self.mais5, self.mais6, self.mais7,
                                       self.betsucre1, self.betsucre2, self.betsucre3, self.betsucre4, self.betsucre5, self.betsucre6, self.betsucre7,
                                       self.tournesol1, self.tournesol2, self.tournesol3, self.tournesol4, self.tournesol5, self.tournesol6, self.tournesol7,
                                       self.surface_zone, self.main_oeuvre, self.eau_irrig, self.heures_machine, self.prix_metre, self.cout_heure]):
            line_edit.setText(str(default_values[i]))

    def show_results_dialog(self):
        if not self.validate_input():
            QtWidgets.QMessageBox.critical(self, "Input Error", "Please ensure all input values are valid and greater than 0.0")
            return

        # Call the PL1 function to perform optimization
        results = self.PL1()

        # Create a ResultsDialog and show it
        results_dialog = ResultsDialog(results, self)
        results_dialog.exec_()
    def retranslateUi(self, PL1_Ui):
        _translate = QtCore.QCoreApplication.translate
        PL1_Ui.setWindowTitle(_translate("PL1_Ui", "Exercice 1"))
        self.label.setText(_translate("MainWindow", "PL 1:"))
        self.label_2.setText(_translate("MainWindow", "Blé"))
        self.label_3.setText(_translate("MainWindow", "Orge"))
        self.label_4.setText(_translate("MainWindow", "Mais"))
        self.label_5.setText(_translate("MainWindow", "Bet-sucre"))
        self.label_6.setText(_translate("MainWindow", "Tournesol"))
        self.label_7.setText(_translate("MainWindow", "Rendement Q/ha"))
        self.label_8.setText(_translate("MainWindow", "Prix de vente UM/Q"))
        self.label_9.setText(_translate("MainWindow", "M.O ouvriers /ha"))
        self.label_10.setText(_translate("MainWindow", "Temps Machine H/ha"))
        self.label_11.setText(_translate("MainWindow", "Eau m3/ha"))
        self.label_12.setText(_translate("MainWindow", "Salaire annuel/Ouvrier"))
        self.label_13.setText(_translate("MainWindow", "Frais fixe de gestion"))
        self.resoudre1.setText(_translate("MainWindow", "Résoudre"))
        self.label_19.setText(_translate("MainWindow", "Surface de la zone agricole"))
        self.label_17.setText(_translate("MainWindow", "Main d\'oeuvre"))
        self.label_18.setText(_translate("MainWindow", "Eau d\'irrigation"))
        self.label_16.setText(_translate("MainWindow", "Heures machine"))
        self.label_15.setText(_translate("MainWindow", "Cout heure machine"))
        self.label_14.setText(_translate("MainWindow", "Prix metre cube"))
    def validate_input(self):
        float_validator = QDoubleValidator(bottom=-1)

        line_edits = [self.ble1, self.ble2, self.ble3, self.ble4, self.ble5, self.ble6, self.ble7,
                      self.orge1, self.orge2, self.orge3, self.orge4, self.orge5, self.orge6, self.orge7,
                      self.mais1, self.mais2, self.mais3, self.mais4, self.mais5, self.mais6, self.mais7,
                      self.betsucre1, self.betsucre2, self.betsucre3, self.betsucre4, self.betsucre5, self.betsucre6, self.betsucre7,
                      self.tournesol1, self.tournesol2, self.tournesol3, self.tournesol4, self.tournesol5, self.tournesol6, self.tournesol7,
                      self.surface_zone, self.main_oeuvre, self.eau_irrig, self.heures_machine, self.prix_metre, self.cout_heure]

        for line_edit in line_edits:
            text = line_edit.text().strip()
            if not text or not float_validator.validate(text, 0)[0] == QValidator.Acceptable:
                return False  # Invalid input

        return True  # All inputs are valid
    def PL1(self):
        #Data extracted from the input
        prix_eau = float(self.prix_metre.text())
        prix_mch = float(self.cout_heure.text())
        surface = float(self.surface_zone.text())
        max_mo = float(self.main_oeuvre.text())
        max_eau = float(self.eau_irrig.text())
        max_mch = float(self.heures_machine.text())

        Ble = Culture("Ble", int(self.ble1.text()), int(self.ble2.text()), int(self.ble3.text()),int(self.ble4.text()), int(self.ble5.text()), int(self.ble6.text()), int(self.ble7.text()))
        Orge = Culture("Orge", int(self.orge1.text()), int(self.orge2.text()), int(self.orge3.text()),int(self.orge4.text()), int(self.orge5.text()), int(self.orge6.text()),int(self.orge7.text()))
        Mais = Culture("Mais", int(self.mais1.text()), int(self.mais2.text()), int(self.mais3.text()),int(self.mais4.text()), int(self.mais5.text()), int(self.mais6.text()),int(self.mais7.text()))
        Betrave = Culture("Betrave", int(self.betsucre1.text()), int(self.betsucre2.text()),int(self.betsucre3.text()), int(self.betsucre4.text()), int(self.betsucre5.text()),int(self.betsucre6.text()), int(self.betsucre7.text()))
        Tournesol = Culture("Tournesol", int(self.tournesol1.text()), int(self.tournesol2.text()),int(self.tournesol3.text()), int(self.tournesol4.text()), int(self.tournesol5.text()),int(self.tournesol6.text()), int(self.tournesol7.text()))
        Cultures = [Ble, Orge, Mais, Betrave, Tournesol]
        benef=[]
        for culture in Cultures:
            print(f"{culture.nom}: R={culture.R}, PU={culture.PU}, MO={culture.MO}, HM={culture.HM}, E={culture.E}, SMO={culture.SMO}, FX={culture.FX}")
            benefit = (culture.R*culture.PU - culture.MO*culture.SMO - culture.HM*prix_mch - culture.E*prix_eau - culture.FX)
            print(benefit)
            benef.append(benefit)
        model = gp.Model("NationalAgriCultureure")
        
        xBle = model.addVar(lb=0,vtype=gp.GRB.INTEGER, name="xBle")
        xOrge = model.addVar(lb=0,vtype=gp.GRB.INTEGER, name="xOrge")
        xMais = model.addVar(lb=0,vtype=gp.GRB.INTEGER, name="xMais")
        xBet = model.addVar(lb=0,vtype=gp.GRB.INTEGER, name="xBet")
        xTournesol = model.addVar(lb=0,vtype=gp.GRB.INTEGER, name="xTournesol")

        vals = [xBle, xOrge, xMais, xBet, xTournesol]

        model.setObjective(gp.quicksum(vals[i] * benef[i] for i in range(len(vals))), gp.GRB.MAXIMIZE)

        model.addConstr(xBle + xOrge + xMais + xBet + xTournesol <= surface, name="contrainte de surface")
        model.addConstr((xBle * Ble.MO) + (xOrge * Orge.MO) + (xMais * Mais.MO) + (xBet * Betrave.MO) + (xTournesol * Tournesol.MO) <= max_mo,name="contrainte de main d'oeuvre")
        model.addConstr(xBle * Ble.E + xMais * Mais.E + xOrge * Orge.E + xBet * Betrave.E + xTournesol * Tournesol.E <= max_eau,name="contrainte d'eau")
        model.addConstr(xBle * Ble.HM + xOrge * Orge.HM + xMais * Mais.HM + xBet * Betrave.HM + xTournesol * Tournesol.HM <= max_mch,name="contrainte d'heures de machine")
        model.addConstr(xBle <= surface, name="Ble")
        model.addConstr(xOrge <=  surface, name="Orge")
        model.addConstr(xMais <=  surface, name="Mais")
        model.addConstr(xBet <=  surface, name="Betrave")
        model.addConstr(xTournesol <=  surface, name="Tournesol")

        model.optimize()
        print(model.ObjVal)

        results = {
            "objVal":model.objVal,
            "xBle": xBle.X,
            "xOrge": xOrge.X,
            "xMais": xMais.X,
            "xBet": xBet.X,
            "xTournesol": xTournesol.X
        }

        return results
"""
if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = PL1_Ui()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
"""