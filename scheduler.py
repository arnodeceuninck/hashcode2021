from simulation import *


def scheduler(system):
    for intersection in system.getIntersections():
        for incoming_street in intersection.incoming:
            # schedule incoming street in round robin
            intersection.schedule[incoming_street.name] = 1
    return system

def schedule_e(system):
    for intersection in system.getIntersections():
        for incoming_street in intersection.incoming:
            if incoming_street.name.find('ejj'):
                pass
            else:
                intersection.schedule[incoming_street.name] = 1
    return system


def scheduler_basil(system):
    update_counter(system.cars)
    for intersection in system.getIntersections():
        for incoming_street in intersection.incoming:
            # schedule incoming street in round robin
            if incoming_street.count == 0:
                intersection.schedule[incoming_street.name] = 1
            else:
                intersection.schedule[incoming_street.name] = incoming_street.count
    return system


def scheduler_without_redundant_streets(system):
    for intersection in system.getIntersections():
        for incoming_street in intersection.incoming:
            if incoming_street.visited_street:
                # schedule incoming street in round robin
                intersection.schedule[incoming_street.name] = 1
    return system
