class Plane():

    def __init__(self, destination, departure_city, trip_distance):
        self.destination = destination
        self.departure_city = departure_city
        self.trip_distance = trip_distance

    def fly(self):
        self.departure_city, self.destination = (
        self.destination, self.departure_city)
