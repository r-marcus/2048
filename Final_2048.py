
"I hereby certify that this program is solely the result of my own work and is in compliance with the Academic Integrity policy of the course syllabus and the academic integrity policy of the CS department."

import Draw 
import random
import time

SQUARESIZE = 100  #APPROVED CONSTANT
BORDERSIZE = 15   #APPROVED CONSTANT

def background():
    Draw.setCanvasSize(BORDERSIZE * 5 + SQUARESIZE * 4, \
                       BORDERSIZE * 5 + SQUARESIZE*4) 
    
    backcolor = Draw.color(173,161,152) #background color RGB values
    Draw.setBackground(backcolor)  

    
def masterList():
    masterlist = [[0 for col in range(4)] for row in range(4)] #creates a 4x4 2D list full of 0s
    
    rowPick = random.randint(0,3)
    colPick = random.randint(0,3)
    masterlist[rowPick][colPick] = 2 #a 2 is placed in a random location on the board

    return masterlist

def add2(masterList): # a random location in the 2D list is chosen. If that location is not a 0, a different location is chosen
    
    row = random.randint(0, 3) #len(masterList)
    col = random.randint(0, 3) #len(masterList)
    two_four = random.randint(1, 5) #4/5 chance of a 2 being placed in a random location
    
    while masterList[row][col] != 0: 
        row = random.randint(0, 3)
        col = random.randint(0, 3)
        
    if two_four <= 4: masterList[row][col] = 2
    else: masterList[row][col] = 4
    
    return masterList
       
    
def drawBoard(masterList): #For each row and col, it draws a box based on that location's value in the 2D list and the string of that value


    
    color0= Draw.color(184,179,172)
    color2 = Draw.color(238, 228, 218)
    color4 = Draw.color(237, 223, 200)
    color8 = Draw.color(241, 177, 120)
    color16 = Draw.color(245, 149, 99)
    color32 = Draw.color(246, 124, 96)
    color64 = Draw.color(246, 94, 58)
    color128 = Draw.color(237, 207, 114)
    color256 = Draw.color(237, 204, 97)
    color512 = Draw.color(237, 199, 81)
    color1024 = Draw.color(237, 197, 63)
    color2048 = Draw.color(236, 194, 45) #RGB values of 2048 gamepieces
    
    numColor = Draw.color(96, 96, 96) #RGB value of text
    
    for row in range(len(masterList)):
        for col in range(len(masterList[0])): #For each row and col: draw a box with a specific color based on that location's value in the 2D list
            Draw.setColor(eval('color'+str(masterList[row][col]) ) )
            Draw.filledRect((row * (SQUARESIZE+BORDERSIZE) + BORDERSIZE), \
                            (col * (SQUARESIZE+BORDERSIZE) + BORDERSIZE), \
                            SQUARESIZE, SQUARESIZE)  
            Draw.setColor(Draw.WHITE) 
            
         #set different text sizes based on how many digits will fit in the SQUARESIZE x SQUARESIZE box   
            if masterList[row][col] == 2 or masterList[row][col] == 4 or masterList[row][col] == 8: 
                if masterList[row][col] != 8: Draw.setColor(numColor)
                
                Draw.setFontSize(50)
                Draw.string(str(masterList[row][col]), \
                            row * (SQUARESIZE+BORDERSIZE) + BORDERSIZE + 35, \
                            col * (SQUARESIZE+BORDERSIZE) + BORDERSIZE + 25) #arbitrary numbers to center text
                
                
            elif masterList[row][col] == 16 or masterList[row][col] == 32 or \
                 masterList[row][col] == 64:
                Draw.setFontSize(45)
                Draw.string(str(masterList[row][col]), \
                            row * (SQUARESIZE+BORDERSIZE) + BORDERSIZE + 25, \
                            col * (SQUARESIZE+BORDERSIZE) + BORDERSIZE + 27)  #arbitrary numbers to center text     
                
                
            elif masterList[row][col] == 128 or masterList[row][col] == 256 or \
                 masterList[row][col] == 512:
                Draw.setFontSize(40)
                Draw.string(str(masterList[row][col]), \
                            row * (SQUARESIZE+BORDERSIZE) + BORDERSIZE + 16, \
                            col * (SQUARESIZE+BORDERSIZE) + BORDERSIZE + 29)  #arbitrary numbers to center text
            
            
            elif masterList[row][col] == 1024 or masterList[row][col] == 2048:
                Draw.setFontSize(40)
                Draw.string(str(masterList[row][col]), \
                            row * (SQUARESIZE+BORDERSIZE) + BORDERSIZE + 5, \
                            col * (SQUARESIZE+BORDERSIZE) + BORDERSIZE + 29) #arbitrary numbers to center text                 

    return masterList


#MOVEMENT FUNCTIONS
def smushDown(masterList): #Move all non 0 values to the bottom of the 2D list
    for row in range(len(masterList)):
        nextFilled = len(masterList)-1 
        for col in range(len(masterList[0])-1,-1,-1):
            if masterList[row][col] != 0:
                masterList[row][nextFilled] = masterList[row][col]
                if col != len(masterList[0])-1 and col != nextFilled:
                    masterList[row][col] = 0
                nextFilled -= 1
                
    return masterList
                
def smushUp(masterList): #Move all non 0 values to the top of the 2D list
    for row in range(len(masterList)):
        nextFilled = 0
        for col in range(len(masterList[0])):
            if masterList[row][col] != 0:
                masterList[row][nextFilled] = masterList[row][col]
                if col != nextFilled and col != 0:
                    masterList[row][col] = 0
                nextFilled += 1
                
    return masterList

def smushL(masterList): #Move all non 0 values to the left of the 2D list
    for col in range(len(masterList[0])):
        nextFilled = 0
        for row in range(len(masterList)):
            if masterList[row][col] != 0:
                masterList[nextFilled][col] = masterList[row][col]
                if row != nextFilled and row != 0:
                    masterList[row][col] = 0
                nextFilled += 1  
    return masterList
                
def smushR(masterList): #Move all non 0 values to the right of the 2D list
    for col in range(len(masterList[0])):
        nextFilled = len(masterList)-1
        for row in range(len(masterList)-1,-1,-1):
            if masterList[row][col] != 0:
                masterList[nextFilled][col] = masterList[row][col]
                if row != nextFilled and row != len(masterList)-1:
                    masterList[row][col] = 0
                nextFilled -= 1  
    return masterList

            
def combineDown(masterList): 
    #Loop through the list and combine values that are directly above/below each other to be the sum of those values in the lower position, 
    #replace the higher positioned value with a zero
    for row in range(len(masterList)):
        for col in range(len(masterList)-1,-1,-1): 
            if masterList[row][col] == masterList[row][col-1]:
                masterList[row][col] = (masterList[row][col]*2)
                masterList[row][col-1] = 0
    return masterList

def combineUp(masterList): 
    #Loop through the list and combine values that are directly above/below each other to be the sum of those values in the higher position, 
    #replace the lower positioned value with a zero
        for row in range(len(masterList)):
            for col in range(len(masterList)-1):
                if masterList[row][col] == masterList[row][col+1]:
                    masterList[row][col] = (masterList[row][col]*2)
                    masterList[row][col+1] = 0
        return masterList

def combineL(masterList): 
    #Loop through the list and combine values that are directly next to each horizontally to be the sum of those values in the leftmost position, 
    #replace the right positioned value with a zero
    for col in range(len(masterList[0])):
        for row in range(len(masterList)-1):
            if masterList[row][col] == masterList[row+1][col]:
                masterList[row][col] = (masterList[row][col]*2)
                masterList[row+1][col] = 0
    return masterList    

def combineR(masterList):
    #Loop through the list and combine values that are directly next to each horizontally to be the sum of those values in the rightmost position, 
    #replace the left positioned value with a zero
    for col in range(len(masterList[0])):
        for row in range(len(masterList)-1,-1,-1):
            if masterList[row][col] == masterList[row-1][col]:
                masterList[row][col] = (masterList[row][col]*2)
                masterList[row-1][col] = 0
    return masterList     



#THE PARAMETERS FOR THE GAME
def gameOngoing(masterlist): 
    
    #loop through the board and see if there is a 2048- The game has been won
    for row in range(len(masterlist)): 
        for col in range(len(masterlist)):
            if masterlist[row][col] == 2048: return 'win'
            
    #loop through the board and see if the bottommost or rightmost positions have a zero value, 
     #if so, the game can continue
    for row in range(len(masterlist)):
        for col in range(len(masterlist)):
            if row == len(masterlist) - 1 or col == len(masterlist) - 1: 
                if masterlist[row][len(masterlist)-1] == 0: return 'continue'
                elif masterlist[len(masterlist)-1][col] == 0: return 'continue'

                     
    #loop through the board and see if there are any vertical or horizontal pairs, if so, the game can continue
    for row in range(len(masterlist)-1):  
        for col in range(len(masterlist[0])-1):
            if masterlist[row][col] == 0 or \
               masterlist[row][col] == masterlist[row][col+1] or \
               masterlist[row][col] == masterlist[row+1][col]: return 'continue' 
            
    #loop through the bottommost row and see if there are any horizontal pairs
    for col in range(len(masterlist)-1):
        if masterlist[len(masterlist)-1][col] == masterlist[len(masterlist)-1][col + 1]: return 'continue'
    
    #loop through the rightmost row and see if there are any vertical pairs
    for row in range(len(masterlist)-1):
        if masterlist[row][len(masterlist)-1] == masterlist[row  + 1][len(masterlist)-1]: return 'continue'
    
    #if none of the above is true, the game has been lost    
    return False


            
def game():
#GAME SETUP
    
    #initialize a variable that will keep track of if a two/four can be added to the board. 
     #if not but a move is still possible, it will not add any more two/fours until the combination has been made 
     #and the game can continue
    spaceAvail = False
    
    masterlist = masterList()
    add2(masterlist) #add a random second piece to the board
    background()
    status = gameOngoing(masterlist)

#GAME PLAY
    while status == 'continue': #While the game has not been won, and is still able to be played
        
        drawBoard(masterlist)
        
        #AWAITING USER INPUT
        if Draw.hasNextKeyTyped(): 
                newKey = Draw.nextKeyTyped()
                
        #move the entire board in the direction the user prompted
        #make any combinations that can be made in that direction (see individual combine functions)
        #move the board again to accomodate the zeros that the combining caused
        
                if newKey == 'Right': 
                        smushR(masterlist)
                        combineR(masterlist)
                        smushR(masterlist)

                    
                elif newKey == 'Left':
                        smushL(masterlist)
                        combineL(masterlist)
                        smushL(masterlist)

                    
                elif newKey == 'Up':
                        smushUp(masterlist)
                        combineUp(masterlist)
                        smushUp(masterlist)

                    
                elif newKey == 'Down':
                        smushDown(masterlist)
                        combineDown(masterlist)
                        smushDown(masterlist)

                          
                
                Draw.clear()
                drawBoard(masterlist) 
                Draw.show(100)
                #Delay adding a two/four so that the change in board the user prompted is easier to see 
                time.sleep(.1) 
                
                for row in masterlist:
                    if 0 in row: #if a zero can be added, there is availible Space, and add2() can be called
                        spaceAvail = True
                if spaceAvail == True: add2(masterlist)
                spaceAvail = False #make sure spaceAvail is turned back 'off' before the next round
                drawBoard(masterlist)
                
        status = gameOngoing(masterlist) 

        
    
        
    if status == False: #if the game hasn't been won and cannot be continued, 
        #clear the board and display the message
        Draw.clear()
        Draw.setColor(Draw.GRAY)
        Draw.filledRect(BORDERSIZE, BORDERSIZE*2+SQUARESIZE, \
                        BORDERSIZE * 3 + SQUARESIZE * 4, BORDERSIZE * 3 + SQUARESIZE * 2)
        Draw.setFontSize(SQUARESIZE) 
        Draw.setColor(Draw.BLACK)
        Draw.string("You Lost", (SQUARESIZE//2) - BORDERSIZE*2, (SQUARESIZE*2) - BORDERSIZE  )
        Draw.show(100)

        
    elif status == 'win': #if there is a 2048 piece on the board, 
        #clear the board and display the message
        Draw.clear()
        Draw.setFontSize(100)
        WinText = Draw.color(255,240,128) #RGB values
        Draw.setColor(WinText)
        
        Draw.filledRect(BORDERSIZE, BORDERSIZE*2+SQUARESIZE, \
                        BORDERSIZE * 3 + SQUARESIZE * 4, BORDERSIZE * 3 + SQUARESIZE * 2)
        Draw.setColor(Draw.GRAY)
        
        Draw.string("You Won!", (SQUARESIZE//2) - BORDERSIZE*2, (SQUARESIZE*2) - BORDERSIZE )
        Draw.show(SQUARESIZE)

    
def main():
    game()
            
main()

# Thank you to Professor Broder, Judith Wechter, Tova Narrowe, Alexandra Roffe, and Shira Orlian for all their guidance on this project. Advice was all given within the Integrity Policy

# All RGB values were picked using ginifab.com and 2048game.com