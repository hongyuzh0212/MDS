import re
import pandas as pd
'''
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

def rev(seq):
    #Returns the reverse of seq
    return seq[::-1]

def revcomp(seq):
    #Returns the reverse complement of seq
    rv = rev(seq)
    rvcp = compseq(rv)
    return rvcp

def covert (Read):
    outseq=[]
    infile1 = open(Read)
    for line in infile1:
        out = line.replace("\n", "")
        out = out.replace("\r", "")
        outseq.append(out)
    infile1.close()
    return outseq

def seqrevcomp (seq):
    out=[]
    for i in range(len(seq)):
        if i%4 == 0 or i%4==2:
            out.append(seq[i])
        elif i%4 == 1:
            temp = revcomp(seq[i])
            out.append(temp)
        else:
            temp = rev(seq[i])
            out.append(temp)
    return out

def merge(read1,read2,r1headkeep,r2tailkeep):
    out=[]
    for i in range(len(read1)):
        if i%4 == 0 or i%4==2:
            temp = "".join([read1[i],read2[i]])
            out.append(temp)
        else:
            temp= "".join([read1[i][0:r1headkeep],read2[i][-r2tailkeep:]])
            out.append(temp)
    return out

def onlyseq(seq):
    out=[]
    for i in range(len(seq)):
        if i%4==1:
            out.append(seq[i])

    return out

def final25(seq):
    MyList=[]
    for line in seq:
        MyList.append(line[-25:])
    return MyList

from collections import Counter

import statistics
def adjustseq(seqlist):
    out=[]
    for i in range(len(seqlist[1])):
        temp=[]
        for line in seqlist:
            if len (line) == 228:
                temp.append(line[i])
        most=statistics.mode(temp)
        out.append(most)
    seq = "".join(out)
    return seq


def finalseq(dubplicate,original):
    out=[]
    for line in dubplicate:
        temp=[]
        for seq in original:
            if re.search(line,seq):
                temp.append(seq)
        out.append(adjustseq(temp))
    return out


def counterror(seq):
    score =0
    for element in seq:
        if element != 0:
            score = score +1
    return score

def filterbarcode(barcode):
    out =[]
    for element in barcode:
        if element not in ['CCCCCCCCCCCCCCCCCCCCCCCCC','NNNNNNNNNNNNNNNNNNNNNNNNN','AAAAAAAAAAAAAAAAAAAAAAAAA','TTTTTTTTTTTTTTTTTTTTTTTTT','GGGGGGGGGGGGGGGGGGGGGGGGG']:
            out.append(element)
    return out


r1=covert('AAC-2min_S195_L001_R1_001.fastq')
b=covert('AAC-2min_S195_L001_R2_001.fastq')
r2 =seqrevcomp(b)

mergerdseq0 = merge(r1,r2,120,104)
seqonly0=onlyseq(mergerdseq0)
barcode0=final25(seqonly0)

mergerdseq4 = merge(r1,r2,140,88)
seqonly4=onlyseq(mergerdseq4)
barcode4=final25(seqonly4)


if barcode0 ==  barcode4:
    print ('same barcode')

counts = Counter(barcode0)
fivetimesbarcode = [value for value, count in counts.items() if count >2]
#print(output)
print(len(fivetimesbarcode))
fivetimesbarcode=filterbarcode(fivetimesbarcode)
print(len(fivetimesbarcode))


MyFile=open('barcode.txt','w')

for element in fivetimesbarcode:
     MyFile.write(element)
     MyFile.write('\n')
MyFile.close()






MyFile=open('AAC.txt','w')
for element in seqonly0:
     MyFile.write(element)
     MyFile.write('\n')
MyFile.close()

'''

list_ = open("seq7.txt").read().split()
#print(list_)
out=[0]*5


#5+5+5+5+5+5 motif combination
for line in list_:
    if line[5] == 'T':
        out[0]=out[0]+1
    if line [11] == 'T':
        out[1]=out[1]+1
    if line [17] == 'T':
        out[2]=out[2]+1
    if line [23] == 'T':
        out[3]=out[3]+1
    if line [29] == 'T':
        out[4]=out[4]+1

'''
#5+3+7+7+3+5 motif combination
for line in list_:
    if line[5] == 'T':
        out[0]=out[0]+1
    if line [9] == 'T':
        out[1]=out[1]+1
    if line [17] == 'T':
        out[2]=out[2]+1
    if line [25] == 'T':
        out[3]=out[3]+1
    if line [29] == 'T':
        out[4]=out[4]+1

'''
print(out)
sum = 0
for element in out:
    sum = sum + element

percentage= []
for element in out:
    percentage.append(element/sum*100)
print(percentage)

position = list(range(1,6))
print(position)

import matplotlib.pyplot as plt
plt.plot(position,percentage)
plt.xlabel('position')
plt.ylabel('percentage')
plt.show()
'''
out3=[]
out4=[]
out5or_more=[]
n=[0,0,0,0,0]
for line in list_:
    a= line.count('T')
    if a == 2:
        out2.append(line)
        n[1]=n[1]+1
    elif a== 3:
        out3.append(line)
        n[2] = n[2] + 1
    elif a ==4:
        out4.append(line)
        n[3] = n[3] + 1
    else:
        out5or_more.append(line)
        n[4] = n[4] + 1
'''
#print(out2)
#print(out3)
#print(out4)
#print(out5or_more)
#print(n)
'''

gap='*******************************************************************************************************'

outfile = []
outfile.append(out2)
outfile.append(gap)
outfile.append(out3)
outfile.append(gap)
outfile.append(out4)
outfile.append(gap)
outfile.append(out5or_more)
outfile.append(gap)
outfile.append(n)
print(outfile)

MyFile = open('AAC mutation.txt', 'w')

for element in out2:
    MyFile.write(element)
    MyFile.write('\n')

MyFile.write(gap)
MyFile.write('\n')



for element in out3:
    MyFile.write(element)
    MyFile.write('\n')

MyFile.write(gap)
MyFile.write('\n')


for element in out4:
    MyFile.write(element)
    MyFile.write('\n')

MyFile.write(gap)
MyFile.write('\n')

for element in out5or_more:
    MyFile.write(element)
    MyFile.write('\n')

MyFile.write(gap)


for element in n:
    MyFile.write(str(element))
    MyFile.write('\n')

MyFile.close()

'''

