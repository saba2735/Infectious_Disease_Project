import numpy as np
import matplotlib.pyplot as plt

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
    Inf = [I]
    Rec = [R]
    Vax = [V]
    time = [init_t]
    
    # Forward Euler method
    for t in np.arange(init_t, final_t, dt):
        # Update equations for S, I, R, V
        dS_dt = -beta * S * I / N
        
        if VE == 0:
            # For VE = 0, LM behaves like regular SIR
            dI_dt = (beta * S * I / N)+(beta*V*I*(1-VE))/N -(gamma*I)/N
            dV_dt = 0  # No change in vaccinated individuals
        elif VE == 0.8: 
            dI_dt = (beta * S * I/ N) +(beta*V*I*(1-VE))/N-(gamma*I)/N
            dV_dt = (-beta*I*(1-VE))*0.8
        elif VE == 1:
            # When VE is 1, no new infections and everyone is vaccinated
            dI_dt = 0  # No change in infected individuals
            dV_dt = 0  # No change in vaccinated individuals
        else: 
            dI_dt = (beta * S * I / N) +(beta*V*I*(1-VE))/N-(gamma*I)/N
            dV_dt = -beta*V*I*(1-VE)
        
        # Update values using Euler method
        S += dt * dS_dt
        I += dt * dI_dt
        R += dt * gamma * I
        V += dt * dV_dt
        
        Sus.append(S)
        Inf.append(I)
        Rec.append(R)
        Vax.append(V)
        time.append(t + dt)
    
    total_infections = max(Inf)
    
    return time, Sus, Inf, Rec, Vax, total_infections

def All_or_Nothing_model(R_0, N, VE):
    infectious_period = 14
    beta = R_0 / infectious_period
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
            dI_dt = (beta * S * I / N)+(beta*V*I*(1-VE))/N -(gamma*I)/N
            dV_null_dt = 0 # No change in vaccinated individuals
            dR_dt = gamma * I
            dV_all_dt = 0  # No change in vaccinated individuals
        elif VE == 0.8: 
            dI_dt = (beta * S * I)/ N + (beta*V*I*(1-VE))/N-(gamma*I)/N
            dV_null_dt =0.8 
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
            dV_all_dt = N * VE * (-beta * S * I / N) # Corrected vaccination rate for VE != 0
        

        S += dt * dS_dt
        I += dt * dI_dt
        R += dt * dR_dt
        V_null += dt * dV_null_dt
        V_all += dt * dV_all_dt
        
        Sus.append(S)
        Inf.append(I)
        Rec.append(R)
        Vax_null.append(V_null)
        Vax_all.append(V_all)
        time.append(t + dt)
    
    total_infections = max(Inf)
    
    return time, Sus, Inf, Rec, Vax_null, Vax_all, total_infections

def main():
    # Parameters
    R0_kids = 2
    R0_adults = 2
    R0_grandparents = 2
    VE_vals = [0, 0.8, 1]
    N_kids = 30
    N_adults = 55
    N_grandparents = 60
    total_population = N_kids + N_adults + N_grandparents
    
    contact_matrix = np.array([[20, 2, 2],
                               [2, 1, 2],
                               [2, 2, 1]])
    
    for VE in VE_vals:
        # Run LM and ANM simulations for kids
        lm_data_kids = leaky_model(R0_kids, N_kids, VE)
        anm_data_kids = All_or_Nothing_model(R0_kids, N_kids, VE)
        # Extract cumulative infectious populations
        lm_total_infections_kids = round(lm_data_kids[5], 0)  # Last value of infected from LM data
        anm_total_infections_kids = round(anm_data_kids[6], 0)  # Last value of infected from ANM data
        
        # Run LM and ANM simulations for adults
        lm_data_adults = leaky_model(R0_adults, N_adults, VE)
        anm_data_adults = All_or_Nothing_model(R0_adults, N_adults, VE)
        # Extract cumulative infectious populations
        lm_total_infections_adults = round(lm_data_adults[5], 0)  # Last value of infected from LM data
        anm_total_infections_adults = round(anm_data_adults[6], 0)  # Last value of infected from ANM data
        
        # Run LM and ANM simulations for grandparents
        lm_data_grandparents = leaky_model(R0_grandparents, N_grandparents, VE)
        anm_data_grandparents = All_or_Nothing_model(R0_grandparents, N_grandparents, VE)
        # Extract cumulative infectious populations
        lm_total_infections_grandparents = round(lm_data_grandparents[5], 0)  # Last value of infected from LM data
        anm_total_infections_grandparents = round(anm_data_grandparents[6], 0)  # Last value of infected from ANM data
        
        print(f'VE={VE}')
        print(f'Total infections for kids: {lm_total_infections_kids}, {anm_total_infections_kids}')
        print(f'Total infections for adults: {lm_total_infections_adults}, {anm_total_infections_adults}')
        print(f'Total infections for grandparents: {lm_total_infections_grandparents}, {anm_total_infections_grandparents}\n')
            
if __name__ == '__main__':
    main()
