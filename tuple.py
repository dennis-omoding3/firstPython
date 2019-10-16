#definition of data types in python
a=0 #integer
b=0.0 #float
c="" #string
d=[] #list
e=()#tuple

#tuples are like lists but cannot be manipulated/altered

days_of_week=("mon","tue","wed","thur","fri","sat","sun")
print(type(days_of_week))
print(len(days_of_week))

#methods of a tuple are only count and index

print(days_of_week.index("sat"))