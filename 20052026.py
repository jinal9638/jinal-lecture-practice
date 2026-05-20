#identity operators
#identity operators check whether two variables point to the same object
#'is' return True if both variables refers to the same object
#'is not' return True if both variables refers to the different object
a=[1,2]
b=a
c=[1,2]
print(a is b)
print(a is c)
print(a is not c)

#membership operator in python
#membership operator check whether a value exists in a sequnce like list, tuple string or diictionary
#'in' return True if value exists
#'not in' return True if value does not exists

numbers=[1,2,3,4]
print(2 in numbers)
print(5 not in numbers)

#string
text="python"

print("py"in text)

#bitwise operator in python
#bitwise operator work on binary numbers(bits)
#& bitwise AND
#^ bitwise XOR

a=5
b=3
print(a&b)
print(a^b)

#python control flow
#conditional statements allow a program to make decisions based on conditions

#if,elif,else
#if statement
#the if statement allow a program to check whether condition true
#syntax
#if condition:
age=18
if age >= 18:
   print("you are eligible to vote")

#if .... else statement
   """
if condition:

else:

"""
   number=7
   if number% 2 ==0:
       print("Even")
   else:
       print("Odd")
#if...elif...else statement
"""
if condition:

elif condition:

elif condition:

else:

"""
marks=70
if marks >=90:
   print("Grade 'A'")
elif marks >=75:
   print("Grade 'B'")
elif marks>=50:
   print("Grade 'C'")
else:
   print("Fail")
                 
