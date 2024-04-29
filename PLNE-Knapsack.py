import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QTextEdit
import gurobipy as gp


class KnapsackSolver:
    def __init__(self):
        self.model = gp.Model('Knapsack')
        self.items = []
        self.capacity = 0
        self.n = 0
        self.x = None

    def add_item(self, name, weight, value):
        self.items.append((name, weight, value))

    def solve(self):
        self.n = len(self.items)
        self.x = self.model.addVars(self.n, vtype=gp.GRB.BINARY, name='x')
        self.model.setObjective(sum(item[2] * self.x[i] for i, item in enumerate(self.items)), gp.GRB.MAXIMIZE)
        self.model.addConstr(sum(item[1] * self.x[i] for i, item in enumerate(self.items)) <= self.capacity, 'capacity_constraint')
        self.model.optimize()

    def get_solution(self):
        selected_items = [self.items[i][0] for i in range(self.n) if self.x[i].x == 1]
        total_value = sum(self.items[i][2] for i in range(self.n) if self.x[i].x == 1)
        total_weight = sum(self.items[i][1] for i in range(self.n) if self.x[i].x == 1)
        return selected_items, total_value, total_weight


class KnapsackUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Knapsack Problem Solver")
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        
        
        desc1 = QLabel("Tu es un voleur qui a un sac à dos de capacité limitée et qui veut voler des objets de valeur. ")
        desc2 = QLabel("Chaque objet a un poids et une valeur.")
        desc3 = QLabel("Le but est de maximiser la valeur totale des objets volés sans dépasser la capacité du sac à dos.")
        layout.addWidget(desc1)
        layout.addWidget(desc2)
        layout.addWidget(desc3)
        
        

        # Add item button
        self.add_item_button = QPushButton("Ajouter un objet")
        self.add_item_button.clicked.connect(self.add_item)
        layout.addWidget(self.add_item_button)

        # Input widgets for each item
        self.item_inputs_layout = QVBoxLayout()
        layout.addLayout(self.item_inputs_layout)

        # Capacity input
        self.capacity_input = QLineEdit()
        layout.addWidget(QLabel("Capacité:"))
        layout.addWidget(self.capacity_input)

        # Solve button
        self.solve_button = QPushButton("Resoudre le problème")
        self.solve_button.clicked.connect(self.solve)
        layout.addWidget(self.solve_button)

        # Output text area
        self.output_text = QTextEdit()
        layout.addWidget(QLabel("Sortie:"))
        layout.addWidget(self.output_text)

        self.setLayout(layout)

    def add_item(self):
        item_layout = QHBoxLayout()

        name_input = QLineEdit()
        weight_input = QLineEdit()
        value_input = QLineEdit()

        item_layout.addWidget(QLabel("Nom:"))
        item_layout.addWidget(name_input)
        item_layout.addWidget(QLabel("Poids:"))
        item_layout.addWidget(weight_input)
        item_layout.addWidget(QLabel("Valeur:"))
        item_layout.addWidget(value_input)

        self.item_inputs_layout.addLayout(item_layout)

    def solve(self):
        solver = KnapsackSolver()
        for i in range(self.item_inputs_layout.count()):
            item_layout = self.item_inputs_layout.itemAt(i).layout()
            name_input = item_layout.itemAt(1).widget()
            weight_input = item_layout.itemAt(3).widget()
            value_input = item_layout.itemAt(5).widget()
            solver.add_item(name_input.text(), int(weight_input.text()), int(value_input.text()))

        solver.capacity = int(self.capacity_input.text())
        solver.solve()
        selected_items, total_value, total_weight = solver.get_solution()

        output = f"Objets Selectionnés: {selected_items}\nValeur Totale: {total_value}\nPoids Totale: {total_weight}"
        self.output_text.setPlainText(output)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    knapsack_ui = KnapsackUI()
    knapsack_ui.show()
    sys.exit(app.exec_())
