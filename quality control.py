def covert (Read):
    outseq=[]
    infile1 = open(Read)
    for line in infile1:
        out = line.replace("\n", "")
        out = out.replace("\r", "")
        outseq.append(out)
    infile1.close()
    return outseq

def seqqulity(seq):
    goodquality= ['A','B','C','D','E','F','G','H','I','J','K']
    print(len(seq))
    length = len(seq)/4
    #print(length)
    length = int(length)
    print(length)
    for i in range(0,length):
        if len(seq[i * 4 + 3]) > 129:
            for j in range(0,130):
                if seq[i*4+3][j] not in goodquality:
                    mylist=list(seq[i*4+1])
                    mylist[j]='N'
                    seq[i*4+1] = ''.join(mylist)
    return seq


read = covert('Undetermined_S0_L001_R2_001.fastq')
Read = seqqulity(read)

MyFile=open('seqR2.txt','w')
for element in Read:
     MyFile.write(element)
     MyFile.write('\n')
MyFile.close()