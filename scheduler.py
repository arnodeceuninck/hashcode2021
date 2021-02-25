def scheduler(system):
    for intersection in system.intersections:
        for incoming_street in intersection.incoming:
            # schedule incoming street in round robin
            intersection.schedule[incoming_street] = 1
    return system
