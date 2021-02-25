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

class Car:
    streets: list = []


class Intersection:
    incoming: list = []  # list of streets
    outgoing: list = []
    id: int = 0

    def __init__(self, id):
        self.id = id


class Schedule:
    intersection_id: list = []
    schedule: OrderedDict = OrderedDict()  # Keys zijn straatnamen, values green light durations


class Street:
    length: int = 0
    name: str = ""
    begin: Intersection = 0
    end: Intersection = 0
