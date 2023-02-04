class Guest:
    def __init__(self, name, cash, favourite_song=None):
        self.name = name
        self.cash = cash
        self.favourite_song = favourite_song

    def can_afford_to_pay(self, amount):
        return self.cash >= amount

    def pay_cash(self, amount):
        if self.can_afford_to_pay(amount):
            self.cash -= amount
            return True
        else:
            return False
