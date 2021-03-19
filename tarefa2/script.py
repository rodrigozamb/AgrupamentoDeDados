import math
import random



def main():

    add()



def escrita(arq):

    f = open(arq+".csv", "r")
    f2 = open("dataset.csv", "w")

    i=0
    for line in f:
        if i == 0:
            f2.write(line)
            i=i+1
            continue
        
        s = line.replace("\n","")
        a = s.split(",")

        r1 = random.randint(0,9)
        r2 = random.randint(0,9)
        r3 = random.randint(0,9)

        if(r1 == 0):
            a[2]='?'
        if(r2 == 0):
            a[3]='?'
        if(r1 == 0):
            a[4]='?'
        
        wline = str(a[0])+''.join(","+j for j in a[1::])+'\n'
        f2.write(wline)

        i = i+1


    f.close()
    f2.close()


def add():
    f2 = open("dataset.csv", "a")

    for i in range(0,10000):

        r1 = random.randint(0,9)
        r2 = random.randint(0,9)
        r3 = random.randint(0,9)

        if(r1 == 0):
            a='?'
        else:
            a = random.randint(0,3)
        if(r2 == 0):
            b='?'
        else:
            b = random.randint(0,3)
        if(r1 == 0):
            c='?'
        else:
            c = random.randint(0,3)

        wline = "U"+str(random.randint(1000,1200))+",13"+str(random.randint(1000,6000))+","+str(a)+","+str(b)+","+str(c)+"\n"
        f2.write(wline)

    f2.close()
    print("added 10000 lines to the file")


main()