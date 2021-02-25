from collections import OrderedDict


class System:
    streetsdict: dict = dict()  # Lijst van streets
    cars: list = list()  # Lijst van cars
    intersectionsdict: dict = dict()
    duration: int = 0
    points: int = 0

    def __repr__(self):
        return f"Streets: {self.streetsdict}\n Cars: {self.cars}\n Intersections: {self.intersectionsdict}\n " \
               f"Duration: {self.duration}\n Points: {self.points}"


    # def findStreetWithName(self, name):
    #     # StopIteration Exception means no street found
    #     return next(filter(lambda street: street.name == name, self.streets))

    # def getIntersectionFromId(self, id):
    #     return next(filter(lambda intersection: intersection.id == id, self.intersections))


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
        self.incoming = []
        self.outgoing = []
        self.schedule = OrderedDict()

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

    def getNextStreet(self, street):
        for i in range(len(self.streets)):
            if self.streets[i] == street:
                return self.streets[i+1]

    # simulation variables
    current_street: Street = 0
    street_position: int = 0

    def __init__(self):
        self.streets = []
        self.current_street: Street = 0
        self.street_position: int = 0

