"""Simulate a simple population model. Start with population = 100. Each "year" (loop iteration), 
   the population increases by 10% (population *= 1.10) but also decreases by a fixed number loss = 15. 
   The simulation should stop if the population drops to 50 or below, OR if it exceeds 1000. 
   To prevent potential infinite loops (e.g., if the population oscillates or grows very slowly), 
   add a safety break: the simulation must also stop if it runs for more than max_years = 100. 
   Write a function run_simulation(initial_pop, growth_rate, loss, lower_bound, upper_bound, max_years) 
   that performs this simulation. The function should print the population each year and a final message 
   indicating why it stopped (hit lower bound, hit upper bound, or max years reached). 
   Return the final population and the number of years simulated.

   Concepts Reinforced: while loop with complex condition, multiple exit conditions, floating-point 
   arithmetic considerations (use rounding or careful comparison), safety counter (break), 
   functions with multiple parameters, formatted printing, returning multiple values (tuple)."""

def run_simulation(initial_pop : int, growth_rate : float, loss : int, lower_bound : int, upper_bound : int, max_years : int) -> tuple[float,int]:
    """Simulate population changes - stops at population <= lower_bound or population > upper_bound or year > max_years"""
    year = 0
    population = initial_pop
    while year < max_years:
        population *= growth_rate
        population -= loss
        if population > upper_bound:
            print(f"Population is of {round(population,2)} and surpassed the upper bound of {upper_bound}")
            break
        if population <= lower_bound:
            print(f"Population is of {round(population,2)} and is under the lower bound of {lower_bound}")
            break
        year += 1
        if year == max_years:
            print(f"Max year {max_years} as been reached")

    return (round(population,2),year)

def print_simulation_result(result : tuple[float,int]) -> None:
    """Format result of the simulation"""
    if not result:
        return
    
    print("Simulation result :")
    print(f"Final population : {result[0]}")
    print(f"Number of years simulated : {result[1]}")

def main() -> None:
    """main function"""

    # Scenario 1: Reaches lower bound
    result = run_simulation(initial_pop=100, growth_rate=1.05, loss=10, lower_bound=80, upper_bound=1000, max_years=50)
    print_simulation_result(result)
    # Scenario 2: Reaches upper bound
    result = run_simulation(initial_pop=100, growth_rate=1.20, loss=5, lower_bound=50, upper_bound=200, max_years=50)
    print_simulation_result(result)
    # Scenario 3: Reaches max years (potential oscillation or slow change)
    result = run_simulation(initial_pop=100, growth_rate=1.10, loss=10, lower_bound=95, upper_bound=105, max_years=10)
    print_simulation_result(result)

if __name__ == "__main__":
    main()