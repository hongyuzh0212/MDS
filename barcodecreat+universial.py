### Need input
READ1 = '22095FL-08-02-01_S2_L006_R1_001.fastq'
READ2 ='22095FL-08-02-01_S2_L006_R2_001.fastq'

ORDER= 142
Primer1= 25
Primer2= 0
#######
Primer1EXTEND=Primer1-25
Primer2EXTEND=Primer2-0

FullLENGTH= ORDER+25 #default: 142 designed sequences with priming site and 25N barcode

R2ADD = FullLENGTH-130+Primer1EXTEND+Primer2EXTEND

R2MATCH1=FullLENGTH-125+Primer1EXTEND+Primer2EXTEND
R2MATCH2=FullLENGTH-135+Primer1EXTEND+Primer2EXTEND



def compbase(base):
    #Returns complement of base
    if base == "A":
        compbase = "T"
    elif base == "C":
        compbase = "G"
    elif base == "G":
        compbase = "C"
    elif base == "T":
        compbase = "A"
    else:
        compbase = base
        # if there's an N in the sequence, for example, keep the N
    return compbase

def compseq(seq):
    #Returns complement of seq
    comp = [] # empty list
    for base in seq:
        nuc = compbase(base)
        comp.append(nuc)
    compstr = "".join(comp)
    return compstr

def covert (read):
    out = []
    with open(read) as f:
        for idx, line in enumerate(f.read().splitlines()):
            if idx %4==1 :
                out.append(line)
    return out

def rev(seq):
    #Returns the reverse of seq
    return seq[::-1]

def revcomp(seq):
    #Returns the reverse complement of seq
    rv = rev(seq)
    rvcp = compseq(rv)
    return rvcp

def seqrevcomp (seq):
    out=[]
    for i in range(len(seq)):
            temp = revcomp(seq[i])
            out.append(temp)

    return out

def merge(read1,read2,r1headkeep,r2tailkeep): #merge the R1 and R2 sequence together
    out=[]
    for i in range(len(read1)):
        if read1[i][125:135] == read2[i][-R2MATCH1:-R2MATCH2]:
            temp= "".join([read1[i][0:r1headkeep],read2[i][-r2tailkeep:]])
            out.append(temp)
    return out


def final25(seq): #get the last 25 bases of the read. The last 25 reads are the barcodes
    MyList=[]
    for line in seq:
        if line[-(35+Primer2):-(25+Primer2)] == 'GAAGATTGAA':
            MyList.append(line[-25:])
    return MyList

def filterbarcode(barcode): #get rid of the barcode error reads
    out =[]
    for element in barcode:
        if element not in ['CCCCCCCCCCCCCCCCCCCCCCCCC','NNNNNNNNNNNNNNNNNNNNNNNNN','AAAAAAAAAAAAAAAAAAAAAAAAA','TTTTTTTTTTTTTTTTTTTTTTTTT','GGGGGGGGGGGGGGGGGGGGGGGGG']:
            out.append(element)
    return out

from collections import Counter

r1=covert(READ1)
b=covert(READ2)
r2 =seqrevcomp(b)
del b



mergerdseq0 = merge(r1,r2,130,R2ADD) #



del r2
del r1



MyFile=open('sequence-over.txt','w')
for element in mergerdseq0:
     MyFile.write(element)
     MyFile.write('\n')
MyFile.close()



counts = Counter(final25(mergerdseq0))
del mergerdseq0
fivetimesbarcode = [value for value, count in counts.items() if count >2]
#print(output)
print(len(fivetimesbarcode))
del counts
fivetimesbarcode=filterbarcode(fivetimesbarcode)

#creat the barcode file
MyFile=open('barcode-over.txt','w')

MyFile.write('\n'.join(fivetimesbarcode))

MyFile.close()
