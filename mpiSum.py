# mpi finds the sum of a list

from mpi4py import MPI
import random

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

def createList(size):
	numList=[]
	for element in (range(size)):
    	numList.append(random.randint(0, size))
	print(numList)
	return numList

def sumOfList(size):
	result = 0
	numList = createList(size)
	for value in numList:
    	result+=value
	return result

    #below sets partial list to proc
 if rank==0:
 	numList=createList(1000)
    listSize = 1000
 	partial_list = int(result/size)  #result/proc = partial
 	print(partial_list)
 else:
 	message = comm.recv(source = 0) #

#below sends the partial list to the proc
 	for proc in (1,size):
     	start= proc * partialLen #splicing the list
     	end = start+partialLen
     	partial_list = numList[start:end]
     	comm.send(partial_list, dest=proc)
     	print(partial_list)

    else:
        partial_list = comm.recv(source = 0)
        sum_x=sumOfList()


#after (file.read) reading a file the file will be a string
