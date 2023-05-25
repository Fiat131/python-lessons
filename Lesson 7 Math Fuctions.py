## Lesson 7 Math Fuctions
import math #to gain acces to the math moddule in pyhton

pi = 3.14

#print(round(pi))
## rounds a number to the closest interger

#print(math.ceil(pi)) #[ceil] is short for ceiling
## rounds a number "up"(changes it to the closest interger that is bigger than this[pi] value)

#print(math.floor(pi))
## rounds a number "down"(changes it to the closest interger lower than this[pi] value)

#print(abs(pi)) #abs is short for absolute value and there is no need to write math because this function is python from the start
## tells how far away a number is from zero

#print(pow(pi,2)) # ""pi" to the power of "2"" pow is short for "power"
## multiplies a value by itself. [<value to be multiplied>,<how many times it will be multiplied>]

#print(math.sqrt(pi)) #it cant do negative numbers (just like i cant) sqrt is short for "square root"
## this function is from the math module so we write [math.sqrt(<value>)]
## finds a number that needs to be multiplied by itself to become the given value

x = 1
y = 2
z = 3

print (max(x,y,z)) #max is short for "maximum"
## finds the largest value from given values

print (min(x,y,z)) #min is short for minimum
## finds the lowest value from given values
###end