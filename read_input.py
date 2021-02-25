from models import *




def read_file(filename):
    system = System()
    with open(filename) as infile:
        firstline = infile.readline().strip().split(' ')
        system.duration = int(firstline[0])
        intersectioncount = int(firstline[1])
        streetcount = int(firstline[2])
        carcount = int(firstline[3])
        system.points = int(firstline[4])

        for i in range(intersectioncount):
            system.intersectionsdict[i] = Intersection(i)

        for i in range(streetcount):
            line = infile.readline().strip().split(' ')
            street = Street()
            street.begin = int(line[0])
            street.end = int(line[1])
            street.name = line[2]
            street.length = int(line[3])
            system.streetsdict[line[2]] = street
            system.intersectionsdict[int(line[0])].outgoing.append(street)
            system.intersectionsdict[int(line[1])].incoming[street] = 1

        for i in range(carcount):
            line = infile.readline().strip().split(' ')
            car = Car()
            for j in range(int(line[0])):
                car.streets.append(system.streetsdict[line[j + 1]])
            system.cars.append(car)

    return system

