def run_simulation(system):
    while system.duration > 0:
        # progress lights based on schedule
        for intersection in system.intersections:
            next_light_green = False  # if this is True, the next light needs to be put on green
            for street_name, light_duration in intersection.schedule.items():
                current_street = system.findStreetWithName(street_name)
                # if all lights are red, we are in init phase
                if intersection.all_red:
                    intersection.all_red = False
                    assert light_duration > 0  # if light_duration is 0, i need to fix this
                    current_street.light += 1
                    intersection.current_green = current_street
                else:
                    # check if new light needs to be put on green
                    if next_light_green:
                        current_street.light += 1
                        intersection.current_green = current_street
                        next_light_green = False
                    # check if current light is green, else progress
                    elif intersection.current_green != current_street:
                        continue
                    else:
                        # current light is green, check if it has reached the end
                        if light_duration != current_street.light:
                            current_street.light += 1
                        else:
                            current_street.light = 0
                            next_light_green = True

        # progress cars
        for car in system.cars:
            # if car has not been put on street yet
            if car.current_street == 0:
                car.current_street = car.streets[0]
                car.current_street.visited_street = True
            # check if car is at the end of street
            if car.current_street.length != car.street_position:  # if car is not at the end at street
                car.street_position += 1
            else:
                # check if car is in front of red or green light
                if car.current_street.light == 0:  # light is red
                    continue
                else:
                    # light is green
                    # get outgoing street of car, and put it on this street
                    outgoing_street = car.getNextStreet(car.current_street)
                    car.current_street = outgoing_street
                    car.street_position = 0
                    car.current_street.visited_street = True

        system.duration -= 1

