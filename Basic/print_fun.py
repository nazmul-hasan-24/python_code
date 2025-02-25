#The Python print() function is often used to output variables.
name = str("Nazmul Hasan")
print(name)
print(type(name))


#In the print() function, you output multiple variables, separated by a comma:
#You can also use the + operator to output multiple variables:
x = "Python"
y = "is"
z = "awsome"
print(x, y, z)
print(x + " " + y + " " + z)


my_name = "Nazmul"
age = 23
height = 5.5
print("Name:", name,"Age:", age, "Height:", height)

name = "Nazmul"

print(f"My name is {name} and I am {age} years old.")

print("Line 1\nLine 2")  # Newline
print("Tab\tSeparated")  # Tab space
print("Backslash: \\")   # Backslash

#printing without new line
print("Hello", end="")
print("World")

