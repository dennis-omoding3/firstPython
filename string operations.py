#concatenation
first_name="dennis"
last_name="omoding"
#use .format to concatenate
full_name="{}{}".format(first_name,last_name)
print(full_name)
print("the tallest person is {} from the family of {}".format(first_name,last_name))
# #full_name=first_name+" "+last_name
# #print(full_name)
#
# names="dennis omoding"
# name2="brian bett"
# name3="brigid bett"
# print(names.capitalize())
# print(name2.title())
print(name3.upper())

sen="i am going to have dinner because dinner makes me stronger"
#count displays the number of times a string appears
print(sen.count("dinner"))
#count number of letter a
print(sen.count("a"))
#count number of spaces
print(sen.count(" "))
#strng slicing
#left of the colon signifies the starting point whereas the right of the colon signifies the letter before the last letter
print(sen[0])
# sen[0] will print the first letter of sen sen[-1] will print the display the letter before the last
print(sen[0:-1])
print(sen[0:9])
jina="omoding"
print(jina[0:-1])
print(jina[1:6])

#revert jina
print(jina[::-1])
print(jina.split()) #splits the string
print(sen.split())
clubs=["manchester_utd", "tottenham", "chelsea","watford"]
clubs[0]="wolves" #replaces the club in position 1 with another club
print(clubs)
team=clubs.replace("tottenham","stoke")
print(team)
#data structures