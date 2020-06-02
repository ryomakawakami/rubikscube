import rubikscube.move_table as move_table
import rubikscube.pruning_table as pruning_table

class Table:
    def __init__(self):
        self.coMove, self.eoMove, self.udMove1 = move_table.phase1()
        self.coPrune = pruning_table.generate(self.coMove)
        self.eoPrune = pruning_table.generate(self.eoMove)
        self.udPrune1 = pruning_table.generate(self.udMove1)

        self.cpMove, self.epMove, self.udMove2 = move_table.phase2()
        self.cpPrune = pruning_table.generate(self.cpMove)
        self.epPrune = pruning_table.generate(self.epMove)
        self.udPrune2 = pruning_table.generate(self.udMove2)
