#examples

x=3
y=1

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x**y)
print(x//y)

#comparison

print(x==y)
print(x!=y)
print(x<y)
print(x>y)
print(x<=y)
print(x>=y)

#assignment operators
x+=y
print(x)
x-=y
print(x)
x*=y
print(x)
x/=y
print(x)
x//=y
print(x)
x**=y
print(x)

price=1000
discount=100
price-=discount
#after discount
print(price)

#check if a number is even or odd
num=int(input("enter a no:"))
if num%2==0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is a odd number.")

#find the minimum of two numbers

num1=int(input("enter 1st number:"))
num2=int(input("enter 2nd number:"))
if num1<num2:
    print(f"The minimum number is {num1}")
else:
   print(f"The maximum number is {num1}")

#find the largest of three number
num1=int(input("enter 1st number:"))
num2=int(input("enter 2nd number:"))
num3=int(input("enter 3rd number:"))
if num1>=num2 and num1>=num3:
    print(f"The largest number is {num1}")
elif num2>num1 and num2>num3:
    print(f"The largest number is {num2}")
else:
    print(f"The largest number is {num3}")


        

