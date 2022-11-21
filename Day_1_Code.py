# Introduction
# Day 1

print("Welcome to Day 1 of python challenge")

#Opertors
print("Welcome to Operators")
print(2 + 3)    #Addition
print(2 - 3)    #Subtraction
print(2 * 3)    #Multiplication
print(2 / 3)    #Division
print(2 ** 3)   #Exponential
print(2 % 3)    #Modulous
print(2 // 3)   #Flooe division

#Data Types
print("Checking data types of variable")
# You can get the data type of a variable with the type() function.
# type() - to check type of variable
# id() - to get address of object
print(type(10))                     #Integer
print(type(10>20))                  #Boolean
print(type(3.14))                   #Float
print(type(1+3j))                   #Complex
print(type('30 Days Of Code'))      #String
print(type([1, 2, 3]))              #List / Array
print(type({'Name': 'Ankush'}))     #Dictionary
print(type({2.4, 5.7, 9.8}))        #Set
print(type((2.4, 5.7, 9.8)))        #Tuple


# TYPE CASTING / Type Coersion
print("TYPE CASTING / Type Coersion")
# We can convert one type value to another type. This conversion is called Type Casting or Type coersion.
# The following are various inbuilt functions for type casting.
# int()
# We can convert from any type to int except complex type
print(int(24.5))
# float()
# We can convert any type value to float type except complex type
print(float(16))
# complex()
print(complex(32))
# bool()
print(bool(76<98))
# str()
print(str(45))

### we will learn more about these concepts in upcoming days ###
