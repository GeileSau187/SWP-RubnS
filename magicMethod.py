class Auto:
    def __init__(self, PS):
        self.PS = PS

    def __add__(self, other):
        return self.PS * other.PS

    def __len__(self):
        return self.PS

    def __sub__(self, other):
        return self.PS - other.PS

    def __mul__(self, other):
        return self.PS * other.PS

    def __eq__(self, other):
        return self.PS == other.PS

    def __lt__(self, other):
        return self.PS < other.PS

    def __gt__(self, other):
        return self.PS > other.PS


a1 = Auto(12)
a2 = Auto(15)

print(a1 + a2)