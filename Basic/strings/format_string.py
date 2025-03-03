#we cannot combine strings and numbers like this

age = 23
#txt = "My name is Hasan, I am " + age
#print(txt)

#But we can combine strings and numbers by 
# using f-strings or the format() method!

f_text = f"My name is Hasan, I'm {age} years old"
print(f_text)

name = "My name is Hasan "
f_txt = f"{name}, I'm {age}"
print(f_txt)

#Placeholders and Modifiers
#A placeholder can contain variables, operations, functions, and modifiers to format the value.

price = 24
t_price = f"Das Handy prais {price} Euro"
print(t_price)
#A modifier is included by adding a colon : followed by a legal formatting type, 
# like .2f which means fixed point number with 2 decimals:
t_price2 = f"The price is {price:.2f} Euro"
print(t_price2)

