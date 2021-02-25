from read_input import *
from scheduler import scheduler
from output import generate_output

if __name__ == '__main__':
    filename = "a.txt"
    system = read_file(f"input/{filename}")
    system = scheduler(system)
    generate_output(system, f"output/generated_{filename}")
    print(system)
