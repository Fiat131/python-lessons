## Lesson 9 İf statements
## if statements = a block of code that will execute if it's condition is true

age = int(input("How old are you?: "))
## notice the block of code you put after this is indented. any indented code is a part of that if statement
if age == 100: # we write double equal signs because python will think age is equal to 100 instead of comparing the already given value
    print("You are a century old!") # if this condition is false it will simply skip over the if statement
elif age >= 18: # make sure you are not typing in the indentation
    print("You are an adult!")
elif age < 0: 
    print("You haven't been born yet!")
else: # this ends the if statement
    print("You are a child!")
## again make sure you are not in the indentation when ending an if statement
###end