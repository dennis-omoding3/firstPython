#while loop
# a=0
# while a<100:
#     print("dennis omoding")
#     a+=1 #increases by 1
#     print(a)
    # a while loop repeats execution  of its indented until the specified condition is false

saved_pin  = "9999"
tries=3

current=input("enter pin:")
tries-=1
while current != saved_pin and tries>0:
     current=input("enter pin:")
     tries-=1 #repeats the loop
if current!=saved_pin:
         print("card blocked")
else:
         print("welcome, proceed")