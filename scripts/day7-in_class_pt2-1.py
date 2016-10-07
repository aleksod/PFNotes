class Car():

    def __init__(self, model, color, tank_size):
        self.model = model
        self.color = color
        self.tank_size = tank_size
        self.gallons_of_gas = self.tank_size # We're assuming its tank is full.

    def drive(self, miles_driven):
        self.gallons_of_gas -= miles_driven / 10.
