#a list is a collection of more than one variable

#int []

#a python list
personal=[]
print(type(personal))
print(len(personal))

personal=["dennis omoding",24,20000.0,"kasarani"]
print(len(personal)) # len determines the number of items in a list

students=["linet","ali","letina"]
print(students)
print(students[0])
new_student=["dennis"]
all_students=students+new_student
print(all_students)
#or

#methods of a list
all_students.append("grace") #adds a new item onto the list
print(all_students)
#all_students.clear() #deletes everything in the list
print(all_students)
students=all_students.count("dennis") #determines the number of times an elememt appears in the list
print(students)
all_students.append(" ")
print(all_students)
all_students.append("dennis")

print(all_students.count("dennis"))
pos=all_students.index("letina") #index determines the position of an item/element in a list
print(pos)
print(all_students)
print(all_students[2:4]) #prints items in position 2 and 4(not included) i.e 2 and 3
all_students.pop(5) #pop removes an item when the position is known
print(all_students)
all_students.insert(0,"erik") #adds new element to a specific position
print(all_students)

