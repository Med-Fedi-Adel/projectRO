# import numpy as np
# import pandas as pd

# import gurobipy as gp
# from gurobipy import GRB

# # Parameters

# years = [1, 2, 3, 4, 5]
# mines = [1, 2, 3, 4]

# royalties = {1: 5e6, 2: 4e6, 3: 4e6, 4: 5e6}
# capacity = {1: 2e6, 2: 2.5e6, 3: 1.3e6, 4: 3e6}
# quality  = {1: 1.0, 2: 0.7, 3: 1.5, 4: 0.5}
# target = {1: 0.9, 2: 0.8, 3: 1.2, 4: 0.6, 5: 1.0}
# time_discount = {year: (1/(1+1/10.0)) ** (year-1) for year in years}

# max_mines = 3
# price = 10

# mining = gp.Model('Mining')

# blend = mining.addVars(years, name="Blend")
# extract = mining.addVars(years, mines, name="Extract")
# working = mining.addVars(years, mines, vtype=GRB.BINARY, name="Working")
# available = mining.addVars(years, mines, vtype=GRB.BINARY, name="Available")


# #1. Operating Mines

# OperatingMines = mining.addConstrs((working.sum(year, '*') <= max_mines for year in years), "Operating_mines")

# #2. Quality

# Quality = mining.addConstrs((gp.quicksum(quality[mine]*extract[year, mine] for mine in mines)
#                    == target[year]*blend[year] for year in years), "Quality")

# #3. Mass Conservation

# MassConservation = mining.addConstrs((extract.sum(year, '*') == blend[year] for year in years), "Mass Conservation")

# #4. Mine Capacity

# MineCapacity = mining.addConstrs((extract[year, mine] <= capacity[mine]*working[year, mine] for year, mine in extract), "Capacity")

# # Open to operate
# OpenToOperate = mining.addConstrs((working[year, mine] <= available[year, mine] for year, mine in available), "Open to Operate")

# # Shutdown Mine
# ShutdownMine = mining.addConstrs((available[year+1, mine] <= available[year, mine]
#                    for year, mine in available if year < years[-1]), "Shut down")

# #0. Objective function
# obj = gp.quicksum(price*time_discount[year]*blend[year] for year in years) \
# - gp.quicksum(royalties[mine] * time_discount[year] * available[year, mine] for year, mine in available)
# mining.setObjective(obj, GRB.MAXIMIZE)

# mining.optimize()


# rows = years.copy()
# columns = mines.copy()
# extraction = pd.DataFrame(columns=columns, index=rows, data=0.0)

# for year, mine in extract.keys():
#     if (abs(extract[year, mine].x) > 1e-6):
#         extraction.loc[year, mine] = np.round(extract[year, mine].x / 1e6, 2)
# extraction

# rows = years.copy()
# sales = pd.DataFrame(columns=['Sales'], index=rows, data=0.0)

# for year in blend.keys():
#     if (abs(blend[year].x) > 1e-6):
#         sales.loc[year, 'Sales'] = np.round(blend[year].x / 1e6, 2)
# sales

# mining.write("mining-output.sol")
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
import numpy as np
import pandas as pd

import gurobipy as gp
from gurobipy import GRB

class MiningOptimizer(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Mining Optimization GUI')
        self.setGeometry(100, 100, 400, 300)

        self.input_layout = QVBoxLayout()
        self.add_input_fields()
        self.add_buttons()

        self.setLayout(self.input_layout)

    def add_input_fields(self):
        self.years_input = QLineEdit()
        self.years_input.setPlaceholderText('Number of years')
        self.input_layout.addWidget(self.years_input)

        self.mines_input = QLineEdit()
        self.mines_input.setPlaceholderText('Number of mines')
        self.input_layout.addWidget(self.mines_input)

        self.royalty_capacity_quality_btn = QPushButton('Add Royalty, Capacity, Quality')
        self.royalty_capacity_quality_btn.clicked.connect(self.add_royalty_capacity_quality_input)
        self.input_layout.addWidget(self.royalty_capacity_quality_btn)

        self.target_value_btn = QPushButton('Add Target Value for Year')
        self.target_value_btn.clicked.connect(self.add_target_value_input)
        self.input_layout.addWidget(self.target_value_btn)

        self.max_mines_input = QLineEdit()
        self.max_mines_input.setPlaceholderText('Max Mines')
        self.input_layout.addWidget(self.max_mines_input)

        self.price_input = QLineEdit()
        self.price_input.setPlaceholderText('Price')
        self.input_layout.addWidget(self.price_input)

    def add_royalty_capacity_quality_input(self):
        num_mines =0
        if(self.mines_input.text()):
            num_mines = int(self.mines_input.text()) or 0
        for _ in range(num_mines):
            mine_layout = QHBoxLayout()

            royalty_input = QLineEdit()
            royalty_input.setPlaceholderText('Royalty')
            mine_layout.addWidget(royalty_input)

            capacity_input = QLineEdit()
            capacity_input.setPlaceholderText('Capacity')
            mine_layout.addWidget(capacity_input)

            quality_input = QLineEdit()
            quality_input.setPlaceholderText('Quality')
            mine_layout.addWidget(quality_input)

            self.input_layout.insertLayout(self.input_layout.indexOf(self.royalty_capacity_quality_btn)+1, mine_layout)

    def add_target_value_input(self):
        num_years = 0 
        if(self.years_input.text()):
            num_years = int(self.years_input.text())
        for year in range(1, num_years + 1):
            target_layout = QHBoxLayout()

            target_label = QLabel(f'Target value for Year {year}:')
            target_layout.addWidget(target_label)

            target_input = QLineEdit()
            target_input.setPlaceholderText('Target Value')
            target_layout.addWidget(target_input)

            self.input_layout.insertLayout(self.input_layout.indexOf(self.target_value_btn)+1, target_layout)
    def add_buttons(self):
        self.optimize_btn = QPushButton('Optimize')
        self.optimize_btn.clicked.connect(self.run_optimization)
        self.input_layout.addWidget(self.optimize_btn)

    def run_optimization(self):
        # Get user inputs
        num_years = int(self.years_input.text())
        num_mines = int(self.mines_input.text())
        max_mines = int(self.max_mines_input.text())
        price = float(self.price_input.text())

        royalties = []
        capacities = []
        qualities = []
        targets = []

        # Gather royalty, capacity, and quality inputs for each mine
        for i in range(num_mines):
            royalties.append(float(self.input_layout.itemAt(self.input_layout.indexOf(self.royalty_capacity_quality_btn)+1+i).layout().itemAt(0).widget().text()))
            capacities.append(float(self.input_layout.itemAt(self.input_layout.indexOf(self.royalty_capacity_quality_btn)+1+i).layout().itemAt(1).widget().text()))
            qualities.append(float(self.input_layout.itemAt(self.input_layout.indexOf(self.royalty_capacity_quality_btn)+1+i).layout().itemAt(2).widget().text()))

        # Gather target values for each year
        for i in range(num_years):
            targets.append(float(self.input_layout.itemAt(self.input_layout.indexOf(self.target_value_btn)+1+i).layout().itemAt(1).widget().text()))

        # Perform optimization
        years = list(range(1, num_years + 1))
        mines = list(range(1, num_mines + 1))

        print(years) 
        print(mines)

        print(royalties)
        print(capacities)
        print(qualities)
        print(targets)
        print(max_mines)
        print(price)

        royalties_dict = {mine: royalties[i] for i, mine in enumerate(mines)}
        capacities_dict = {mine: capacities[i] for i, mine in enumerate(mines)}
        qualities_dict = {mine: qualities[i] for i, mine in enumerate(mines)}
        targets_dict = {year: targets[i] for i, year in enumerate(years)}

        time_discount = {year: (1/(1+1/10.0)) ** (year-1) for year in years}

        mining = gp.Model('Mining')

        blend = mining.addVars(years, name="Blend")
        extract = mining.addVars(years, mines, name="Extract")
        working = mining.addVars(years, mines, vtype=GRB.BINARY, name="Working")
        available = mining.addVars(years, mines, vtype=GRB.BINARY, name="Available")

        OperatingMines = mining.addConstrs((working.sum(year, '*') <= max_mines for year in years), "Operating_mines")
        Quality = mining.addConstrs((gp.quicksum(qualities_dict[mine]*extract[year, mine] for mine in mines)
                                    == targets_dict[year]*blend[year] for year in years), "Quality")
        MassConservation = mining.addConstrs((extract.sum(year, '*') == blend[year] for year in years), "Mass Conservation")
        MineCapacity = mining.addConstrs((extract[year, mine] <= capacities_dict[mine]*working[year, mine]
                                        for year, mine in extract), "Capacity")
        OpenToOperate = mining.addConstrs((working[year, mine] <= available[year, mine] for year, mine in available), "Open to Operate")
        ShutdownMine = mining.addConstrs((available[year+1, mine] <= available[year, mine] for year, mine in available if year < years[-1]), "Shut down")

        obj = gp.quicksum(price*time_discount[year]*blend[year] for year in years) \
            - gp.quicksum(royalties_dict[mine] * time_discount[year] * available[year, mine] for year, mine in available)
        mining.setObjective(obj, GRB.MAXIMIZE)

        mining.optimize()

        # After running mining.optimize()
        if mining.status == GRB.OPTIMAL:
            # Objective Value
            print("Objective Value:", mining.objVal)
            # Format objective value in dollars
            objective_value_dollars = '${:,.2f}'.format(mining.objVal)

            # Display objective value
            objective_label = QLabel(f'Objective Value: {objective_value_dollars}')
            self.input_layout.addWidget(objective_label)

            

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MiningOptimizer()
#     window.show()
#     sys.exit(app.exec_())
