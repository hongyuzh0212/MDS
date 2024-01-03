These are the code for analyze MDS data with the UCS HPC system
Python codes have been optimized for minimal changes needed for each set of sample
  The user needs to input the infomation about insert sequence, pimer design and processor requested before the run
Shell codes are needed for HPC system
  It is suggest to request the largemem partition for dealing with Hiseq/Novaseq data
  The processor request is default at 60 and can be adjusted if needed

To analyze the MDS data, the user should have filled all the input information and run the shell barcodelargdn.job followed by finalseq.job to have mutation spots identified as "T" and unmutated spots identified as "."

Additional codes could be helpful for other analysis
1.quality control.py: extact the reads with quality score >=32. For nucleotide with lower quality score, the code would change it into "N" and can be filtered out for later analysis
2.mutation distribute 3motif.py: from the finalseq.py result, this code can identify the mutation happened at each motif and one can compare the mutability of enzyem on certain motifs along the insert 
