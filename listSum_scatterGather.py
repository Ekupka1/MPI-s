# Assignment 3 - First Scatter and gather

from mpi4py import MPI
import random
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

#creates main list
def createList(length):
    numList=[]
    random.seed(time.time())
    for element in range(length):
        numList.append(random.randint(0, length))
    return numList

#divides main list in sections
def divideList(newList, part):
    numlist = []
    partial_len = len(newList)//part
    for proc in range(part):
        start = proc*partial_len
        end = start + partial_len
        numlist.append(newList[start:end])
    print("split list:",numlist)
    return numlist

#finds the sum
def sumOfList(lst):
    result = 0
    for value in lst:
        result+=value
    return result

#rank 0 gets main list and inital section
if rank == 0:
    amount = 5
    newlist = createList(amount)
    print("main list:", newlist)
    lists = divideList(newlist, size)
else:
    lists = []

#gather and scatter of the list gets sum
lists = comm.scatter(lists, root = 0)
result = sumOfList(lists)
result = comm.gather(result, root = 0)

#rank 0 sums up all the list to one
if rank == 0:
    result= sumOfList(result)
    print(result)
