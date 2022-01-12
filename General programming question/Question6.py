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

# Write a function that returns the largest value that is also an even value in the
# input dictionary whose values are all whole numbers (values, not keys).
# # weight = 5 

def value_greatest_even(dictionary):
    dictionaryvalues = [x for x in dictionary.values()]
    print(f"checking {dictionaryvalues} for the largest even number...")
    largestvalue = 0
    for value in dictionaryvalues:
        while type(value) != int:
            return print("ERROR: One of the values is not an integer variable")
             
        else:
            for x in dictionaryvalues:
                if (x > largestvalue) and (x%2 == 0):
                    largestvalue = x

    if largestvalue>0:
        print(largestvalue)
        return largestvalue
    else:
        print("ERROR: No even numbers found")
        return None
        
             

dictionary1 = {"a":"Maz", "b":19, "c": 6, "d":12}
dictionary2 = {"x":9, "y":1, "z":3}
dictionary3 = {"k":2, "l":1, "m":16}

value_greatest_even(dictionary1)
value_greatest_even(dictionary2)
value_greatest_even(dictionary3)