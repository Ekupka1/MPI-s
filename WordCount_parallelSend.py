# mpi word count seperates the paragraph in lines then counts the word count then adds to a dictionary where all the line counts gets added to one.
#Ethan Kupka

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

#splits the main str in muiltiple sections and returns newStr
def splitStr(text, size):
    print("text: ", text)
    newStr = []
    partial_len = len(text)//size
    for proc in range(size):
        start = proc*partial_len
        end = start + partial_len
        newStr.append(text[start:end])
    print("split list:",newStr)
    return newStr

#splits the str and counts the accurance of words and returns the count
def count(lines):
    wordCount ={}
    for word in lines:
        words = word.split()
        for word in words:
            if word in wordCount:
                wordCount[word] += 1
            else:
                wordCount[word] = 1
    return wordCount

#combines the word count of the seperated lines and combines them
def combineResult(resultList):
    result = {}
    for dicts in resultList:
        for key in dicts:
            if key in result:
                result[key] += dicts[key]
            else:
                result[key] = dicts[key]
    return result

#writes the word count in output file
def fileWrite(result):
    fileOut = open("output.txt", "w")
    for key in result:
        status = key+' '+str(result[key])+'\n'
        text = fileOut.write(status)
    fileOut.close()

#rank 0 opens file and makes main str
if rank == 0:
    file = open("par.txt", "r")
    text = file.read()
    file.close()
    wordCount = {}
    line = splitStr(text.split('\n'), size) #calling split-makes new lines
else:
    line = []

#Process other than 0 send wordCount dictionary to proc 0
if not rank==0:
	comm.send(wordCount,dest=0)

if rank == 0:
    for line in range(1,size):
        line = comm.recv(source = line)
        result = count(line) #calls count-counts new lines
        print("rank: ",rank," - ",result)
        result = comm.recv(source = result)

if rank == 0:
    result = combineResult(result) #calling combineResult-combines the count results of each
    print(fileWrite(result)) #put write after count

#loop is need for send and recv
