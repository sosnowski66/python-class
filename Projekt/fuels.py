import enum
from datetime import datetime

class FuelType(enum.Enum):
    petrol = "Benzyna"
    diesel = "Diesel"
    gasoline = "Gaz"


class Fuel:

    def __init__(self, name=FuelType.petrol, price=0):
        self.name = name
        self.price = price
        self.date = datetime.date(datetime.now())

    def __str__(self):
        return "{0} - {1} zł/l".format(self.name, self.price)

    def __repr__(self):
        return "{0} - {1} zł/l".format(self.name, self.price)

