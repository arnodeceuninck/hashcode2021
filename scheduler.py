def scheduler(system):
    for intersection in system.intersections:
        for incoming_street in intersection.incoming:
            # schedule incoming street in round robin
            intersection.schedule[incoming_street.name] = 1
    return system

def scheduler_without_redundant_streets(system):
    for intersection in system.intersections:
        for incoming_street in intersection.incoming:
            if incoming_street.visited_street:
                # schedule incoming street in round robin
                intersection.schedule[incoming_street.name] = 1
    return system
