# We used Dr. Smays StemFiles to help write this program.
#Ethan and I shared screens in order to complete this code.
from rankine import rankine


def main():
    # Define the properties for the first Rankine cycle (saturated vapor entering turbine)
    p_high_1 = 8000  # high pressure in kPa
    p_low_1 = 8  # low pressure in kPa
    t_high_1 = None  # Temperature is not specified, so it's assumed saturated steam

    # Instantiate the first Rankine cycle object
    rankine_cycle_1 = rankine(p_low=p_low_1, p_high=p_high_1, t_high=t_high_1, name='Rankine Cycle 1: Saturated Vapor')

    # Calculate efficiency for the first cycle and print the summary
    efficiency_1 = rankine_cycle_1.calc_efficiency()
    print(f"Efficiency of {rankine_cycle_1.name}: {efficiency_1:.2f}%")
    rankine_cycle_1.print_summary()
    print("-----------------------------------------------------")

    # Define the properties for the second Rankine cycle (superheated steam entering turbine)
    # For this, we assume the temperature is 1.7 times the saturation temperature at p_high
    # However, the actual temperature value needs to be determined based on steam tables or an equation of state
    # This is a placeholder since the calculation or lookup to determine T from 1.7*T_sat is not implemented here
    p_high_2 = 8000  # high pressure in kPa
    p_low_2 = 8  # low pressure in kPa
    # Assuming we've looked up Tsat for p_high and found it, then calculated t_high_2 as 1.7 * Tsat
    # For demonstration, we're directly setting a hypothetical value for t_high_2
    t_high_2 = 1.7 * 250  # Placeholder for 1.7*Tsat, assuming Tsat at p_high is 250°C

    # Instantiate the second Rankine cycle object
    rankine_cycle_2 = rankine(p_low=p_low_2, p_high=p_high_2, t_high=t_high_2,
                              name='Rankine Cycle 2: Superheated Vapor')

    # Calculate efficiency for the second cycle and print the summary
    efficiency_2 = rankine_cycle_2.calc_efficiency()
    print(f"Efficiency of {rankine_cycle_2.name}: {efficiency_2:.2f}%")
    rankine_cycle_2.print_summary()


if __name__ == "__main__":
    main()