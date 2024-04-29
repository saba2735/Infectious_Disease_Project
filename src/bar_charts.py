import argparse
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from vaccine_model import plot_histogram

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Plot infection distribution for a specific age group')
    
    parser.add_argument('file_name', 
                        type=str, 
                        help='Path to the CSV file containing simulation results')
    
    parser.add_argument('age_group', 
                        type=str,
                        help='Specify the age group (kids, adults, or grandparents)')
    
    parser.add_argument('output_file', 
                        type=str, 
                        help='output file name')
    
    args = parser.parse_args()
    
    # Read the CSV file
    data = pd.read_csv(args.file_name)  # Corrected the argument name
    
    # Melt the DataFrame to convert it to long format
    melted_data = pd.melt(data, id_vars=['R0_kids', 'R0_adults', 'R0_grandparents'], var_name='Age_Group_and_VE', value_name='Total_Infections')
    
    # Extract age group and VE from the column 'Age_Group_and_VE'
    melted_data[['Age_Group', 'VE']] = melted_data['Age_Group_and_VE'].str.split('_', expand=True)
    
    # Drop the 'Age_Group_and_VE' column
    melted_data.drop(columns=['Age_Group_and_VE'], inplace=True)
    
    # Filter data for the specified age group
    filtered_data = melted_data[melted_data['Age_Group'] == args.age_group]
    
    # Plot histogram for the specified age group
    if args.age_group == 'kids':
        # Plot histogram
        sns.histplot(filtered_data, x='Total_Infections', hue='VE', bins=15, alpha=0.7)
        plt.title(f'Infection Distribution for {args.age_group}')  # Corrected variable reference
        plt.xlabel('Total Infections')
        plt.ylabel('Frequency')
        plt.legend(title='VE')
        plt.savefig(args.output_file)  # Corrected variable reference
        plot_histogram(filtered_data, 'TI_kids', args.output_file)  # Corrected function call
    elif args.age_group == 'adults':
        plot_histogram(filtered_data, 'TI_adults', args.output_file)  # Corrected function call
    elif args.age_group == 'grandparents':
        plot_histogram(filtered_data, 'TI_grandparents', args.output_file)  # Corrected function call
    else:
        print('Hmmm... No graphs here...')
    
    plt.savefig(args.output_file)  # Corrected the position to save the figure

if __name__ == '__main__':
    main()
