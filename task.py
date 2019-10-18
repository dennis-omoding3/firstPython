taskList=[23,"jane",["lesson 23",560,{"currency":"kes"}],987,(76,"john")]
# 1. determine the type of var in task list using an inbuilt function
print(type(taskList))
# 2.print kes

print(taskList[2][2]["currency"])
# 3.print 560
print(taskList[2][1])

# 4. use a function to determine the length of taskList
print(len(taskList))

# 5. change 987 to 789 using an inbuilt method or assignment
print(str(taskList[3])[::-1] )#typecasting into a string because integer cannot be reversed

#print(a.reverse())
# 6. change the name "john" to "jane" without using assignment
#NA a tuple cannot be modified

#print(taskList.index("jane"))
