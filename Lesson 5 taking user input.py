## This is how you accept user input in python

name = input("What is your name?: ")
## notice terminal {What is your name?:} click and write anything
print ("Hello "+name)
## notice terminal the printed "name" is your input

age = int(input("How old are you?: "))
## we defined "age" as an interger input for "How old are you?:" user prompt
age = age + 1
## we did an addition because we can(and to show that you as the programmer can do things with user inputs now)
print("You are "+str(age)+" years old")
## because "age" is a interger now we have to turn it into a string to print
 
height = float(input("How tall are you?: "))

print ("You are "+str(height)+"cm tall")

#remember that if you want to use inputs for math then you must use int or float data type. and numbers with decimal points do not work in int.
###end