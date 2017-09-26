import random
from array import *
#############################################
# Generator for a wordsearch. This generates a 20 by 20 wordsearch
# You put the file inside the folder with the python code. The
# file must be called "wordSearch.txt". Create a wordSearch.txt file to place
# your word search.
#
# Michael Larios and Grayson Taylor
#
#############################################
wordlist= [ ] #array holding our solution
wordsearch= [ [ '+' for i in range(20) ] for j in range(20) ] #array holding our wordsearch
wordbank = [ ]  #Holds the words we are looking for
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'
		, 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
print(alphabet)
##
# This method prints everything in our solution list
##
def print_everything():
    for i in range(20):
        for j in range (20):
            print(solution[i][j])
            print( j + (20 *i))


##
# This method reads in our list of possible words
# This method also puts in the words into our wordbank
##

def readFile(file):
    f = open(file, 'r')
    counter = -1
    j=-1
    
    for line in f:
        tempLine=line.strip()
        index=len(wordlist)
        wordlist.insert(index,tempLine)

##
#This sets up our wordsearch
##
def createWordsearch():
    wordsearch= [ [ '+' for i in range(20) ] for j in range(20) ] #array holding our wordsearch
    return wordsearch

##
#
# This picks out the words from our list
# This makes sure no words are duplicated
#
##
def createWordbank():
    tempWordbank=[]
    i = 0
    wordcheck=0
    while i < 15:
        wordcheck = 0
        index= random.randrange(0, len(wordlist))
        word=wordlist[index]
        for x in tempWordbank:    #This makes sure we don't choose the same words twice
            if word == x:
                wordcheck = 1
        if wordcheck == 0:        
            tempWordbank.insert(i,word)
            i = i + 1
        
    return tempWordbank
  
   

##
# This writes our wordsearch into our wordSearch.txt
##
def writeWordsearch(wordbank):
    f= open('wordSearch.txt', 'w')
    for i in range(0, len(wordsearch)):
        for j in range(0, len(wordsearch)):
            f.write(wordsearch[i][j])
            f.write("  ")
        f.write("\n")
    f.write("----------------------------------------------------------------")
    f.write("\n")
    for i in range(0,len(wordbank)):
        f.write(wordbank[i])
        f.write("\n")




##
#
# This checks each direction to see if the word can be palced, 
# Once the word if found to work, it updates our array holding our word search 
#
##
def checkDir(x, y, direc, word):
    if direc == 0:                   #This checks right
        if ( ( y + len(word) - 1) < len(wordsearch[0]) ):
            for i in range(0, len(word)):        
                if not( word[i] == wordsearch[x][y+i] or '+' == wordsearch[x][y+i] ): #Checks each letter to make sure it matches
                           return False
            placeWord(x,y,direc,word)
            return True
    elif direc ==1:             #This checks diagonal down right
        if ( (y + len(word) - 1) < len(wordsearch[0]) ) and (  (x + len(word) -1) < len(wordsearch)):
             for i in range(0, len(word)):
                if not( word[i] == wordsearch[x+i][y+i] or '+' == wordsearch[x+i][y+i] ):
                           return False
             placeWord( x, y, direc, word)
             return True
    elif direc ==2:            #This checks down  
        if ( (x + len(word) - 1) < len(wordsearch[0]) ):
             for i in range(0, len(word)):
                if not( word[i] == wordsearch[x+i][y] or '+' == wordsearch[x+i][y]):
                    return False
             placeWord( x, y, direc, word)
             return True      
    elif direc ==3:             #This checks down left diagonal
        if ( (y - len(word) + 1) >= 0 ) and (  (x + len(word) -1) < len(wordsearch)):
             for i in range(0, len(word)):
                if not( word[i] == wordsearch[x+i][y-i] or '+' == wordsearch[x+i][y-i]):
                    return False
             placeWord( x, y, direc, word)
             return True
    elif direc ==4:             #This checks left
        if ( (y - len(word) + 1) >= 0 ) :
             for i in range(0, len(word)):
                if not( word[i] == wordsearch[x][y-i] or '+' == wordsearch[x][y-i]):
                    return False
             placeWord( x, y, direc, word)
             return True    
    elif direc ==5:             #This checks left up diagonal
        if ( (y - len(word) + 1) >= 0 ) and (  (x - len(word) +1) >= 0 ):
             for i in range(0, len(word)):
                if not( word[i] == wordsearch[x-i][y-i] or '+' == wordsearch[x-i][y-i]):
                        return False
             placeWord( x, y, direc, word)
             return True    
    elif direc ==6:             #This checks up 
        if ( (x - len(word) + 1) >= 0 ) :
             for i in range(0, len(word)):
                if not( word[i] == wordsearch[x-i][y] or '+' == wordsearch[x-i][y] ):
                           return False
             placeWord( x, y, direc, word)
             return True    
    elif direc ==7:             #This checks up right diagonal
        if ( (y + len(word) - 1) < len(wordsearch[0]) ) and (  (x - len(word) +1) >= 0):
             for i in range(0, len(word)):
                if not( word[i] == wordsearch[x-i][y+i] or '+' == wordsearch[x-i][y+i]):
                           return False
             placeWord( x, y, direc, word)
             return True    
    return False

#This checks to palce our word
def checkWord(word):
    x= random.randrange(0, len(wordsearch))
    y= random.randrange(0, len(wordsearch))
    iDir= random.randrange(0, 8)
    for k in range(0,8):
        if iDir > 7:
            iDir=iDir-7
        if(checkDir(x,y,iDir,word)):
            return True
        iDir=iDir+1

    return False


##
#
#This method places our word
##
def placeWord(xCo, yCo, direc, word):
    if direc ==0:                        #This places word right
        for i in range(0, len(word) ):
            wordsearch[xCo][yCo+i]=word[i]
        return True
    elif direc ==1:                       #This places diagonal right down 
        for i in range(0, len(word)):
            wordsearch[xCo+i][yCo+i]=word[i]
        return True
    elif direc ==2:                       # This places down
        for i in range(0, len(word)):
            wordsearch[xCo+i][yCo]=word[i]
        return
    elif direc ==3:                       #This palces down left diagonal
        for i in range(0, len(word) ):
            wordsearch[xCo+i][yCo-i]=word[i]
        return True
    elif direc ==4:                       #This places direction to the left
        for i in range(0, len(word) ):
            wordsearch[xCo][yCo-i]=word[i]
        return True
    elif direc ==5:                       #This places up left diagonal
        for i in range(0, len(word) ):
            wordsearch[xCo-i][yCo-i]=word[i]
        return True
    elif direc ==6:                       #This places left
        for i in range(0, len(word) ):
            wordsearch[xCo-i][yCo]=word[i]
        return True
    elif direc ==7:                       #This places up left diagonal
        for i in range(0, len(word) ):
            wordsearch[xCo-i][yCo+i]=word[i]
        return True
    return False


##
# This is our main method that controls everything
# This is the one method we call in our file. 
##
def main():
    global wordsearch
    global alphabet
    wordsearch = [ [ '+' for i in range(20) ] for j in range(20) ]
    readFile('wordList.txt') #reads in our wordsearch
    wordbank=[]
    wordbank = createWordbank()
    tempBool=False
    for x in wordbank:
        while tempBool==False:
            tempBool=checkWord(x)

        tempBool=False


    for i in range(0,len(wordsearch)):
        for j in range(0,len(wordsearch)):
            if wordsearch[i][j] == '+':
                yoda=random.randrange(0,len(alphabet))
                wordsearch[i][j]=alphabet[yoda]
    writeWordsearch(wordbank)
        
def printing():
    for i in range(0, len(wordsearch)):
        print(i)

#Calls main
main()
