import sys
import argparse
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description=
                                     'Plot line plot for Vaccine Efficacy (VE) or Effective Reproduction Number (Re)')
    
    parser.add_argument('file_name', 
                        type=str, 
                        help='Path to the CSV file containing simulation results')
    
    parser.add_argument('age_group', 
                        type=str, 
                        help='Specify the age group (kids, adults, or grandparents)')
    
    parser.add_argument('ve_or_re', 
                        type=str, 
                        help='Prefix for output file names')
    
    # parser.add_argument('output_file', 
    #                     type=str, 
    #                     help='Prefix for output file names')
    
    args = parser.parse_args()
    
    # Read the CSV file
    data = pd.read_csv(args.file_name)

    print(data.head())
    if args.ve_or_re == 've':
        sns.scatterplot(data=data, x='R0_kids', y='VE_kids')
        plt.xlabel('R0_kids')
        plt.ylabel('Vaccine Efficacy (VE) for Kids')
        plt.title('Scatter Plot of R0 vs VE for Kids')
        plt.savefig('rekids.png')
    elif args.ve_or_re == 're':
        sns.scatterplot(data=data, x='R0_kids', y='Re_kids')
        plt.xlabel('R0_kids')
        plt.ylabel('Effective Reproduction Number (Re) for Kids')
        plt.title('Scatter Plot of R0 vs Re for Kids')
        plt.savefig('vekids.png')
if __name__ == '__main__':
    main()
