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

# Write a function that returns the longest key in the input dictionary 
# whose keys are all strings.
# weight = 2

def longest_key(dictionary):
    keys = []
    longestkeyvalue = 0
    for key in dictionary:
        while type(key) != str:
            return print("One of the keys is not a string variable")
             
        else:
            keys.append(key)
    for key in keys:
        if len(key) > longestkeyvalue:
             longestkeyvalue = len(key)
    for key in keys:
        if len(key) == longestkeyvalue:
            print(key)
            return key


dictionary1 = {"name": "Maz", "age": "19", "height": 6, 0:"x"}
dictionary2 = {"name": "Maz", "age": "19", "height": 6}
longest_key(dictionary1)
longest_key(dictionary2)


