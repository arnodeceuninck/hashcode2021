from collections import OrderedDict


class System:
    streets: set = list()  # Lijst van streets
    cars: list = list()  # Lijst van cars
    intersections: list = []
    duration: int = 0
    points: int = 0

    def __repr__(self):
        return f"Streets: {self.streets}\n Cars: {self.cars}\n Intersections: {self.intersections}\n " \
               f"Duration: {self.duration}\n Points: {self.points}"
    

    def findStreetWithName(self, name):
        for street in self.streets:
            if street.name == name:
                return street
        raise Exception("Invalid street name")

    def getIntersectionFromId(self, id):
        assert self.intersections[id].id == id
        return self.intersections[id]

class Intersection:
    incoming: list = []  # list of streets
    outgoing: list = []
    id: int = 0
    schedule: OrderedDict = OrderedDict()  # Keys zijn straatnamen, values green light durations

    def __init__(self, id):
        self.id = id

    def __repr__(self):
        return f"Id: {self.id}"




class Street:
    length: int = 0
    name: str = ""
    begin: Intersection = 0
    end: Intersection = 0
    # simulation variables
    light: int = 0  # 0 if light is red, else time light has been green
    visited_street: bool = False

    def __repr__(self):
        return f"Length: {self.length} Name: {self.name}\n"


class Car:
    streets: list = []

    # simulation variables
    current_street: Street = 0
    street_position: int = 0
