import enum
import date

class FuelType(enum.Enum):
    petrol = "Benzyna"
    diesel = "Diesel"
    gasoline = "Gaz"


class Fuel:

    def __init__(self, type=FuelType.petrol, price=0):
        self.type = type
        self.price = price
        self.date = date.today()
    def __str__(self):
        return "{0} - {1}".format(self.type, self.price)

    def __repr__(self):
        return "{0} - {1}".format(self.type, self.price)
