"Lists are used to store multiple items in a single variable."


"""List items are ordered, changeable, and allow duplicate values.

List items are indexed, the first item has index [0],"""
obst = ["apfel", "banane", "erdbreen"]
list1 = [1,3, 4, 5, 9,2, 3, 3, 3]
listBool = [True, False, True]
print(obst)
print(len(obst))
print(type(list1))

"""
The list() Constructor
It is also possible to use the list() constructor when creating a new list.
"""
list2 = list((22, 4, 55, 25))
print(list2)
print(type(list2))

#append()	Adds an element at the end of the list
obst.append("Kartofln")
obst.append(list1)
print(obst)
#obst.clear() # clear list
print("Clear all obst: ", obst)
obst2 = obst.copy()
print("Count number of elements ", list1.count(3)) # Returns the number of elements with the specified value

name = ["Hasan", "Parvej", "Rimon"]
age = [23, 26, 25]
name.extend(age)
print(name)

index = name.index("Parvej")
print("Index of Parvej: ", index)

name.insert(2, "Khaled")
print(name)

remove_specifc_ele = name.pop(2) #Removes the element at the specified position
print(remove_specifc_ele)

#remove()	Removes the item with the specified value
print(obst.remove("banane"))

#reverse()	Reverses the order of the list
cuntry = ["BD", "Ger", "Pak", "Afg"]
cuntry.reverse()
print(cuntry)
cuntry.sort()
print(cuntry)