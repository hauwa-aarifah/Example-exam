'''
GeneralProgramming.py



Functions performing operations on basic Python data structures.

TOTAL POINTS AVAILABLE: 40 (notice that each exercise has its own weight)


1 * weight points -  The program works flawlessly and the appropriate ideas to solve it, have been used.

0.75 * weight points - The student has understood the logic and the program works for most inputs.
The code could use some improvement or it is very hard to read. The appropriate ideas to solve the problem have been used.

0.5 * weight points - The student has understood the logic but there is some major bugs, or the program is incomplete. 
This score is also assigned for programs that execute as intended but in a 
very inefficient way (for instance, using a very long list of if statements 
when the problem could be solved easily with a loop).

0.25 * weight points -  The student has attempted to solve the exercise but, either there is a 
logical error in the program (e.g., wrote something but it wouldn't solve the problem) 
or the program is largely incomplete.

0 points - The student has not attempted to solve the exercise or missed the point entirely 
(e.g., blank page or solved something unrelated to the question).




'''

# Write a function with two inputs, one matrix (a list of lists, in which every sublist is the same dimension)
# and a single character. The function will return true if it can find, within the matrix, a 2x2 submatrix made
# with the single character.
#
# Example: Consider the following list, myList = [[1,2,"a","a"], ["a", 3, "a", "a"], [1, 4, 6, 8], [5, 2, 6, 6]]
# that corresponds to the following matrix
# 
#
#
# |  1   2  "a" "a"  |
# | "a"  3  "a" "a"  |
# |  1   4   6   8   |
# |  5   2   6   6   |
#
# in which case the function would return True, if the character was "a" and false otherwise.
# weight = 15

import numpy as np


def characterchecker(list, character):
    result = False
    if len(list)>0:
        result = all(item == character for item in list)

    if result:
        # print("True")
        return True
    else:
        # print("False")
        return False
    



def find_letter(matrix, character):
    answer = False
    value = len(matrix[1])
    array = np.array(matrix)
    shape = np.shape(array)
    x = int(shape[0])

    a = 0
    b = 0
    c = 0
    d = 1
    e = 1
    f = 0
    g = 1
    h = 1

    # print(array , "\n")
    for list in matrix:
        if len(list) != value:
            return print("ERROR: Incorrect matrix dimensions")
    
    else:
        for i in range(x-1):

            while a<x and  b<x and  c<x and d<x and e<x and f<x and g<x and h<x:
                twobytwo = [array.item(a,b), array.item(c,d), array.item(e,f), array.item(g,h)]

                # print(twobytwo)
                b = (b + 1)
                d = (d + 1)
                f = (f + 1)
                h = (h + 1)
                if characterchecker(twobytwo, character) == True:
                    print("True")
                    answer = True
                    return True
            else:
                # print("row check complete")
                a = (a + 1)
                c = (c + 1)
                e = (e + 1)
                g = (g + 1)

                b = (b - x+1)
                d = (d - x+1)
                f = (f - x+1)
                h = (h - x+1)

                
    print(answer)
        

myList = [[1,2,"a","a"], ["a", 3, "a", "a"], [1, 4, 6, 8], [5, 2, 6, 6]]
myList2 = [[1,2,2,2], ["a", 3, 2, 2], [1, 4, 6, 8], [5, 2, 6, "a"]]

find_letter(myList, "a") # should print True
find_letter(myList, "b") # should print False
find_letter(myList2, "2") # should print True
        
    



