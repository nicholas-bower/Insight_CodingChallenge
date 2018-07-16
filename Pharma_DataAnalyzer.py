import pandas as pd
import argparse
from decimal import Decimal

parser = argparse.ArgumentParser(description='ST processing options.', conflict_handler="resolve")

#### Read In parameters####
parser.add_argument('-i', '--input', default='./input/reduced_de_cc_data.txt', help='Input file location.', type=str)
parser.add_argument('-o', '--output', default='./output/top_cost_drug.txt', help='Output file location.', type=str)
parser.add_argument('-n', '--n_entries', default=-1, help='Number of entries to run on(enter -1 for all entries)',
                    type=int)
parser.add_argument('-h', '--header', default=1, help='Indicate the location of the header line (0 for no header)',
                    type=int)
args = parser.parse_args()  # pass the parameters to a new variable

####Create arrays of column names ####
inputColNames = ['id', 'prescriber_last_name', 'prescriber_first_name', 'drug_name', 'drug_cost']
outputColNames = ['drug_name', 'n_prescribers', 'total_cost']

tempList = []  # Create an array from which we build our data frame

####Read the input file,####
####if the user passes a negative number, read the full file, otherwise, read the specified lines  ####
if args.n_entries < 0:
    inframe = pd.read_csv(args.input, header=args.header, sep=",", names=inputColNames)
else:
    inframe = pd.read_csv(args.input, header=args.header, nrows=args.n_entries, sep=",", names=inputColNames)

# Combine the first and last names to ensure different prescribers with the same last name are differentiated properly
inframe['prescriber_full_name'] = inframe['prescriber_last_name'] + ' ' + inframe['prescriber_first_name']

inframe = inframe.groupby('drug_name')

for drug, group in inframe:
    nPrescribers = group['prescriber_full_name'].nunique()  # count the number of unique prescribers for each drug
    totalCost = Decimal(group['drug_cost'].sum())  # Calculate the total cost of each drug and convert to decimal
    totalCost = round(totalCost, 2)  # total cost is rounded to prevent problems caused when summing floats
    tempList.append([drug, nPrescribers, totalCost])  # array is appended to our temp array containing data of interest

####Create a data frame from our 2d array, and sort it by total cost, from highest to lowest####
outframe = pd.DataFrame(tempList, columns=outputColNames)
outframe = outframe.sort_values('total_cost', ascending=False)

outframe.to_csv(args.output, header=outputColNames, index=None, sep=',', mode='w+')  # create the output file
