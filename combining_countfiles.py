#!/usr/bin/env python3

#this script will take any number of files from the command line. 
#the script assumes that the input will have gene names as 1st column
#and num_reads on the 2nd column

 

import sys
import re

#this block of code will parse through all of the files provided, and store the information into a dictionary of lists.
#the key containing the gene names is 'gene_names'
#the key containing num_reads will be the name of the input file that the reads came from with a number after it.
file_number = 0
mydict = {}
with open('combined_counts.txt', 'w') as outputfile:
	for files in sys.argv[1:]:
		file_number+=1
		num_reads_list = []
		gene_name_list = []
		with open(files, 'r') as inputfile:
			for line in inputfile:
				line = line.rstrip()
				if re.search(r"\|", line):
					line_list = line.split('\t')
					gene_name_list.append(line_list[0])
					num_reads_list.append(line_list[1])
		mydict['gene_names'] = gene_name_list
		mydict[files] = num_reads_list

#the following block will take the information stored in the dictionary
#and then write them out into the output file.
#this portion adds the header
	for index in mydict:
		outputfile.write(index+'\t')
	outputfile.write('\n')
#looping through the indices
#specifically, loops through for the number of items there are in the gene_names list
#then takes the 1st entry for each list of each key such that the 1st column will be gene name
#2nd column will be the numreads from one of the files, etc.... 
	for x in range(len(mydict['gene_names'])):
		for index in mydict:
			outputfile.write(mydict[index][x])
			outputfile.write('\t')
#at the end of each line, a new line character is inputted
		outputfile.write('\n')

#this block of code will take the combined_counts.txt file produced from the code above
#then will remove all genes with zero expression values. 
with open('combined_counts.txt', 'r') as inputfile, open('combined_counts_filtered.txt', 'w') as output2:
	for line in inputfile:
		line = line.rstrip()
		if "gene_names" in line:
			output2.write(line+'\n')
		if re.search(r"\|", line):
			line_list = line.split('\t')
			count_list = line_list[1:file_number+1]
			floated_count_list = [float(item) for item in count_list]
			if sum(floated_count_list) != 0:
				output2.write(line+'\n')

