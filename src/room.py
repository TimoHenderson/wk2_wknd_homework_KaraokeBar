from src.transaction import Transaction


class Room:
    def __init__(self, name, capacity, entry_fee=5.00):
        self.name = name
        self.capacity = capacity
        self.entry_fee = entry_fee
        self.songs = []
        self.guests = []
        self.transactions = []

    def add_song(self, song):
        self.songs.append(song)

    def check_in(self, guest):
        checked_in = False
        response = ""
        if self.has_space():
            if self.charge_guest("Entry", guest, self.entry_fee):
                self.guests.append(guest)
                checked_in = True
                response = f"{guest.name} checked in to {self.name}. "
                if self.favourite_song_in_room(guest):
                    response += "Their favourite song is in this room!"
            else:
                response = f"{guest.name} doesn't have enough money for {self.name}. "
        else:
            response = f"There's no space in {self.name}. "
        return checked_in, response

    def check_out(self, guest):
        self.guests.remove(guest)

    def has_space(self):
        return len(self.guests) < self.capacity

    def favourite_song_in_room(self, guest):
        return guest.favourite_song in self.songs

    def charge_guest(self, item, guest, amount):
        if guest.can_afford_to_pay(amount):
            guest.pay_cash(amount)
            self.transactions.append(Transaction(item, guest, amount))
            return True
        else:
            return False
