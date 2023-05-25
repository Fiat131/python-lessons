## Lesson 8 String slicing
## Slicing = create a substring by extracting elements from another string
## looks like [start:stop:step]
## can be aplied to different collections as well

## to slice strings we either use a indexing([]) operator or the slice function (()) to create a slice object

## three optional arguments (three fields to fill) depending on where and how we want to slice our string

## starting index

name = "Ali Kapalıdere"
## we want a substring based off a sliced portion off a string

## start index
first_name = name[0]
## remember computers always count from 0 so the first letter of my sting has the 0 index
print(first_name)

## stop index
first_name = name[:3] # you dont have to write 0 if you are indexing the start of the string
## the [start] index is inclusive meaning the substring includes the inexed character but [stop] is exclusive meaning the indexed charecter is not in the substring
print(first_name)

last_name = name[4:8] # you can write [4:] if you want all of the rest of the string
## notice terminal and where the string ends
print(last_name)

## step index
funky_name = name[::2] ## this statement can be translated as "funky_name is a string and equal to name but from start to the finish and only one out of every second character"
## if you leave the fields to be empty python will automaticaly assume them to be [0:∞:1]
print(funky_name)

## this is how you reverse a string

reversed_name = name[::-1] # the step index reversed the read order of the string 

print(reversed_name)

### Slice Function

website1 = "https://www.google.com/"
website2 = "https://www.youtube.com/"
website3 = "https://www.wikipedia.org/"
## we want a substring that is only based off on the website name mot anything else

slice = slice(12,-5) #exacly like indexing we can add three values but with the slice function we use a comma(,) instead of a colon(:)
## we can not use the same stopping index for every website so we can use a negative index
## when we use negative indexes. negative indexes work exacly the same way but the character most on the right begins with a negative index of minus 1 and goes to a lower number as you read backwards
## we now have a slice object and we can reuse this how ever many times we want

print(website1[slice])
print(website2[slice])
print(website3[slice])
###end