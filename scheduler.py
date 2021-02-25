from simulation import *
import math


def scheduler(system):
    for intersection in system.getIntersections():
        for incoming_street in intersection.incoming:
            # schedule incoming street in round robin
            intersection.schedule[incoming_street.name] = 1
    return system


def scheduler_basil(system):
    update_counter(system.cars)
    for intersection in system.getIntersections():
        for incoming_street in intersection.incoming:
            if incoming_street.count == 0:
                continue
            # schedule incoming street in round robin
            intersection.schedule[incoming_street.name] = math.ceil(incoming_street.count / 6) if incoming_street.count else 1
    return system


def scheduler_without_redundant_streets(system):
    for intersection in system.getIntersections():
        for incoming_street in intersection.incoming:
            if incoming_street.visited_street:
                # schedule incoming street in round robin
                intersection.schedule[incoming_street.name] = 1
    return system
