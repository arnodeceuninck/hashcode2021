from models import System, Intersection

def scheduler(system):
    for intersection in system.intersections:
        for incoming_street in intersection.incoming:
            # TODO: schedule incoming street in round robin
            intersection.schedule[incoming_street] = 1
    return system
