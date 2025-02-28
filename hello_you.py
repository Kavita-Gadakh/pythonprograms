#Ask user for name
 
name = input("What is your name?")
#print(name)

#Ask user for age

age = input("What is your age?")
#print(age)

#Ask user for city

city = input("what city you do live in?:")
#print (city)

#Ask user what they enjoy

love = input("What do you love doing?: ")
#print (love)

#Create output text

string = "your name is {} and you are {} years old. you live in{}and you love{}"
output = string.format(name,age,city,love)



#Print Output On Screen

print(output)
