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
        # Plot histogram for the specified age group
        sns.scatterplot(x=data['R0_kids'], y=data[['TI_kids_VE_0', 'TI_kids_VE_0.8', 'TI_kids_VE_1']], bins=15, alpha=0.7)
        plt.title(f'Infection Distribution for {args.age_group}')
        plt.xlabel('Total Infections')
        plt.ylabel('Frequency')
        #plt.legend(title='VE') Need to have this show for the different R0 values I think
        plt.savefig(args.output_file)
    else:
        print('no plots here ...')
    print(f"Plot saved as '{args.output_file}'")

if __name__ == '__main__':
    main()
