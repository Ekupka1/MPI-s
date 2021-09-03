# Basic fisrt mpi word count

from mpi4py import MPI
lst = "alice bob alice"

lst2 = lst.split(" ")
lst2 = []
wc = {}

for word in lst2:
	if word in wc:
		wc[word]+=1
	else:
		wc[word]=1
	return wc
print(wc)
