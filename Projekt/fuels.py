import enum


class FuelType(enum.Enum):
    petrol = "Benzyna"
    diesel = "Diesel"
    gasoline = "Gaz"


class Fuel:

    def __init__(self, type=FuelType.petrol, price=0):
        self.type = type
        self.price = price

    
