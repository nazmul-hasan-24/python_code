#There are three numeric types in Python:

#Int, or integer, is a whole number, positive or negative, 
#without decimals, of unlimited length.
a = 11 #int

#Float, or "floating point number" is a number, positive or negative, 
# containing one or more decimals.
b = 3.4 #float

#Float can also be scientific numbers with an "e" to indicate the power of 10.
float_scientific = 13e5
print(float_scientific)
print(type(float_scientific))

#Complex numbers are written with a "j" as the imaginary part:
c = 2j #complex
d = 4-5j
#varify type 
print(type(a))
print(type(b))
print(type(c))

#Type Conversion

a1 = float(a) #convert from int to float
b2 =int(b) #Conver from float to int
c3 = complex(a) #conver from int to complex
#Note complex number can't be converted to int or float
print(type(a1))
print(type(b2))
print(type(c3))

#Random Number
import random
print(random.randrange(1,40)) #generate random number between 1 to 40

