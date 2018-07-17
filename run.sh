#!/bin/bash
#This simply runs the program
#I've included the default arguments so they can more easily be changed if need be
python ./src/pharmacy_counting.py python /src/Pharma_DataAnalyzer.py -i ./input/reduced_de_cc_data.txt -h 1 -n -1 -o ./output/top_cost_drug.txt
