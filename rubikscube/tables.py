import rubikscube.move_table as move_table
import rubikscube.pruning_table as pruning_table

class Table:
    def __init__(self):
        self.coMove, self.eoMove, self.udMove1 = move_table.phase1()
        self.coPrune = pruning_table.generate(self.coMove)
        self.eoPrune = pruning_table.generate(self.eoMove)
        self.udPrune1 = pruning_table.generate(self.udMove1)
