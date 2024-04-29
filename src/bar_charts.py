import argparse
import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description=
                                     'Plot infection distribution for a specific age group')
    
    parser.add_argument('file_name', 
                        type=str, 
                        help='Path to the CSV file containing simulation results',
                        required=True)
    
    parser.add_argument('age_group', 
                        type=str, 
                        help='Specify the age group (kids, adults, or grandparents)',
                        required=True)
    
    parser.add_argument('output_file', 
                        type=str, 
                        help='Output file name',
                        required=True)
    
    args = parser.parse_args()
    
    # Read the CSV file
    data = pd.read_csv(args.file_name)
    
    # Filter data for the specified age group
    filtered_data = data[['R0_kids', 'R0_adults', 'R0_grandparents', f'TI_{args.age_group}_VE_0', f'TI_{args.age_group}_VE_0.8', f'TI_{args.age_group}_VE_1']]
    
    # Melt the DataFrame to convert it to long format
    melted_data = pd.melt(filtered_data, id_vars=['R0_kids', 'R0_adults', 'R0_grandparents'], var_name='VE', value_name='Total_Infections')
    
    # Extract age group from the column name
    melted_data['Age_Group'] = args.age_group
    
    # Plot histogram for the specified age group
    sns.histplot(melted_data, x='Total_Infections', hue='VE', bins=15, alpha=0.7)
    plt.title(f'Infection Distribution for {args.age_group}')
    plt.xlabel('Total Infections')
    plt.ylabel('Frequency')
    #plt.legend(title='VE') Need to have this show for the different R0 values I think
    plt.savefig(args.output_file)
    
    print(f"Plot saved as '{args.output_file}'")

if __name__ == '__main__':
    main()
