



import statistics
import re
import multiprocessing
from multiprocessing import Queue
from multiprocessing import Process, managers
import time
##### Need input

name = 'seq7'
Primer1= 25
Primer2= 0
ORDER= 142
Seqinput= 'GTTATGTAGAGTGTTAACGTTATGTAGAGTGTTAGCGTTATGTAGAGTGTTTACGTTATGTAGAGTGTTTTCGTTATGTAGAGTGTTATCGTTATGTAGAGTGTT'
Processors=60



######
filename = name+'.txt'
print(filename)

def replace_c(input_string):
    modified_string = input_string.replace('C', '[CT]')
    return modified_string

MUTseq = replace_c(Seqinput)

Primer1EXTEND=Primer1-25
Primer2EXTEND=Primer2-0

FullLENGTH= ORDER+25 #default: 142 designed sequences with priming site and 25N barcode


def adjustseq(seqlist):
    out=[]
    for i in range(len(seqlist[1])):
        temp=[]
        for line in seqlist:
            if len (line) == FullLENGTH:
                temp.append(line[i])

        most=statistics.mode(temp)
        if temp.count(most) > 0.8*len(temp):
            most = most
        else:
            most = 'N'

        out.append(most)
    seq = "".join(out)
    return seq

def finalseq(dubplicate,original,seq_dict,q):
    out=[]
    for line in dubplicate:
        filter_object = [original[i] for i in seq_dict[line]]
        if len(filter_object) !=0:
            out.append(adjustseq(filter_object))
    q.put(out)

'''
if __name__=="__main__":
    pool =Pool()
    result = pool.map(finalseq,barcode,seq)
    pool.close()
    pool.join()

    print(result)





'''
if __name__=="__main__":
    t1 = time.time()

    my_file = open("barcode-over.txt", "r")
    content = my_file.read()
    testbarcode = content.split("\n")
    my_file.close()

    barcode = testbarcode

    my_file = open("sequence-over.txt", "r")
    content = my_file.read()
    seq = content.split("\n")

    my_file.close()

    seq_dict = dict()
    for i, line in enumerate(seq):
        if line[-25:] in seq_dict:
            seq_dict[line[-25:]].append(i)
        else:
            seq_dict[line[-25:]] = [i]


    t2=time.time()

    q= Queue()


    processes=[]
    processnumber=Processors

    seperation=int(len(barcode)/processnumber)
    fivecode=[barcode[i:i+seperation] for i in range(0,len(barcode),seperation)]
    for element in fivecode:
        process=Process(target= finalseq,args=(element,seq,seq_dict,q))
        process.start()
        processes.append(process)


    final=[]

    for process in processes:
        obj = q.get()
        #print(obj)
        final=final+obj
        print ("finsh")

    for process in processes:
        process.join()

    #print(final)
    #print(len(final))
    print("took",time.time()-t1)


    def motifnoly(seq):
        out = []
        for line in seq:
            out.append(line[18+Primer2:123+Primer2])
        return out


    motifs = motifnoly(final)
    refmoti = MUTseq

    def correctseq(seq, refmoti):
        out = []
        for line in seq:
            if re.findall(refmoti, line) != []:
                out.append(line)
        return out


    correct = correctseq(motifs, refmoti)
    print(len(correct))
    right = Seqinput


    def alignment(seq, ref):
        out = []
        Mut = []
        for line in seq:
            temp = 0
            for i in range(len(ref)):
                if line[i] == ref[i]:
                    temp = temp + 0
                else:
                    temp = temp + 1
                    #print(line[i])
                    #print(i)
                    Mut.append(line[i])
            out.append(temp)
        #print(Mut)
        #print(len(Mut))
        return out


    #alig = alignment(correct, right)


    def counterror(seq):
        score = 0
        for element in seq:
            if element != 0:
                score = score + 1
                #print(element)
        return score

    #print(counterror(alig))


    #def counterrorbiger1(seq):
        score = 0
        for element in seq:
            if element > 1:
                score = score + 1
                #print(element)
        return score

    #print(counterrorbiger1(alig))

    alig = alignment(correct, right)
    #print(alig)

    def counterror(seq):
        score = 0
        for element in seq:
            if element != 0:
                score = score + 1
                # print(element)
        return score


    print(counterror(alig))


    def counterrorbiger1(seq):
        score = 0
        for element in seq:
            if element > 1:
                score = score + 1
                # print(element)
        return score


    print(counterrorbiger1(alig))


    def creatdot(seq, ref):
        out = []
        for line in seq:
            temp = []
            n = 0
            for i in range(35):
                if line[i * 3:i * 3 + 3] == ref[i * 3:i * 3 + 3]:
                    temp.append(".")
                else:
                    temp.append("T")
                    n = n + 1
            tempjoin = "".join(temp)
            if n > 0:
                out.append(tempjoin)
        return out


    def onlymut(seq):
        out = []
        for line in seq:
            if line != '.....':
                out.append(line)
        return out


    allmut = creatdot(correct, right)
    print(onlymut(allmut))
    print(len(onlymut(allmut)))

    MyFile = open(filename, 'w')



    for element in onlymut(allmut):
        MyFile.write(element)
        MyFile.write('\n')
    MyFile.close()
'''
    allmut = creatdot(correct, right)
    print(onlymut(allmut))
    len(onlymut(allmut))


    MyFile = open('CTC-5min.txt', 'w')

    for element in onlymut(allmut):
        MyFile.write(element)
        MyFile.write('\n')
    MyFile.close()
'''