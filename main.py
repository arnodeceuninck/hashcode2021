from read_input import *
from scheduler import scheduler, scheduler_without_redundant_streets
from output import generate_output
from simulation import run_simulation

if __name__ == '__main__':
    for letter in "a":
        print('Starting: ', letter)
        filename = f"{letter}.txt"
        system = read_file(f"input/{filename}")
        run_simulation(system)
        system = scheduler_without_redundant_streets(system)
        generate_output(system, f"output/generated_{filename}")
        print('Finishing: ', letter)
