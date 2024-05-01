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
    
    parser.add_argument('output_file', 
                        type=str, 
                        help='Prefix for output file names')
    
    args = parser.parse_args()

    data = pd.read_csv(args.file_name)
    
    if args.age_group == 'kids':
        sns.barplot(data=data, x='R0_kids', y='Re_kids')
        plt.xlabel('R0_kids')
        plt.ylabel('Effective Reproduction Number (Re)')
        plt.title('R0 vs Re')
        plt.savefig(args.output_file)
        
    if args.age_group == 'adults':
        sns.barplot(data=data, x='R0_adults', y='Re_adults')
        plt.xlabel('R0_adults')
        plt.ylabel('Effective Reproduction Number (Re)')
        plt.title('R0 vs Re')
        plt.savefig(args.output_file)
        
    if args.age_group == 'grandparents':
        sns.barplot(data=data, x='R0_grandparents', y='Re_grandparents')
        plt.xlabel('R0_grandparents')
        plt.ylabel('Effective Reproduction Number (Re)')
        plt.title('R0 vs Re')
        plt.savefig(args.output_file)
        
if __name__ == '__main__':
    main()
