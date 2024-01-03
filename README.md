These are the codes for analyzing MDS data with the UCS HPC system
Python codes have been optimized for minimal changes needed for each set of sample
  The user needs to input the information about the insert sequence, primer design, and processor requested before the run
Shell codes are needed for the HPC system
  It is suggested to request the largemem partition for dealing with Hiseq/Novaseq data
  The processor request is defaulted at 60 and can be adjusted if needed

To analyze the MDS data, the user should have filled in all the input information and run the shell barcodelargdn.job followed by finalseq.job to have mutation spots identified as "T" and unmutated spots identified as "."

Additional codes could be helpful for other analyses but may need modifications for certain sequence designs or arrangements:
1. quality control.py: extract the reads with a quality score >=32. For nucleotides with lower quality scores, the code would change into "N" and can be filtered out for later analysis
2. mutation distribute 3motif.py: from the finalseq.py result, this code can identify the mutation that happened at each motif and one can compare the mutability of enzyme on certain motifs along the insert 
