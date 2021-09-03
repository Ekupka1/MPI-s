# mpi making a random list spliting that list then finding the sum of each of the split list

from mpi4py import MPI
import random
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

def createList(size):
    numList=[]
    random.seed(time.time())
    for element in range(size):
        numList.append(random.randint(0, size))
    print(numList)
    return numList

def sumOfList(size):
    result = 0
    numList = createList(size)
    for value in numList:
        result+=value
    return result
#print(sumOfList(10))

#below sets partial list to proc
if rank==0:
    result = 10
    totsum = 0
    numList=createList(result)
    partiallen = int(result/size)  #result/proc = partial
    print(partiallen)
 #below sends the partial list to the proc
    for proc in (1,size):
        start= proc * partiallen #splicing the list
        end = start+partiallen
        partial_list = numList[start:end]
        print(partial_list)
        comm.send(partial_list, dest=proc)

    result = sumOfList(partiallen, dest = proc)

    for i in range(0, partiallen):
        totsum+=numList[i]

    for proc in range(1, size):
        partialsum += comm.recv(soucre = proc)
        #result += partialsum
    print(partialsum)
else:
    partiallen = comm.recv(source = 0)
    sumLst = sumOfList(partiallen)
    comm.send(sumLst, dest = 0)

#after (file.read) reading a file the file will be a string
