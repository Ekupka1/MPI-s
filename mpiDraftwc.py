#makes a mpi -- draft of WordCount_parallel.py
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

#opens file and makes it str
#file = open("par.txt", "r")
#text = file.read()
#file.close()

#original str
#print("(" + text + ")" + '\n')"

#counts the word occurance of each word
#wordCount = {}

#splits the str and counts the accurance of words and writes it in file
def count(lst):
    #lst2 = lst.split(" ")
    wordCount = {} #{}it is a unhashable list- do I have to add all the list to the main dictionary at the end then run it through count
    for word in lst:
        if word in wordCount:
            wordCount[word] += 1
        else:
            wordCount[word] = 1
    return wordCount

#opens out-file
fileWrite = open("output.txt", "w")

#writes wordCount in out-file
def writeOut(wordCount):
    for word in wordCount:
        string = "'" + word + "' -" + str(wordCount[word]) + '\n'
        fileWrite.write(string)
        print(word, wordCount[word])
    fileWrite.close()

#splits the main str
def splitStr(text, size):
    choppedStr = []
    partial_len = len(text)//size
    for proc in range(size):
        start = proc*partial_len
        end = start + partial_len
        choppedStr.append(text[start:end])
        print("split str:", choppedStr)
    return choppedStr

if rank == 0:
    #opens file and makes it str
    file = open("par.txt", "r")
    text = file.read()
    st2 = text.split(" ")
    #print(text)
    #print("(" + text + ")" + '\n')"
    #wordCount = {}
    newStr = splitStr(st2, size)
    countStr = count(newStr)
    writeFile = writeOut(countStr)

print(wordCount)

file.close()


newS = count(text)
print(writeOut(newS))
