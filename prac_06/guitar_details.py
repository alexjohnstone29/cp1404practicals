
class GuitarDetails:
    def __init__(self):
        self.name = ""
        self.year = 0
        self.cost = 0

    def get_age(self, year):
        self.year = 2020 - year

    def is_vintage(self):
        age = self.year
        if age >= 50:
            return True
        else:
            return False

    def __str__(self):
        return "{}, ({}) : ${:,.2f}".format(self.name, self.year, self.cost)