### delete the first hashtag(#) on all lines to see font colours and run program to see example demonstrations.
## variables = a container for a value. Behaves asthe value that it contains.
## This is the "string" data type  (letters)

#first_name = "Ali"
#last_name = "Kapalıdere"
#full_name = first_name + " " + last_name
## [+ " " +] is so name does not print as "first_namelast_name"
## [print(type(name))] is to check value type. 
#print("Hello "+full_name)

## This is the "int" or "interger" data type (whole number)
## Pay attention! No quotes("") here! it is a string if in quotes.

#age = 20
#age = age + 1
## basic addition 
## can be short like [age += 1]
#print (age)
#print (type(age))
## notice terminal {<class 'int'>} when you run program
#print("your age is: "+str(age))
## [str(age)] you can "type cast" or turn int data type int string data type so it can be printed just like a string

## This is the "float" or "floating point number" data type (numeriv value that contains a decimal portion)
## Pay attention to the decimal point! if there is no decimal it is a int data type not float

#height = 170.6
#print (height)
#print (type(height))
## notice terminal {<class 'float'>} when you run program
#print ("your height is: "+str(height)+"cm")
## we type casted again! [str(height)] (did you notice we can add a bit more as long as it is a string data type? i wonder why it is called the string data type?)

## This is the "boolean" data type (True or False)
## very usefull for "if" statements
## Again this is not a string so No quotes("") here!

#human = True
#print("are you a human: "+str(human))
## type cast again [str(human)]
#print(type(human))
## notice terminal {<class 'bool'>} ("bool" is short for "boolean")
###end