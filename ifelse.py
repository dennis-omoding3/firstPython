if True:
    print("True")

marks= input("what is your kcpe marks:")
marks=eval(marks) # eval takes care of int and float
# if marks >= 350 and marks <=500:
#      print("conrats you are admitted")
#  else:
#      print("sorry, try again next year")

# nested if i.e if inside if
if marks <0 or marks >500:
    print("your marks are unrealistic")
else:
    if marks >= 350 and marks <=500:
        print("conrats you are admitted")
    else:
        print("sorry, try again next year")
