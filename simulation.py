def run_simulation(system):
    while system.duration > 0:
        # TODO: progress lights based on schedule
        for intersection in system.intersections:
            for street_name, light_duration in intersection.schedule:
                # if all lights are red, we are in init phase


        # TODO: progress cars
        # loop over cars
        for car in system.cars:
            # check if car is at the end of street
            if car.current_street.length != car.street_position:  # if car is not at the end at street
                car.street_position += 1
            else:
                # check if car is in front of red or green light
                if car.current_street.light == 0:
