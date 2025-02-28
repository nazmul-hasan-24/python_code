#Strings in python are surrounded by either single quotation marks, or double quotation marks.
name = "Nazmul Hasan"
print(name)

#Multiline Strings
#Also I can use single quotes
intor =  """My name is Nazmul Hasan. I'm 23 years old
and live in Lakshmipur, Bangladesh"""
print(intor)

#Strings are Arrays
#Array index start from 0
stirng_array = "String array"
print(stirng_array[2])

#Looping Through a String
for x in "pineapple":
    print(x)

for y in stirng_array:
    print(y)

# using len() fun we can check the length of string
print(len(stirng_array))

#Check String
# We can check certain phrase or char in a string using in or i keyword 
# Result type bool
print("old" in intor)

if "ld55" in intor:
    print("Yes, old is present")
else:
    print("Not present old word")

#Check if not present using not in keyword

print("Hasan3" not in intor)

#using is not
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")