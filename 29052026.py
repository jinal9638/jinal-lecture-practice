#function in python
#functions, recursion,lambda function,global keyword and multiple return value
#what is function?
#functions are reusable blocks of code use for specific task
#udf function
def prints():
    print("Welcome Students!")

prints()

def multi(a,b):
    print("Multiplication:",a+b)

multi(4,5)

#recursion function
#a function calling itself

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))

def total(n):
    if n==0:
        return 0
    return n+total(n-1)

print(total(5))

# lambda arguments : expression

square=lambda x:x*x

print(square(5))

add=lambda a,b :a+b

print(add(10,20))

numbers=[1,2,3,4,5]

result=list(map(lambda x:x*2,numbers))

print(result)

numbers=[1,2,3,4,5,6,7,8,9]

odd=list(filter(lambda x:x%2 != 0,numbers))

print(odd)

# Global Keyword
# Variables created outside fucntion are called Global variables
# To modify global variable inside function use 'global'

x=10

def show():
    print(x)

show()

count=0

def increment():
    global count
    count+=1

increment()
increment()
print(count)


def calculation(a,b):
    return a+b,a-b

result=calculation(10,5)
print(result)

def student():
    name='ALICE'
    marks=90
    return name,marks

n,m=student()

print(n)
print(m)

numbers = [1 , 2 , 3 , 4 , 5]

print(f"Length:{len(numbers)} \nMAximum:{max(numbers)} \nMinimum:{min(numbers)}")

def greet(name):
    return "Hello! "+name
print(greet("Students"))

# *args collects multiple value into a tuple

def add_number(*args):
    total=0
    for num in args:
        total+=num
    return total

print(add_number(1,2,3,4,5))

def student_info(**kwargs):
    for key, value in kwargs.items():
        print(key,":",value)

student_info(name="Rahul",age=20,course="Python")

# **kwargs stored data in dictionary

def multiply(a,b):
    """This function return the multiplication of two numbers"""
    return a*b

print(multiply(4,5))
print(multiply.__doc__)#here two times underscore use

#TNRN -> Take no arguments , return no value
'''
no parameter
no return
'''
def greet():
    print("Hello,Python Students")

greet()

#TSRN -> Take some Arguments , Return no value
'''
accept parameter
does not return result
'''
def add(a,b):
    print("Addition:",a+b)

add(10,20)

#TNRS -> Take no Arguments , Return Some value
'''
no parameter
return value using return
'''

def message():
    return 'Hello Students'

print(message())


#TSRS -> Take some Arguments , Return Some Value

'''
Accept parameter
return output
'''

def multiply(a,b):
    return a*b

result=multiply(4,7)

print(result)


