#To insert characters that are illegal in a string, use an escape character.

#name = "My name is "Nazmul" Hasan " #Een an error
name = "My name is \"Nazmul\" Hasan "
print(name)

#\'	Single Quote
#\\ Backslash
#\n New line
# \r Carriage Return
#t Tab
#b Backspace
#This example erases one character (backspace):
back_space = "Hello \bWorld!"
print(back_space) 
#\f Form Feed
#\ooo Octal value
octal_val = "\110\145\154\154\157"
print(octal_val) 

#\xhh Hex value
hex_val = "\x48\x65\x6c\x6c\x6f"
print(hex_val) 