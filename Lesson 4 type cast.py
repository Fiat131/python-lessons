## type casting = convert data type of a value to another data type
x = 5 #interger
y = 2.0 #float
z = "3" #string

## this is how you type cast
#y = int(y)

#print(y)
## notice terminal {2.0} becomes {2} after we type cast the floating point data to interger

## when we do this
#print(z*3)
## notice terminal {333}

## if we want to do math we can't do it with strings, we need float or int.
#print(int(z)*3)
## notice terminal {9} is z multiplied by 3. we can do this because we turned the z string into a interger

## you cannot normally display a string along with a interger or a float because we are using a string concatenation
## for example
#print("x is "+x)
## will cause a compilation error

# it must be like this
#rint("x is "+str(x))
#print("y is "+str(y))

###end