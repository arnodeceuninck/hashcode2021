def scheduler(system):
    for intersection in system.getIntersections():
        for incoming_street in intersection.incoming:
            # schedule incoming street in round robin
            intersection.schedule[incoming_street.name] = 1
    return system

def filter_streets(system):
    visited_streets = []
    for car in system.cars:
        visited_streets.extend(car.streets)

    set(visited_streets)
    return visited_streets


def scheduler_without_redundant_streets(system):
    visited_streets = filter_streets(system)
    for intersection in system.intersectionsdict.values():
        for incoming_street in intersection.incoming:
            if incoming_street in visited_streets:
                # schedule incoming street in round robin
                intersection.schedule[incoming_street.name] = 1
    return system
