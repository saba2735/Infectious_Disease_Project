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
            dI_dt = (beta * S * I)/ N + (beta*V_null*I)/N-(gamma*I)/N
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
    R0_vals = [3, 4, 5]
    VE_vals = [0, 0.8, 1]
    N = 300000
    
    for R0 in R0_vals:
        for VE in VE_vals:
            # Run LM and ANM simulations
            lm_data = leaky_model(R0, N, VE)
            anm_data = All_or_Nothing_model(R0, N, VE)
            
            # Extract cumulative infectious populations
            lm_total_infections = round(lm_data[5], 0)  # Last value of infected from LM data
            anm_total_infections = round(anm_data[6], 0)  # Last value of infected from ANM data
            
            print(f'R_0={R0}, VE={VE}')
            print(f'Total infections for LM: {lm_total_infections}')
            
            if VE == 0:
                print(f'Total Infections for ANM: {anm_total_infections}')  # Print ANM value only when VE = 0
            elif VE == 1:
                print(f'Total Infections for ANM: {anm_total_infections}')  # Print ANM value only when VE = 1
            elif VE == 0.8:
                print(f'Total Infections for ANM: {anm_total_infections}')  # Print ANM value only when VE = 0.8
            
            # Plotting (unchanged)
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
    
            # SIR dynamic curves (unchanged)
            ax1.plot(lm_data[0], lm_data[2], color='red', label='Infected-LM')
            ax1.plot(anm_data[0], anm_data[2], color='blue', label='Infected-ANM')
            ax1.set_xlabel('Time (days)')
            ax1.set_ylabel('Infected Population (people)')
            ax1.set_title(f'Infected Population of a vaccine model using SIR of R0={R0}, VE={VE}')
            ax1.legend()
    
            # Bar Plots (unchanged)
            ax2.plot(['LM', 'ANM'], [lm_total_infections, anm_total_infections])
            ax2.set_xlabel('Time (days)')
            ax2.set_ylabel('Total infected population (People)')
            ax2.set_title(f'Total infectious population of R0={R0}, VE = {VE}')
    
            plt.tight_layout()
    
            # Save plot to file (unchanged)
            filename = f'Leaky Model vs. All or Nothing model for VE_{VE}_R0_{R0}.png'
            fig.savefig(filename)
            print(f'Graph saved as {filename}\n')

if __name__ == '__main__':
    main()

