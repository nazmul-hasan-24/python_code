""""
Complex Numbers in Python
In Python, complex numbers are a built-in data type
used for mathematical computations involving imaginary
numbers. A complex number is represented as:

a + bj

a is the real part
b is the imaginary part
j represent √-1 (the imaginary unit in Python, similar to 
i in mathematics).

"""
complex_num = 4j
print(complex_num)

#a is the real part
#b is the imaginary part

c1 = 3 + 4j
c2 = 7 - 2j
print("Addiation", c1 + c2) #addition 
print("Substruction", c1 - c2) # substruction
print("Divition", c1 / c2) #division

""""

"""
print("Multiplication", c1 * c2) #Multiplication

print("Real number: ", c1.real, "Imagenary number: ", c1.imag)