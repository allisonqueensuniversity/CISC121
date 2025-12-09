import tkinter #The UI library I am using
import turtle #How the sorting is displayed
import time #Used to "wait" (I use this to make the binary search visible for enough time to see it)

#Checks if the string can be turned into an integer
def isInteger(integer):
    try:
        int(integer)
        return True #If it is an integer
    except ValueError:
        return False #If it is not

#Checks if the string can be turned into an integer above (by default including) an integer
def isIntegerAbove(inputInteger,minimum,inclusive=True):
    if not isInteger(inputInteger):
        return False #If it is not an integer
    if int(inputInteger)>minimum or (int(inputInteger)==minimum and inclusive):
        return True #If it is an integer above the minimum (or at the minimum if inclusive)
    return False #If it is an integer below the minimum (or at the minimum if not inclusive)

#Checks if the string can be turned into an integer below (by default including) an integer
def isIntegerBelow(inputInteger,maximum,inclusive=True):
    if not isInteger(inputInteger):
        return False #If it is not an integer
    if int(inputInteger)<maximum or (int(inputInteger)==maximum and inclusive):
        return True #If it is an integer below the maximum (or at the maximum if inclusive)
    return False #If it is an integer above the maximum (or at the maximum if not inclusive)
    
#Checks if the string can be turned into an integer between/within (by default witin) 2 integers
def isIntegerBetween(inputInteger,minimum,maximum,inclusive=True):
    if isIntegerAbove(inputInteger,minimum,inclusive) and isIntegerBelow(inputInteger,maximum,inclusive):
        return True #If it is an integer between/within the maximum and minimum
    return False #If it is not
    
#The binary search algorithm I used (here for reference)
def binarySearch(arr,target,low,high):
    if low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        if arr[mid]<target:
            return binarySearch(arr,target,mid+1,high)
        return binarySearch(arr,target,low,mid-1)
    return -1

#Checks if a list is sorted
def isSorted(list):
    previous=None #The first entry does not have a previous number
    for current in list:
        if previous!=None and current<previous: #If the previous entry is more than the current
            return False #The list is unsorted
        previous=current #The previous is set to current for the next entry
    return True #The list is sorted

#Code for the UI starts here
#The following code sets up the UI window
appUI=tkinter.Tk()
appUI.title("Binary Search App")
entriesToSort=0
maxRows=10 #The maximum number of rows (used to make the UI show itself horizontally right rather than just vertically down)
numberOfRows=2 #The number of rows, this is mostly just used to put the buttons in the right place
rowManager=[] #This holds the entries for the UI
listToSearch=[] #This is the final list of integers that it will sort

enterPressed=False #Checks whether the enter button is pressed
#Defines what the enter button does when it is pressed
def enterPress(): #This is the thing that makes the enter button work
    global enterPressed
    enterPressed=True

#This makes the fields that take the inputs
class tkinterInput():
    def __init__(self,rowInput,columnInput,name): #Initializer
        self.rowInput=rowInput
        self.columnInput=columnInput
        self.name=name

        self.inputName=tkinter.Label(appUI,text=name)
        self.inputName.grid(row=rowInput,column=columnInput)
        self.inputField=tkinter.Entry(appUI)
        self.inputField.grid(row=rowInput,column=columnInput+1)
    
    def getValue(self): #Gets the value within the field
        return self.inputField.get()
    
    def close(self): #Closes the field
        self.inputName.destroy()
        self.inputField.destroy()
        #MAKE SURE TO CLEAR IT FROM THE LIST AFTER

toSortAsk=tkinterInput(0,0,"Number of entries to sort:") #To take the # of entries to sort

#The following code defines error messages
error=tkinter.Label(appUI,text="",fg="white",bg="red",font=("Arial",14)) #Defines the error box's appearance
def showError(message): #The function that shows the error box
    error.lift()
    error.config(text=message)
    error.place(relx=0.5,rely=0.5,anchor="center")  #Centers the warning
    appUI.after(1500,error.place_forget) #Removes the error after 1.5 seconds

#The following sets up the enter and stop buttons
enterButton=tkinter.Button(appUI,text="Enter",fg="white",width=25,command=enterPress,bg="green")
enterButton.grid(row=numberOfRows+1)
stopButton=tkinter.Button(appUI,text="Stop",fg="white",width=25,command=appUI.destroy,bg="red")
stopButton.grid(row=numberOfRows+1,column=2)

#First UI loop for the number of entries
while True:
    appUI.update()
    if enterPressed: #If the green enter button is pressed
        if isIntegerBetween(toSortAsk.getValue(),1,30):
            entriesToSort=int(toSortAsk.getValue())
            numberOfRows=maxRows
            if entriesToSort<maxRows:
                numberOfRows=entriesToSort
            break
        enterPressed=False
        showError("Must an integer be within 1 to 30")

#The following code closes the previous and initializes the next
toSortAsk.close()
enterButton.grid_forget()
stopButton.grid_forget()
enterButton.grid(row=numberOfRows+1)
stopButton.grid(row=numberOfRows+1,column=2)
enterPressed=False
for i in range(entriesToSort):
    rowManager.append(tkinterInput(i%maxRows,i//maxRows*2,"Entry "+str(i)+":"))

#Second UI loop for the value of entries
while True:
    appUI.update()
    if enterPressed:
        largestEntry=0 #For sizing the display window
        for i in range(entriesToSort):
            if not isIntegerBetween(rowManager[i].getValue(),1,30):
                enterPressed=False
                showError("All entries must be integers within 1 to 30")
                break
            else:
                listToSearch.append(int(rowManager[i].getValue()))
                if largestEntry<int(rowManager[i].getValue()):
                    largestEntry=int(rowManager[i].getValue())
    if enterPressed:
        if isSorted(listToSearch):
            break
        showError("Entries must be in order from lowest to highest")
        enterPressed=False
    listToSearch=[]

#The following code closes the previous and initializes the next
for i in range(len(rowManager)):
    rowManager[i].close()
rowManager=[]
rowManager.append(tkinterInput(0,0,"Enter the integer to search for:"))
enterButton.grid_forget()
stopButton.grid_forget()
enterButton.grid(row=1)
stopButton.grid(row=1,column=2)
enterPressed=False

#Third UI loop for the entry to search for
while True:
    appUI.update()
    if enterPressed:
        if isIntegerBetween(rowManager[0].getValue(),1,30):
            entryToFind=int(rowManager[0].getValue())
            break
        enterPressed=False
        showError("Entries must be an integer within 1 to 30") 

#The following code completely closes the tkinter window
appUI.destroy()

#Turtle display
#The numbers might look arbitrary but they generally make the size right
appDisplay=turtle.Screen()
appDisplay.title("Binary Search Algorithm")
appDisplay.bgcolor("black")
screenHeight=200
if 21*largestEntry+75>screenHeight:
    screenHeight=21*largestEntry+100
appDisplay.setup(width=(21*len(listToSearch)+640), height=screenHeight)

#This variable type is used to display each entry of the list as a bar in the Turtle display
class turtleDisplaySortList():
    entry=turtle.Turtle()
    entry.speed(0)
    entry.penup()
    entry.color("white")
    entry.shape("square")

    def __init__(self,value,entryNumber,totalEntries,biggestEntry):
        self.value=value #Value of the item in the original list (used for size)
        self.entryNumber=entryNumber #The number of the entry (used for X position)
        self.totalEntries=totalEntries #The number of total entries (also used for the X position)
        self.biggestEntry=biggestEntry #Value of the biggest entry (used for the Y position)

        self.draw()
    
    def setColour(self,colour): #Sets the colour of the entire entry (for marking the item as either the target or not)
        self.entry.color(colour)
        self.draw()
    
    def draw(self): #Draws the item as a bar
        self.entry.setpos(self.entryNumber*20-10*self.totalEntries,-10*self.biggestEntry)
        self.entry.showturtle()
        for i in range(self.value):
            self.entry.goto(self.entryNumber*20-10*self.totalEntries,i*20-10*self.biggestEntry)
            self.entry.stamp()
        self.entry.hideturtle()

    def clean(self): #Clears itself (DOES NOT WORK CORRECTLY RIGHT NOW)
        self.entry.clearstamps()

    def getX(self): #Gets its X position, this is only used for the position of the mid arrow in the binary search later
        return self.entryNumber*20-10*self.totalEntries

#This resets and then sets up the display
listDisplay=[]
appDisplay.tracer(0)
for i in range(len(listToSearch)):
    listDisplay.append(turtleDisplaySortList(listToSearch[i],i,entriesToSort,largestEntry))

#This writes what is going on to show how binary search works
actionWriter=turtle.Turtle()
actionWriter.speed(0)
actionWriter.color("white")
actionWriter.penup()
actionWriter.hideturtle()
actionWriter.setpos(-10*entriesToSort-300,0)
def aClear(): #Clears the current message
    actionWriter.clear()
def aWrite(message): #Writes the new message
    aClear()
    actionWriter.write(message)
    time.sleep(3) #SET TIME AS 3 OR ABOVE OR IT IS NOT VISIBLE

#This keeps track of which entry of the list it is on
listTracker=turtle.Turtle()
listTracker.speed(0)
listTracker.penup()
listTracker.color("white")
listTracker.shape("arrow")
listTracker.setheading(90)
listTracker.setpos(0,-10*largestEntry-30)

appDisplay.tracer(1) #Makes the changes visible

#Updates all of the bars nessecary to update to the correct colour to visualize binary search
def updateColours(aboveBelowExact,targetLocation):
    appDisplay.tracer(0)
    if aboveBelowExact=="above": #Sets all bars below (and including) the current to red (the entry is not the desired value)
        for i in range(len(listDisplay)):
                if i<=targetLocation:
                    listDisplay[i].setColour("red")
    elif aboveBelowExact=="below": #Sets all bars above (and including) the current to red (the entry is not the desired value)
        for i in range(len(listDisplay)):
                if i>=targetLocation:
                    listDisplay[i].setColour("red")
    elif aboveBelowExact=="exact": #Sets the current bar to green (the entry is the desired value)
        for i in range(len(listDisplay)):
                if i==targetLocation:
                    listDisplay[i].setColour("green")
    else: #Sets all bars to red (none of the entries are the desired value)
        for i in range(len(listDisplay)):
            listDisplay[i].setColour("red")
    appDisplay.update()
    appDisplay.tracer(1)
    
#This is a binary search function altered to show the process behind it
#aWrite is used to tell the user what is going on
#The colours of the bars are updated as nessecary (red for not the entry, green for the entry)
#listTracker is used to show which entry is being checked for the value
def binarySearchTracked(arr,target,low,high):
    if low<=high:
        mid=(low+high)//2
        appDisplay.update()
        listTracker.setx(listDisplay[mid].getX())
        aWrite("The midway between the lowest entry ("+str(low)+") and highest entry ("+str(high)+") is entry "+str(mid)+".")

        if arr[mid]==target: #If it is the value that is being looked for
            updateColours("exact",mid)
            aWrite(str(listToSearch[mid])+" (entry "+str(mid)+") is the item we were looking for")
            return mid
        if arr[mid]<target: #If it is below the value that is being looked for
            aWrite(str(listToSearch[mid])+" (entry "+str(mid)+") is below the item we are looking for")
            updateColours("above",mid)
            aWrite("Since it is ordered, all items below entry "+str(mid)+" are also below the target "+str(target))
            return binarySearchTracked(arr,target,mid+1,high)
        #If it is above entry that is being looked for
        aWrite(str(listToSearch[mid])+" (entry "+str(mid)+") is above the item we are looking for")
        updateColours("below",mid)
        aWrite("Since it is ordered, all items above entry "+str(mid)+" are also below the target "+str(target))
        return binarySearchTracked(arr,target,low,mid-1)
    #If the value is not in the list
    updateColours("all",0)
    aWrite("None of the items in the list were the value we were looking for")
    return -1

#Initializes the search
binarySearchTracked(listToSearch,entryToFind,0,len(listToSearch)-1)

turtle.done() #Keeps the window open until it is closed (or the program is otherwise terminated)
#End of the program