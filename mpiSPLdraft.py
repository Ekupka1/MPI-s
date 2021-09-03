#!/usr/bin/env python
# coding: utf-8

# In[14]:


from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()


import random
import time
def createList (listSize):
    numList = []
    random.seed(time.time())
    for i in range(listSize):
        numList.append(random.randint(0,listSize))

    return numList

def sumOfList (listA):
    currentSum = 0
    for i in listA:
        currentSum += i
    return currentSum

if rank == 0:
    listSize=13
    totalSum=0
    numList = createList(listSize)
    print(numList)
    partialLen = int(listSize/size)
    for process in range (1, size):
        start = partialLen*(process)
        print(partialLen)
        if process != size-1:
        	partialList = numList[start : start+partialLen]
        else:
        	partialList = numList[start :]
        print(partialList)
        comm.send(partialList, process, tag=0)
    for i in range(0, partialLen):
    	totalSum+=numList[i]

    print(totalSum)
    for process in range (1, size):
        totalSum+=comm.recv(source=process)
    print(totalSum)

else:
    recvdList = comm.recv(source=0)
    listSum = sumOfList(recvdList)
    comm.send(listSum, 0, tag=0)



# In[ ]:
