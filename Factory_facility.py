import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
from itertools import product
from math import sqrt
import gurobipy as gp
from gurobipy import GRB

class FacilityFactoryApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Probleme d''emplacement des installations')
        self.layout = QVBoxLayout()

        self.num_customers_input = QLineEdit()
        self.num_facilities_input = QLineEdit()
        self.cost_per_mile_input = QLineEdit()

        self.layout.addWidget(QLabel("Nombre des clients :"))
        self.layout.addWidget(self.num_customers_input)
        self.layout.addWidget(QLabel("Nombres des emplacements candidats :"))
        self.layout.addWidget(self.num_facilities_input)
        self.layout.addWidget(QLabel("Cout par mile:"))
        self.layout.addWidget(self.cost_per_mile_input)

        self.add_input_fields_button = QPushButton('Ajouter les champs d''entrée')
        self.add_input_fields_button.setStyleSheet("background-color: #4CAF50; color: white;")
        self.add_input_fields_button.clicked.connect(self.add_input_fields)
        self.layout.addWidget(self.add_input_fields_button)

        self.remove_input_fields_button = QPushButton('Supprimer les champs d''entrée')
        self.remove_input_fields_button.setStyleSheet("background-color: #f44336; color: white;")
        self.remove_input_fields_button.clicked.connect(self.remove_input_fields)
        self.layout.addWidget(self.remove_input_fields_button)

        self.run_button = QPushButton('Exécuter l''algorithme')
        self.run_button.setStyleSheet("background-color: #008CBA; color: white;")
        self.run_button.clicked.connect(self.run_algorithm)
        self.layout.addWidget(self.run_button)

        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        self.layout.addWidget(self.result_text)

        self.setLayout(self.layout)
        self.show()

        self.customer_inputs = []
        self.facility_inputs = []

    def add_input_fields(self):
        num_customers = int(self.num_customers_input.text())
        num_facilities = int(self.num_facilities_input.text())
        for i in range(num_customers):
            customer_layout = QHBoxLayout()
            customer_layout.addWidget(QLabel(f"Client {i + 1} (x, y):"))
            x_input = QLineEdit()
            y_input = QLineEdit()
            customer_layout.addWidget(x_input)
            customer_layout.addWidget(y_input)
            self.layout.addLayout(customer_layout)
            self.customer_inputs.append((x_input, y_input))
        for i in range(num_facilities):
            facility_layout = QHBoxLayout()
            facility_layout.addWidget(QLabel(f"Emplacement {i + 1} (x, y, cout d''installation):"))
            x_input = QLineEdit()
            y_input = QLineEdit()
            cost_input = QLineEdit()
            facility_layout.addWidget(x_input)
            facility_layout.addWidget(y_input)
            facility_layout.addWidget(cost_input)
            self.layout.addLayout(facility_layout)
            self.facility_inputs.append((x_input, y_input, cost_input))

    def remove_input_fields(self):
        for input_widgets in self.customer_inputs:
            for widget in input_widgets:
                widget.clear() 
                widget.deleteLater()
        for input_widgets in self.facility_inputs:
            for widget in input_widgets:
                widget.clear()  
                widget.deleteLater()
        self.customer_inputs = []
        self.facility_inputs = []


    def run_algorithm(self):
        num_customers = int(self.num_customers_input.text())
        num_facilities = int(self.num_facilities_input.text())
        cost_per_mile = float(self.cost_per_mile_input.text())

        customers = []
        facilities = []
        setup_cost = []

        for i in range(num_customers):
            customer_input = self.customer_inputs[i]
            x = float(customer_input[0].text())
            y = float(customer_input[1].text())
            customers.append((x, y))

        for i in range(num_facilities):
            facility_input = self.facility_inputs[i]
            x = float(facility_input[0].text())
            y = float(facility_input[1].text())
            cost = float(facility_input[2].text())
            facilities.append((x, y))
            setup_cost.append(cost)

        cartesian_prod = list(product(range(num_customers), range(num_facilities)))
        shipping_cost = {(c,f): cost_per_mile*compute_distance(customers[c], facilities[f]) for c, f in cartesian_prod}

        m = gp.Model('facility_location')
        select = m.addVars(num_facilities, vtype=GRB.BINARY, name='Select')
        assign = m.addVars(cartesian_prod, ub=1, vtype=GRB.CONTINUOUS, name='Assign')

        m.addConstrs((assign[(c,f)] <= select[f] for c,f in cartesian_prod), name='Setup2ship')
        m.addConstrs((gp.quicksum(assign[(c,f)] for f in range(num_facilities)) == 1 for c in range(num_customers)), name='Demand')

        m.setObjective(select.prod(setup_cost)+assign.prod(shipping_cost), GRB.MINIMIZE)

        m.optimize()

        self.result_text.clear()
        self.result_text.append("Resultat :")
        for facility in select.keys():
            if (abs(select[facility].x) > 1e-6):
                self.result_text.append(f"Construire a la localisation : {facility + 1}.")
        
        for customer, facility in assign.keys():
            if (abs(assign[customer, facility].x) > 1e-6):
                self.result_text.append(f"le client {customer + 1} reçoit {round(100*assign[customer, facility].x, 2)} % de ces demandes a partir du candidat {facility + 1}.")

def compute_distance(loc1, loc2):
    dx = loc1[0] - loc2[0]
    dy = loc1[1] - loc2[1]
    return sqrt(dx*dx + dy*dy)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FacilityFactoryApp()
    sys.exit(app.exec_())
