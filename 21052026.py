#match case statement in python
#works similar to switch case

#simple calculator

num1=10
num2=5

operator="+"

match  operator:
    case "+":
        print("Addition=",num1+num2)
    case "-":
        print("Subtraction=",num1-num2)
    case "*":
        print("Multiplication",num1*num2)
    case "/":
        print("Division=",num1/num2)
    case _:
        print("Invalid operator")

#python loop
#1.while loop

i=1
while i<=5:
    print(i)
    i+=1

#countdown
print("Here countdown begins...")
i=3
while i <=3:
    print(i)
    i-=1
    if i == -1:
        break

#for loop

#print 1 to 5

for i in range (1,6):
    print(i)

#loop with string
name="python"

#loop with list
fruits=["Apple","Banana","Mango","Orange"]
for item in fruits:
    print(item)

#range function

for i in range(5):
    print(i)

for i in range(1,10):
    print(i)

for i in range(0,10,2):
    print(i)

#nested loops

for i in range(1,7):
    for j in range(1,6):
        print(j,end="")
    print()
    
for i in range(1,7):
    for j in range(1,6):
        print("*" *j,end="")
    print()
