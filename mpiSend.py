#mpi first basic send

from mpi4py import MPI
import os

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# print(os.getpid())

message = " "

if rank==0:
    message+=str(os.getpid())
    comm.send(message, dest = 1)
    print("Pid of the other process B:", message)
else:
    message = comm.recv(source = 0)

#size = comm.Get_size()
