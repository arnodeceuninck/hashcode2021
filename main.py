from read_input import *
from scheduler import scheduler
from output import generate_output

if __name__ == '__main__':
    for letter in "ab":
        print('Starting: ', letter)
        filename = f"{letter}.txt"
        system = read_file(f"input/{filename}")
        system = scheduler(system)
        generate_output(system, f"output/generated_{filename}")
        print('Finishing: ', letter)
