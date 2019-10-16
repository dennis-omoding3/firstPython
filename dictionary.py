personal=["dennis omodin","eldoret",24,False,"kenyan"]

#a dictionary is a data structure that holds key and value
a=0#int
b=0.0#float
c="" #str
d=[]#list
e=() #tuple
f={} #dictionary

print(type(f))

personal={"name":"dennis omoding","location":"eldoret","age":24,"is_short":False}
print(personal)

#access using the key
print(personal["location"])
print(personal["age"])

#dictionary methods

personal.clear()#removes everything from a dictionary
print(personal.keys())