class Guest:
    def __init__(self, name, cash):
        self.name = name
        self.cash = cash

    def can_afford_to_pay(self, amount):
        return self.cash >= amount
