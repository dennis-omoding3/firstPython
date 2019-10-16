taskList=[23,"jane",["lesson 23",560,{"currency":"kes"}],987,(76,"john")]
# 1. determine the type of var in task list using an inbuilt function
print(type(taskList))
# 2.print kes
second_list=taskList[2]
dict=(second_list[-1])
print(dict["currency"])
# 3.print 560
print(second_list[1])

# 4. use a function to determine the length of taskList
print(len(taskList))

# 4. change 987 to 789 using an inbuilt method or assignment
a=taskList[3]
print(a[-1:0])
#print(a.reverse())
# 6. change the name "john" to "jane" without using assignment
#print(taskList[4].replace([1],"jane"))
