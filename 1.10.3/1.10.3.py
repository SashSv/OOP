class ECom:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def save_name(self):
        print(f"Клиент - '{self.name}' Баланс - '{self.balance}'")

client_1 = ECom("Иван Петров", 10)

client_1.save_name()


