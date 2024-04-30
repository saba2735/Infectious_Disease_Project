import csv
import numpy as np

# Function to simulate the SEIRS model with vaccination and waning immunity
def seirs_model(R0, N, VE_kids, VE_adults, VE_grandparents, waning_rate_kids, waning_rate_adults, waning_rate_grandparents):
    incubation_period = 5
    infectious_period = 14
    sigma = 1 / incubation_period
    gamma = 1 / infectious_period
    beta_kids = R0 / infectious_period
    beta_adults = R0 / infectious_period
    beta_grandparents = R0 / infectious_period
    
    # Initial number of susceptible, exposed, infectious, recovered individuals
    S_kids = N['kids']
    E_kids = np.random.randint(1, 31)  # Range: 1-30
    I_kids = np.random.randint(1, 31)  # Range: 1-30
    R_kids = 0
    
    S_adults = N['adults']
    E_adults = np.random.randint(1, 56)  # Range: 1-55
    I_adults = np.random.randint(1, 56)  # Range: 1-55
    R_adults = 0
    
    S_grandparents = N['grandparents']
    E_grandparents = np.random.randint(1, 61)  # Range: 1-60
    I_grandparents = np.random.randint(1, 61)  # Range: 1-60
    R_grandparents = 0
    
    # Lists to store results
    Inf_kids = [I_kids]
    Inf_adults = [I_adults]
    Inf_grandparents = [I_grandparents]
    
    # Total time steps
    final_t = 300
    # Time step size
    dt = 0.01
    
    # Forward Euler method
    for t in np.arange(0, final_t, dt):
        # Update equations for S, E, I, R
        
        # For kids
        dS_dt_kids = -beta_kids * S_kids * I_kids / N['kids'] + waning_rate_kids * R_kids
        dE_dt_kids = beta_kids * S_kids * I_kids / N['kids'] - sigma * E_kids
        dI_dt_kids = sigma * E_kids - gamma * I_kids
        dR_dt_kids = gamma * I_kids - waning_rate_kids * R_kids
        
        # For adults
        dS_dt_adults = -beta_adults * S_adults * I_adults / N['adults'] + waning_rate_adults * R_adults
        dE_dt_adults = beta_adults * S_adults * I_adults / N['adults'] - sigma * E_adults
        dI_dt_adults = sigma * E_adults - gamma * I_adults
        dR_dt_adults = gamma * I_adults - waning_rate_adults * R_adults
        
        # For grandparents
        dS_dt_grandparents = -beta_grandparents * S_grandparents * I_grandparents / N['grandparents'] + waning_rate_grandparents * R_grandparents
        dE_dt_grandparents = beta_grandparents * S_grandparents * I_grandparents / N['grandparents'] - sigma * E_grandparents
        dI_dt_grandparents = sigma * E_grandparents - gamma * I_grandparents
        dR_dt_grandparents = gamma * I_grandparents - waning_rate_grandparents * R_grandparents
        
        # Update values using Euler method
        
        # For kids
        S_kids += dt * dS_dt_kids
        E_kids += dt * dE_dt_kids
        I_kids += dt * dI_dt_kids
        R_kids += dt * dR_dt_kids
        
        # For adults
        S_adults += dt * dS_dt_adults
        E_adults += dt * dE_dt_adults
        I_adults += dt * dI_dt_adults
        R_adults += dt * dR_dt_adults
        
        # For grandparents
        S_grandparents += dt * dS_dt_grandparents
        E_grandparents += dt * dE_dt_grandparents
        I_grandparents += dt * dI_dt_grandparents
        R_grandparents += dt * dR_dt_grandparents
        
        # Append current infectious individuals to lists
        
        Inf_kids.append(I_kids)
        Inf_adults.append(I_adults)
        Inf_grandparents.append(I_grandparents)

    # Calculate peak infection for each group
    peak_infection_kids = np.max(Inf_kids)
    peak_infection_adults = np.max(Inf_adults)
    peak_infection_grandparents = np.max(Inf_grandparents)
    
    return peak_infection_kids, peak_infection_adults, peak_infection_grandparents

def main():
    # Parameters
    R0_kids_range = np.linspace(1.7, 2, num=5)
    R0_adults_range = np.linspace(1, 2, num=5)
    R0_grandparents_range = np.linspace(1, 1.4, num=5)  # Updated range for R0 values for grandparents
    VE_vals = [0, 0.8, 1]
    N_kids = 30
    N_adults = 55
    N_grandparents = 60
    
    # Waning immunity rates for each group
    # Waning rate for kids ranges from 6 months to 3 years (0.002 to 0.1)
    waning_rate_kids_range = np.linspace(0.002, 0.1, num=5)
    # Waning rate for adults ranges from 3 to 7 years (0.0014 to 0.033)
    waning_rate_adults_range = np.linspace(0.0014, 0.033, num=5)
    # Waning rate for grandparents ranges from 6 months to 1 year (0.0035 to 0.07)
    waning_rate_grandparents_range = np.linspace(0.0035, 0.07, num=5)
    
    # Initialize the CSV file and write headers
    with open('SEIRS_results.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        headers = ['R0_kids','R0_adults','R0_grandparents','Peak_Infection_kids','Peak_Infection_adults','Peak_Infection_grandparents']
        for VE in VE_vals:
            headers.extend([f'VE_{VE}_kids',f'VE_{VE}_adults',f'VE_{VE}_grandparents'])
        writer.writerow(headers)
        
        # Loop through the R0 values for kids
        for R0_kids in R0_kids_range:
            # Loop through the R0 values for adults
            for R0_adults in R0_adults_range:
                # Loop through the R0 values for grandparents
                for R0_grandparents in R0_grandparents_range:
                    # Loop through the waning rate values for kids
                    for waning_rate_kids in waning_rate_kids_range:
                        # Loop through the waning rate values for adults
                        for waning_rate_adults in waning_rate_adults_range:
                            # Loop through the waning rate values for grandparents
                            for waning_rate_grandparents in waning_rate_grandparents_range:
                                # Create a row for each combination of R0 and waning rate values
                                row = [R0_kids, R0_adults, R0_grandparents]
                                # Calculate peak infections for each VE value
                                for VE in VE_vals:
                                    # Calculate peak infections using the SEIRS model with vaccination and waning immunity
                                    peak_infection_kids, peak_infection_adults, peak_infection_grandparents = seirs_model(R0_kids, {'kids': N_kids, 'adults': N_adults, 'grandparents': N_grandparents}, VE, VE, VE, waning_rate_kids, waning_rate_adults, waning_rate_grandparents)
                                    # Append the results to the row
                                    row.extend([peak_infection_kids, peak_infection_adults, peak_infection_grandparents])
                                # Write the row to the CSV file
                                writer.writerow(row)

if __name__ == '__main__':
    main()
