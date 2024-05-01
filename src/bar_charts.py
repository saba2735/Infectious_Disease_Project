import sys
import argparse
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from vaccine_model import read_csv

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description=
                                     'Plot infection distribution for a specific age group')
    
    parser.add_argument('file_name', 
                        type=str, 
                        help='Path to the CSV file containing simulation results')
    
    parser.add_argument('age_group', 
                        type=str, 
                        help='Specify the age group (kids, adults, or grandparents)')
    
    parser.add_argument('output_file', 
                        type=str, 
                        help='Output file name')
    
    args = parser.parse_args()


    # Read the CSV file
    data = pd.read_csv(args.file_name)
    if args.age_group == 'kids':
        ve_data = pd.DataFrame({
            'R0_kids': data['R0_kids'].tolist() * 3,
            'Total_Infections': data['VE_0_kids'].tolist() + data['VE_0.8_kids'].tolist() + data['VE_1_kids'].tolist(),
            'VE': ['VE 0'] * len(data) + ['VE 0.8'] * len(data) + ['VE 1'] * len(data)
        })
        # Plot side-by-side bar plot for the specified age group
        sns.barplot(x='R0_kids', y='Total_Infections', hue='VE', data=ve_data)
        plt.title(f'Infection Distribution for {args.age_group}')
        plt.xlabel('R0')
        plt.ylabel('Total Infections')
        plt.legend(title='Vaccine Efficacy (VE)')
        plt.savefig(args.output_file)
        
    if args.age_group == 'adults':
            # Combine data for different VE values into a single DataFrame
        ve_data = pd.DataFrame({
            'R0_adults': data['R0_adults'].tolist() * 3,
            'Total_Infections': data['VE_0_adults'].tolist() + data['VE_0.8_adults'].tolist() + data['VE_1_adults'].tolist(),
            'VE': ['VE 0'] * len(data) + ['VE 0.8'] * len(data) + ['VE 1'] * len(data)
        })
        # Plot side-by-side bar plot for the specified age group
        sns.barplot(x='R0_adults', y='Total_Infections', hue='VE', data=ve_data)
        plt.title(f'Infection Distribution for {args.age_group}')
        plt.xlabel('R0')
        plt.ylabel('Total Infections')
        plt.legend(title='Vaccine Efficacy (VE)')
        plt.savefig(args.output_file)
    
    if args.age_group == 'grandparents':
        ve_data = pd.DataFrame({
            'R0_grandparents': data['R0_grandparents'].tolist() * 3,
            'Total_Infections': data['VE_0_grandparents'].tolist() + data['VE_0.8_grandparents'].tolist() + data['VE_1_grandparents'].tolist(),
            'VE': ['VE 0'] * len(data) + ['VE 0.8'] * len(data) + ['VE 1'] * len(data)
        })
        # Plot side-by-side bar plot for the specified age group
        sns.barplot(x='R0_grandparents', y='Total_Infections', hue='VE', data=ve_data)
        plt.title(f'Infection Distribution for {args.age_group}')
        plt.xlabel('R0')
        plt.ylabel('Total Infections')
        plt.legend(title='Vaccine Efficacy (VE)')
        plt.savefig(args.output_file)
        
    print(f"Plot saved as '{args.output_file}'")

if __name__ == '__main__':
    main()
