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

# Write a function that takes a string as parameter, which will contain single digit numbers, 
# letters, and question marks, and check if there are exactly 3 question marks 
# between every pair of two numbers, whose sum is 10. 
# If so, then your program should return the string true, otherwise it should return the string false. 
# If there aren't any two numbers then your program should return false 
# as well.
# Example1: input = "sdfhdsl4??sfasdfga?1sdjkfhbdsjhfkb" output = False (the two numbers do not sum to 10)
# Example2: input = "sdfhdsl4??sfasdfga?6sdjkfhbdsjhfkb" output = True (the two numbers sum to 10)
# weight = 8

def question_mark(string):
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    characters = [char for char in string]
    counter = 0
    for i in characters:
        if i == "?":
            counter = counter + 1

    if counter == 3:
        # print("yay 3 queation marks")
        list1 = string.split("?")
        # print(list1)
        # print(len(list1))
        numberstocheck = []
        numbers1 = []
        numbers2 = []
        
        for char in list1[0]:
            if char not in alphabets: 
                x = int(char)
                numbers1.append(x)
        numberstocheck.append(numbers1[-1])

        for char in list1[-1]:
            if char not in alphabets:
                y = int(char)
                numbers2.append(y)
        numberstocheck.append(numbers2[0])

        if len(numberstocheck) >= 2:
            x = sum(numberstocheck)

            if x == 10:
                print("True (the two numbers sum to 10)")
            else:
                print("False (the two numbers do not sum to 10)")
        else: 
            print("False (there aren't any two numbers to sum)")

    
    else:
        print("False (you did not input exactly 3 question marks)")

    
    return 

question_mark("sdfhdsl4??sfasdfga?1sdjkfhbdsjhfkb")

question_mark("sdfhdsl4?8vb9?sfasdfga?1sdjkfhbdsjhfkb")

question_mark("sdfhds24??sfasdfga?6sdjkfhbdsjhfkb")
question_mark("sdfhds24??sfasdfga?6sd7jkfhbdsjhfkb")