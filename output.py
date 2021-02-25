from models import System, Intersection


def generate_output(system: System, filenmae):
    # TODO: assuming you specify a schedule for all intersections
    file = open(filenmae, "w")
    append(file, len(system.intersections))
    for intersection in system.intersections:
        append_intersection(file, intersection)
    file.close()


def append(file, text):
    return file.write(f"{text}\n")


def append_intersection(file, intersection):
    assert isinstance(intersection, Intersection)
    append(file, intersection.id)
    schedule = intersection.schedule
    append(file, len(schedule))  # E, number of incoming streets
    append_schedule(file, schedule)


def append_schedule(file, schedule):
    for street, duration in schedule.items():
        assert isinstance(street, str)
        assert street != ""
        assert isinstance(duration, int)
        append(file, f"{street} {duration}")
