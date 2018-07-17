# Insight Coding Challenge


This is a brief script written for the Insight Data Engineering Fellowship. I was presented with the problem of analyzing a sample pharmaceutical dataset. Input files provide the name of drugs, their prescribers and costs. Prospective fellows were tasked with creating new files that included the number of unique prescribers for each drug and their total cost. Though it was not specified by the assignment, I elected to sort the output file by cost, simply to make it easier to find the most expensive drugs.

The analysis is written in python, making use of the pandas data analysis library (the only library needed that doesn't come standard.) I have included a sample input file with 1000 entries, and the resulting output that is obtained by running the script on the sample. The sample file is a reduced version of a pharmaceutical provided by the facilitators of the fellowship selection process.

## Getting Started

As mentioned in the above section this is a very straight forward program to run, only requiring python, a properly formatted by input file, and the pandas package.

### Pandas
The Pandas package (for more information visit their [website](https://pandas.pydata.org/)) is an open source data analysis tool. The latest release can be downloaded using conda from conda-forge or the default channel: 
```
conda install pandas
```
or using PyPl
```
pip install pandas
```
### Input Files
This analysis takes input files formated in the following columns seperated by commas (',') :

id,prescriber_last_name,prescriber_first_name,drug_name,drug_cost

There is a sample printed in the bellow section and included in the /input/ file.

## Running Instructions
The program is fairly straightforward to run, taking only a few parameters. The defaults are set to run on the sample input, and save to the same location as the sample output. A full description of these parameters are displayed below. These defaults are written with the understanding that the code is being run from the directory containing the input and output files directories contained in this repository.
* -i point to the location of a properly .txt input file. If no input is specified the script will use the sample input
* -o point to the location where the output will be saved. If none is specified the script will overwrite the sample output.
* -h specify the location of the header line (aka a line in the input data file which labels each of the columns.) The sample file includes a header on the first line and presumably all inputs will be in this format, but on the off chance they aren't this argument has been included. If no header is present enter 0.
* -n how many entries from the input file to include in the analysis. For testing it is often useful to only run over a small subset of the data. Entering a negative number or not including this argument will simply make the script run on all input entries.

### Running with run.sh
Calling run.sh will simply run the script with the default arguments. To pass other arguments you must either change the run.sh file, or  simply run the script directly as described in the bellow section. It is important not to forget to change the permissions for the shell script to allow it to run.
```
chmod run.sh --x
./run.sh
```
### Running the script without use of the .sh script
An example run command looks like this running from the main directory:
```
python ./src/Pharma_DataAnalyzer.py -i ./input/reduced_de_cc_data.txt -h 1 -n 5 -o ./output/top_cost_drug.txt
```
This will take the first 5 lines of the sample input:
```
id,prescriber_last_name,prescriber_first_name,drug_name,drug_cost
1952310666,A'BODJEDI,ENENGE,ALPRAZOLAM,1964.49
1952310666,A'BODJEDI,ENENGE,AMANTADINE,1129.94
1952310666,A'BODJEDI,ENENGE,AMBIEN,4792.29
1952310666,A'BODJEDI,ENENGE,AMBIEN CR,4792.29
1952310666,A'BODJEDI,ENENGE,AMITRIPTYLINE HCL,692.78
```
and create the following output, saved as './output/top_cost_drug.txt'
```
drug_name,n_prescribers,total_cost
ARIPIPRAZOLE,1,8374.44
AMBIEN,1,4792.29
AMBIEN CR,1,4792.29
AMANTADINE,1,1129.94
AMITRIPTYLINE HCL,1,692.78
```



## My approach

Pandas is perfectly tailored to this challenge, to the extent that it almost feels like cheating. Pandas is able to use operations which work significantly more efficiently than line by line analysis methods using for or while loops. I was able to easily subdivide the dataset by drug name. From there I again used simple pandas methods to find the number of unique prescribers for each subdivision and sum up the total amount spent on each drug. After collecting all the needed information it was simply a matter of creating a new dataframe to sort and save to a new file, containing all the required information in the proper format.
