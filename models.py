from collections import OrderedDict


class System:
    streets: set = list()  # Lijst van streets
    cars: list = list()  # Lijst van cars
    intersections: list = []
    duration: int = 0


class Car:
    streets: list = []


class Intersection:
    incoming: list = []  # list of streets
    outgoing: list = []
    id: int = 0


class Schedule:
    intersection_id: list = []
    schedule: OrderedDict = OrderedDict()  # Keys zijn straatnamen, values green light durations


class Street:
    length: int = 0
    name: str = ""
    begin: Intersection = 0
    end: Intersection = 0
