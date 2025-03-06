#Booleans represent one of two values: True or False.
print(10 > 9)
print(10 == 9)
print(10 < 9)

mein_alt = 23
dein_alt = 21
if mein_alt > dein_alt:
    print("I'm older then you")
else:
    print("I'm not older the you")
a = ""
print("Empty anything return flse: ",bool(a))

#Some Values are False
#In fact, there are not many values that evaluate to False,
# except empty values, such as (), [], {}, "", the number 0, and the value None. 
# And of course the value False evaluates to False.

class myclass():
    def __len__(self):
        return 0
myobj= myclass() #here created a class object 
print(bool(myobj))

def myFunction():
    return True

if myFunction():
    print("Yes")
else:
    print("No")

# isinstance() function, which can be used 
# to determine if an object is of a certain data type:
print("Checking int", isinstance(a, int)) #Check if an object is an integer or not: