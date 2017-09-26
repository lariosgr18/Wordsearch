import random
from array import *
#############################################
# Solver for a wordsearch. This solves a 20 by 20 wordsearch
# You put the file inside the folder with the python code. The
# fle must be called "wordSearch.txt". Create a solution.txt file to place
# your solution.
#
#
# Michael Larios 
#
#############################################
solution= [ [ '+' for i in range(20) ] for j in range(20) ]   #array holding our solution
wordsearch= [ [ '+' for i in range(20) ] for j in range(20) ] #array holding our wordsearch
wordbank = [ '+' for i in range (15)]  #Holds the words we are looking for

##
# This method prints everything in our solution list
##
def print_everything():
    for i in range(20):
        for j in range (20):
            print(solution[i][j])
            print( j + (20 *i))


##
# This method reads in our word search and places it in our list
# This method also puts in the words into our wordbank
##

def readFile(file):
    f = open(file, 'r')
    counter = -1
    j=-1
    for line in f:
        counter= counter +1
        j=-1
        if counter < 20:
            for x in line:
                if x and (not x.isspace()):
                    j=j+1
                    
                    wordsearch[counter][j]= x
        if (counter > 21) and (counter < 37):  ##This makes sure we only get the words
            i=counter-22
            tempWord=line.strip()

            wordbank[i]=tempWord


##
# This writes our solution into our soultion.txt
##
def writeSolution():
    f= open('solution.txt', 'w')
    for i in range(0, len(solution)):
        for j in range(0, len(solution)):
            f.write(solution[i][j])
            f.write("  ")
        f.write("\n")
    f.write("--------------------------------------------------------------------")
    f.write("\n")
    for i in range(0,len(wordbank)):
        f.write(wordbank[i])
        f.write("\n")




##
#
# This checks each direction to see if the word has been found.
# Once the word if found to match, it updates our array holding our solution
#
##
def checkDir(x, y, direc, word):
    if direc == 0:                   #This checks right
        if ( ( y + len(word) - 1) < len(wordsearch[0]) ):
            for i in range(0, len(word)):        
                if not( word[i] == wordsearch[x][y+i] ): #Checks each letter to make sure it matches
                           return False
            print(word)
            placeWord(x,y,direc,word)
            return True
    elif direc ==1:             #This checks diagonal down right
        if ( (y + len(word) - 1) < len(wordsearch[0]) ) and (  (x + len(word) -1) < len(wordsearch)):
             for i in range(0, len(word)):
                if not( word[i] == wordsearch[x+i][y+i] ):
                           return False
             print(word)
             placeWord( x, y, direc, word)
             return True
    elif direc ==2:            #This checks down  
        if ( (x + len(word) - 1) < len(wordsearch[0]) ):
             for i in range(0, len(word)):
                if not( word[i] == wordsearch[x+i][y] ):
                    return False
             print(word)
             placeWord( x, y, direc, word)
             return True      
    elif direc ==3:             #This checks down left diagonal
        if ( (y - len(word) + 1) >= 0 ) and (  (x + len(word) -1) < len(wordsearch)):
             for i in range(0, len(word)):
                if not( word[i] == wordsearch[x+i][y-i] ):
                    return False
             print(word)
             placeWord( x, y, direc, word)
             return True
    elif direc ==4:             #This checks left
        if ( (y - len(word) + 1) >= 0 ) :
             for i in range(0, len(word)):
                if not( word[i] == wordsearch[x][y-i] ):
                    return False
             print(word)
             placeWord( x, y, direc, word)
             return True    
    elif direc ==5:             #This checks left up diagonal
        if ( (y - len(word) + 1) >= 0 ) and (  (x - len(word) +1) >= 0 ):
             for i in range(0, len(word)):
                if not( word[i] == wordsearch[x-i][y-i] ):
                        return False
             print(word)
             placeWord( x, y, direc, word)
             return True    
    elif direc ==6:             #This checks up 
        if ( (x - len(word) + 1) >= 0 ) :
             for i in range(0, len(word)):
                if not( word[i] == wordsearch[x-i][y] ):
                           return False
             print(word)
             placeWord( x, y, direc, word)
             return True    
    elif direc ==7:             #This checks up right diagonal
        if ( (y + len(word) - 1) < len(wordsearch[0]) ) and (  (x - len(word) +1) >= 0):
             for i in range(0, len(word)):
                if not( word[i] == wordsearch[x-i][y+i] ):
                           return False
             print(word)
             placeWord( x, y, direc, word)
             return True    
    return False

def findWord(word):
    cFirst = word[0]
    for i in range(0, len(wordsearch) ):
        for j in range(0, len(wordsearch[0]) ):
            if cFirst == wordsearch[i][j]:
                for k in range(0,8):
                    if(checkDir(i,j,k,word)):
                        return

##
#
#This method
##
def placeWord(xCo, yCo, direc, word):
    print(word)
    print(direc)
    if direc ==0:                        #This places word right
        for i in range(0, len(word) ):
            solution[xCo][yCo+i]=word[i]
        return True
    elif direc ==1:                       #This places diagonal right down 
        for i in range(0, len(word)):
            solution[xCo+i][yCo+i]=word[i]
        return True
    elif direc ==2:                       # This places down
        for i in range(0, len(word)):
            solution[xCo+i][yCo]=word[i]
        return
    elif direc ==3:                       #This palces down left diagonal
        for i in range(0, len(word) ):
            solution[xCo+i][yCo-i]=word[i]
        return True
    elif direc ==4:                       #This places direction to the left
        for i in range(0, len(word) ):
            solution[xCo][yCo-i]=word[i]
        return True
    elif direc ==5:                       #This places up left diagonal
        for i in range(0, len(word) ):
            solution[xCo-i][yCo-i]=word[i]
        return True
    elif direc ==6:                       #This places left
        for i in range(0, len(word) ):
            solution[xCo-i][yCo]=word[i]
        return True
    elif direc ==7:                       #This places up left diagonal
        for i in range(0, len(word) ):
            solution[xCo-i][yCo+i]=word[i]
        return True
    return False


##
# This is our main method that controls everything
# This is the one method we call in our file. 
##
def main():
    readFile('wordSearch.txt') #reads in our wordsearch
    for x in wordbank:      #This loops through our wordbank to find the words 
        findWord(x)      
    writeSolution()
def printing():
    for i in range(0, len(wordsearch)):
        print(i)

#Calls main
main()
