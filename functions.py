#functions

# syntax
#
# def functionName():
#     #statements
#functionName()

#example 1
# def hello():
#     print("hello world")
#     print("dennis omoding") #you can add as many statements as possible
#
# hello() #calls the function
# hello()#replicates the functions

#example 2(passing parameters)
#
# def add_two_numbers(a,b):
#     summ=a+b
#     print(summ)
# add_two_numbers(4,9)
# add_two_numbers("dennis","omoding")

#do subtraction and multiplication

          #pass a number then determine if its > or <100
# def greater_or_equal(a):
#  if a<100:
#         print("less than 100")
#  elif a==100:
#     print("its 100")
#  else:
#          print("greater than 100")
# greater_or_equal(100)

        #pass a number and determine whether its dividible by 2
# def divisible(c):
#     if c%2!=0:
#         print("not divisible")
#     else:
#         print("divisible")
# divisible(8)

       #strings
#write a function to change your name to upper case

# def my_name():
#     first_name="dennis"
#     print(first_name.upper())
# my_name()

#change good morning to good evening

def replace_name():
    greeting="good morning"
    print(greeting.replace("morning","evening"))
replace_name()