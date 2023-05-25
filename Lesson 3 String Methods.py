### delete the first hashtag(#) on all lines to see font colours and run program to see example demonstrations.
name = "ali"

#print(len(name))
## [len(name)] shows lenght of string
## notice terminal {3} for 3(three) characters in [Ali]

## "<string_name>.find("part_of_string_to_find")" finds charachter in a string

#print(name.find("a"))
##notice terminal {0}. Computers always count from zero so the first character is the zero(0)th character in the string

## capitilize the first character in a string (only first character)

#print(name.capitalize())

## this is how you capitilize everything

#print(name.upper())
## uppercase
#print(name.lower())
## lowercase

## this how you print true or false based on if string is numbers or letters

number = ("123")
#print(name.isdigit())
#print(number.isdigit())
## notice {False} for line 26 and {True} for line 27  

## check to see if your string is only letters

full_name = "Ali Kapalıdere"
#print(full_name.isalpha())
## notice terminal {False} because of space the string has more than letters

## count how many characters there are in a string

#print(full_name.count("a"))
## notice terminal {2} because it is case sensetive

## replace letters or parts of string

#print(full_name.replace("ı","i"))

## this is not a string method but nice to know
## you can print multiple times

#print(full_name*3)
#print((full_name+" ")*3)

###end