'''
PlotQuestion.py

See the README for the full description of the desired plot.


TOTAL POINTS AVAILABLE: 10 

10 points - desired plot is generated and code is efficient 

6-9 points - desired plot is generated, but code could be 
improved (e.g., the students used unnecessary if statements)

4-6 points - plot is generated but it has some errors

1-4 points - no plot is generated, but some effort was made to generate one

0 points - no effort made to answer question





'''
# Write a Python script that reads in the text file `data.txt`, in the folder Data, and generates 
# one plot as shown in image.png
# 
# Read the text file (hint: the delimiter in the 
# file is `','`) and notice that there are 9 columns. The first column represents the time of the 
# measurement, whereas the other columns represent data collected 
# at that specific time. To get maximum marks you need to be sure that the code you write can be executed on a computer different than yours (meaning, do not use
# absolute paths when opening and closing directories).
# 
# - Plot the data contained in the 6th column against the data contained in the 1st column (i.e., 
#   data in the 6th column on the y axis, data in the 1st column on the x axis). 
# - Plot the data contained in the 3rd column against the data contained in the 1st column (i.e., 
#   data in the 3rd column on the y axis, data in the 1st column on the x axis). 
# - Add an xlabel as "Time [s]" and a ylabel as "Speed [m/s]"
#

import matplotlib.pyplot as plt  
import os
# path = 'C:\\Users\\User\\Documents\\Computing1\\MOCK\\Plot question\\Data\\data.txt'  This was specifically for my laptop


x = os.getcwd()
y = x + "\Plot question\Data\data.txt" 
# print(y)
path = y

file = open(path, "r")
a = file.read()
datapoints = a.split() # I will convert the file into a list containing all the elements
# print(datapoints)
list = [float(data) for data in datapoints] # Then I will create a list of all the floats ready for some maths!
# print(list)

column1 = list[0::7]
column2 = list[1::7]
column3 = list[2::7]
column4 = list[3::7]
column5 = list[4::7]
column6 = list[5::7]
column7 = list[6::7]
averages = []

plt.plot(column1, column6) 
plt.plot(column1, column3)

plt.xlabel("Time [s]")
plt.ylabel("Speed [m/s]") 

plt.show()


file.close()

