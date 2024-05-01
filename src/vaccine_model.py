import csv
import numpy as np

def read_csv(file_name):
    data = []
    with open(file_name, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    return data

# Function to simulate the leaky model
def leaky_model(R0, N, VE):
    period_of_infection = 14
    gamma = 1 / period_of_infection
    beta = R0 / period_of_infection
    I = 1
    S = N - I
    R = 0
    V = 0
    final_t = 300
    init_t = 0
    dt = 0.01
    # Lists to store results
    Sus = [S]
    Rec = [R]
    Vax = [V]
    Inf = [I]
    time = [init_t]
    
    # Forward Euler method
    for t in np.arange(0, final_t, dt):
        # Update equations for S, I, R, V
        dS_dt = -beta * S * I / N
    
        if VE == 0:
            # For VE = 0, LM behaves like regular SIR
            dI_dt = (beta * S * I / N)+(beta*V*I*(1-VE))/N -(gamma*I)/N
            dV_dt = 0  # No change in vaccinated individuals
        elif VE == 0.8: 
            dI_dt = (beta * S * I / N)+(beta*V*I*(1-VE))/N -(gamma*I)/N
            dV_dt = (-beta*I*(1-VE))*N
        elif VE == 1:
            # When VE is 1, no new infections and everyone is vaccinated
            dI_dt = 0  # No change in infected individuals
            dV_dt = 0  # No change in vaccinated individuals
        else:
            dI_dt = (beta * S * I / N)+(beta*V*I*(1-VE))/N -(gamma*I)/N
            dV_dt = -beta * V * I * (1 - VE)*N
    
        # Update values using Euler method
        I += dt * dI_dt
        R += dt * gamma * I
        V += dt * dV_dt
        S += dt * dS_dt
    
        Sus.append(S)
        Inf.append(I)
        Rec.append(R)
        Vax.append(V)
        time.append(t+dt)

    # Calculate total infections correctly
    total_infections = np.max(Inf)

    return total_infections

# Function to simulate the all-or-nothing model
def All_or_Nothing_model(R0, N, VE):
    infectious_period = 14
    beta = R0 / infectious_period
    gamma = 1 / infectious_period
    I = 1
    R = 0
    V_null = 0
    V_all = N * VE
    S = N - I - V_all
    V = 0
    final_t = 300
    init_t = 0
    dt = 0.01
    
    # Lists to store results
    Sus = [S]
    Inf = [I]
    Rec = [R]
    Vax_null = [V_null]
    Vax_all = [V_all]
    time = [init_t]
    
    # Forward Euler method
    for t in np.arange(init_t, final_t, dt):
        # Update equations for S, I, R, V_null, and V_all
        dS_dt = -beta * S * I / N
        
        if VE == 0:
            # When VE is 0, ANM behaves like regular SIR
            dI_dt = (beta * S * I / N) + (beta * V * I * (1 - VE)) / N - (gamma * I) / N
            dV_null_dt = 0  # No change in vaccinated individuals
            dR_dt = gamma * I
            dV_all_dt = 0  # No change in vaccinated individuals
        elif VE == 0.8: 
            dI_dt = (beta * S * I / N) + (beta * V * I * (1 - VE)) / N - (gamma * I) / N
            dV_null_dt = 0.8
            dR_dt = gamma * I 
            dV_all_dt = 0.8
        elif VE == 1:
            # When VE is 1, no new infections and everyone is vaccinated
            dI_dt = 0  # No change in infected individuals
            dV_null_dt = 0  # No change in vaccinated individuals
            dR_dt = 0  # No change in recovered individuals
            dV_all_dt = 0  # No change in vaccinated individuals
        else:
            dI_dt = beta * S * I / N + beta * V_null * I / N - gamma * I
            dV_null_dt = -beta * V_null * I / N
            dR_dt = gamma * I
            dV_all_dt = N * VE * (-beta * S * I / N)  # Corrected vaccination rate for VE != 0
        
        # Update values using Euler method
        I += dt * dI_dt
        R += dt * dR_dt
        V_null += dt * dV_null_dt
        V_all += dt * dV_all_dt
        S += dt * dS_dt
        
        Sus.append(S)
        Inf.append(I)
        Rec.append(R)
        Vax_null.append(V_null)
        Vax_all.append(V_all)
        time.append(t + dt)
    
    # Calculate total infections correctly
    total_infections = np.max(Inf)
    
    return total_infections


def main():
    # Parameters
    R0_kids_range = np.linspace(1.7, 2, num=5)
    R0_adults_range = np.linspace(1, 2, num=5)
    R0_grandparents_range = np.linspace(1, 1.4, num=5)  # Updated range for R0 values for grandparents
    VE_vals = [0, 0.8, 1]
    N_kids = 30
    N_adults = 55
    N_grandparents = 60
    
    # Initialize the CSV file and write headers
    with open('simulation_results.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        headers = ['R0_kids','R0_adults','R0_grandparents']
        for VE in VE_vals:
            headers.extend([f'VE_{VE}_kids',f'VE_{VE}_adults',f'VE_{VE}_grandparents'])
        writer.writerow(headers)
        
        # Loop through the R0 values for kids
        for R0_kids in R0_kids_range:
            # Loop through the R0 values for adults
            for R0_adults in R0_adults_range:
                # Loop through the R0 values for grandparents
                for R0_grandparents in R0_grandparents_range:
                    # Create a row for each combination of R0 values
                    row = [R0_kids, R0_adults, R0_grandparents]
                    # Calculate total infections for each VE value
                    for VE in VE_vals:
                        # Calculate total infections using the leaky model for kids
                        lm_total_infections_kids = leaky_model(R0_kids, N_kids, VE)
                        # Calculate total infections using the leaky model for adults
                        lm_total_infections_adults = leaky_model(R0_adults, N_adults, VE)
                        # Calculate total infections using the all-or-nothing model for grandparents
                        lm_total_infections_grandparents = leaky_model(R0_grandparents, N_grandparents, VE)
                        # Append the results to the row
                        row.extend([lm_total_infections_kids, lm_total_infections_adults, lm_total_infections_grandparents])
                    # Write the row to the CSV file
                    writer.writerow(row)

if __name__ == '__main__':
    main()
