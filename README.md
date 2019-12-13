# SMARTseq_Pipeline
Pipeline for taking demultiplexed SMARTseq data, then creating count matrices to be used for Seurat and other analysis tools
Before starting, you will need the following on your computer:
Python3
Salmon

# # Running Salmon to Map and Quantify Reads
If you haven't already, you need to create a Salmon index of your transcriptome. This will allow Salmon to parse through your transcriptome to pseudomap reads. 
Make sure your transcriptome is in .fasta format. 
Go to the same directory as your transcriptome, and on the command line type the following:

'''salmon index -t yourtranscriptomefile -i nameofyourindexedtranscriptome'''

Place all fastq files into a single folder. In the command line, go to this directory, and run the following for each sample:

'''salmon quant -i nameofyourindexedtranscriptome -l A -1 read1 -2 read2 -p 4 -o nameofyouroutputfile'''


