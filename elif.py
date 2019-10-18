#elif is used when dealing with a number of option

avg_marks= input("enter avg_marks:")
avg_marks=eval(avg_marks)
if avg_marks >=70 and avg_marks <=100:
    print("A")
elif avg_marks>=60:
    print("B")
elif avg_marks>=50:
    print("C")
elif avg_marks>=40:
    print("D")
else:
    print("unfulfilled")