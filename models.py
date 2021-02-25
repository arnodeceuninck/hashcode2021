from collections import OrderedDict


class System:
    streets: set = list()  # Lijst van streets
    cars: list = list()  # Lijst van cars
    intersections: list = []
    duration: int = 0
    points: int = 0
    

    def findStreetWithName(self, name):
        for street in self.streets:
            if street.name == name:
                return street
        raise Exception("Invalid street name")

class Intersection:
    incoming: list = []  # list of streets
    outgoing: list = []
    id: int = 0
    schedule: OrderedDict = OrderedDict()  # Keys zijn straatnamen, values green light durations

    # simulation variables
    all_red: bool = True  # check if all lights are red, initialization phase
    current_green = 0  # street which has current green light

    def __init__(self, id):
        self.id = id


class Street:
    length: int = 0
    name: str = ""
    begin: Intersection = 0
    end: Intersection = 0

    # simulation variables
    light: int = 0  # 0 if light is red, else time light has been green
    visited_street: bool = False


class Car:
    streets: list = []

    def getNextStreet(self, street):
        for i in range(len(self.streets)):
            if self.streets[i] == street:
                return self.streets[i+1]

    # simulation variables
    current_street: Street = 0
    street_position: int = 0
