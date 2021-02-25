from read_input import *
from scheduler import scheduler, scheduler_without_redundant_streets
from output import generate_output
from simulation import run_simulation

if __name__ == '__main__':
    for letter in "e":
        print('Starting: ', letter)
        filename = f"{letter}.txt"
        system = read_file(f"input/{filename}")
        system = scheduler(system)
        print('Running Simulation')
        # run_simulation(system)
        print('Scheduling')
        system = scheduler_without_redundant_streets(system)
        print('Writing Output')
        generate_output(system, f"output/generated_{filename}")
        print('Finishing: ', letter)
