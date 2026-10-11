#Machine eli puhuva ääni class
class Machine():
    def __init__(self, hp):
        self.hp = hp

    def Machine_hp_muutos(self, muutos):
        self.hp = self.hp - muutos
        return

masiina = Machine(100)




