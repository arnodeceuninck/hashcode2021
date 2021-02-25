from collections import OrderedDict


class System:
    streets: set = list()  # Lijst van streets
    cars: list = list()  # Lijst van cars
    intersections: list = []
    duration: int = 0


class Intersection:
    incoming: list = []  # list of streets
    outgoing: list = []
    id: int = 0
    schedule: OrderedDict = OrderedDict()  # Keys zijn straatnamen, values green light durations


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

    # simulation variables
    current_street: Street = 0
    street_position: int = 0
