""""
Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""

a = "This is string" # Stirng data
print(a)

b = 10  # int data
print(b)

c = 1.4 # float
print(c)

d = 1j # Complex data
print(d)

e =[ "Chat GPT", "DeepSeek", "Bird"] # List data type
print(e)

f = ( "Apfel", "Banane", "Tomaten" ) # tuple data type
print(f)

g = range(4) # range 
print(g)

h = {"name" : "Nazmul Hasan", "age" : 23} # dict
print(h)

i = {"Apfel", "Erdbreen", "Gemuse"} # Set data type
print("Set data:", i)

j = frozenset({"apple", "banana", "cherry"}) # Frozenset
print("Frozen set data type:", j)

k = True # Bool
print("Boolean Data type", k)

l = b"Byte data type" #Bytes data type
print("Byte data type", l)

m = bytearray(5) # bytearray
print("Byte array", m)

n = memoryview( bytes(5)) # Memory view
print("Memory View", n)

o = None # NoneType data
print("None type data", o)



