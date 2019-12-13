# SMARTseq_Pipeline
Pipeline for taking demultiplexed SMARTseq data, then creating count matrices to be used for Seurat and other analysis tools.
Before starting, you will need the following on your computer:
Python3
Salmon

## Running Salmon to Map and Quantify Reads
If you haven't already, you need to create a Salmon index of your transcriptome. This will allow Salmon to parse through your transcriptome to pseudomap reads. 
Make sure your transcriptome is in .fasta format. 
Go to the same directory as your transcriptome, and on the command line type the following:

	salmon index -t yourtranscriptomefile -i nameofyourindexedtranscriptome

Place all fastq files into a single folder. In the command line, go to this directory, and run the following for each sample:

	salmon quant -i nameofyourindexedtranscriptome -l A -1 read1 -2 read2 -p 4 -o nameofyouroutputfile

## Creating count matrix
Each of the salmon output files contains a file named 'quant.sf'.
Use a loop to re-name all of these files into the following format: 'samplename_quantfile'
Take all of the re-named files and place them into a new directory. 
Place the 'quant_file_extract.py' and 'combining_countfiles.py' scripts into the same folder. 

On the command line, type the following:

	python3 quant_file_extract.py *quantfile

This will create new files that contains two columns: gene name and num reads.

Next, type the following in the command line:

	python3 combining_countfiles.py *counts

This will create two files. combined_counts.txt contains all num reads columns concatenated with eachother. combined_counts.txt has all genes with zero expression filtered out. 

The filtered combined_counts.txt file can now be used as input for Seurat. 
If using Scanpy, make sure to transpose this table after import. 

