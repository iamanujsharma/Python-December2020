#Python is a popular programming language. 
#It was created by Guido van Rossum, and released in 1991. 

print("Hello, World") #gives output "Hello, World"

name = "John"         #declaring a string 
print(name)

age = 32              #declaring an integer
print(age)

print("Hello"+" "+name+"!!") #concatenation of string and a variable

#print("You are "+age+" years old") if you do this you will get an error because we can not add string and an integer

#but what is string and integer, these are data types

#Data Types
name = "John"
age = 32
weight = 58.3
print(type(name)) #string
print(type(age))    #int
print(type(58.3))   #float

#we can change the data types using casting method

#casting from int to str
print(type(str(age))) #str

#We can not cast int to str

#casting int to str
print(type(int(weight)))







