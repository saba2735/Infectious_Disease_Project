import csv
import numpy as np

def read_csv(file_name):
    data = []
    with open(file_name, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    return data

def calculate_re(R0, N, VE):
    return R0 * N*(1 - VE)

def main():
    # Parameters
    R0_kids_range = np.linspace(1.7, 2, num=5)
    R0_adults_range = np.linspace(1, 2, num=5)
    R0_grandparents_range = np.linspace(1, 1.4, num=5)
    VE_vals = [0, 0.8, 1]
    N_kids = 30 
    N_adults = 55 
    N_grandparents = 60

    # Initialize the CSV file and write headers
    with open('re_calculation_results.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        headers = ['R0_kids', 'R0_adults', 'R0_grandparents', 'VE_kids', 'VE_adults', 'VE_grandparents',
                   'Re_kids', 'Re_adults', 'Re_grandparents']
        writer.writerow(headers)

        # Loop through the R0 values for kids
        for R0_kids in R0_kids_range:
            # Loop through the R0 values for adults
            for R0_adults in R0_adults_range:
                # Loop through the R0 values for grandparents
                for R0_grandparents in R0_grandparents_range:
                    # Loop through the VE values
                    for VE_kids in VE_vals:
                        for VE_adults in VE_vals:
                            for VE_grandparents in VE_vals:
                                Re_kids = calculate_re(R0_kids, N_kids, VE_kids)
                                Re_adults = calculate_re(R0_adults, N_adults, VE_adults)
                                Re_grandparents = calculate_re(R0_grandparents, N_grandparents, VE_grandparents)
                                row = [R0_kids, R0_adults, R0_grandparents, VE_kids, VE_adults, VE_grandparents,
                                       Re_kids, Re_adults, Re_grandparents]
                                writer.writerow(row)

if __name__ == '__main__':
    main()
