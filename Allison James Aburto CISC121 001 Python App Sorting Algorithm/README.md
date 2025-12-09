## Author and Acknowledgment
Author: Allison (James) Aburto
Instructor: Dr. Rahatara Ferdousi
Course: CISC121 001 (Introduction to Computing Science I Fall 2025)

Acknowledgements:
https://www.geeksforgeeks.org/python/python-gui-tkinter/
for the general understanding of Tkinter

https://stackoverflow.com/questions/14824163/how-to-get-the-input-from-the-tkinter-text-widget
for getting taking input in Tkinter

https://docs.python.org/3/library/tkinter.html
for additional tkinter functions like changing the background colour

https://www.geeksforgeeks.org/python/turtle-programming-python/
https://docs.python.org/3/library/turtle.html
for a refresher on Turtle (I have used it before)

https://stackoverflow.com/questions/510348/how-do-i-make-a-time-delay
to make time delays

## Algorithm Name
Binary search

## Demo screenshots of test
SEE THE DEMOS FOLDER

## Problem Breakdown & Computational Thinking (You can add a flowchart , write the four pillars of computational thinking briefly in bullets, etc.)
# Why Binary Search: 
I chose a to implement and visualize a binary search algorithm because I felt it would be one of the more simple programs to make but still interesting to visualize.
# Decomposition:
1) Take the middle value of the list.
2) If it is the value that's being looked for, return its position (end of steps).
3) If it is more than the value, ignore values greater (right). If it is less than the value, ignore values smaller (left).
4) Repeat the steps until either the value has been found, or you have ruled out all of the entries on the list.
5) If it is not in the list, return the position as -1
# Pattern Recognition:
It repeatedly compares the middle entry of the part of list being checked.
# Abstraction:
The user is able to see and change all entries at once while entering.
# Algorithm Design:
Input: List
Processing: (Steps in decomposition)
Output: Location of an instance of the value being searched for (or -1 if it is not in the list)

## Steps to Run
1) Make sure you have all the requirements in requirements.txt before attempting to run the program
2) Press the red stop button at any time to stop the program
3) Enter the integer number of entries in your list and then press the green enter button (up to [update how many])
4) Enter all of the entries of your list (each entry must be an integer from 0 to [max], the entries must be ordered)
5) Press the green enter button, and watch the visualization of the binary search algorithm

## Github Link
https://github.com/allisonqueensuniversity/CISC121
