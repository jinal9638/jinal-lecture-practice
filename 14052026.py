#python mutable and immutable data types
#In python, every value is stored as an object
#mutable object can be change after creation
#immutable object cannot be change after creation

#concept
"""
1.Memory management
2.variable behaviour
3.function arguments
4.performance
5.debugging
6.Learning objectives
"""

#Everything in python is an object

x=10
name="python"
numbers=[1,2,3,4]

#Each object has value,type,memory,address

#We can check memory location using :id() built in function

x=10
print(id(x))
y=10
print(id(y))

#note that this will generate same reference number

y=12
print(id(y))

#when you write different value you get differ reference number.

#common immutable types

"""
int like 10
float like 10.10  it's means decimal value
complex 2+3j
boolean value True or False
str"Hello"
Frozenset{1,2,3}
bytes b"abcd"
tuple(1,2)
"""

#int
x=10
print("before",id(x))
x=x+1
print("after",id(x))

#string

name="python"
#name[0]="j"
#output you find a error TypeError: 'str' object does not support item assignment

#common mutable types
"""
list[1,2,3]
dict{"a":1}
set{1,2,3}
bytearray bytearray(5)
"""
#mutable list

numbers=[1,2,3,4,5]
print("before",numbers)
print("Before ID",id(numbers))
numbers.append(4)

#append function use for to add a element end of the list

print("after",numbers)
print("After ID",id(numbers))

#note that reference number will not change after you add anything in the list it remain same

#mutable dictionary

Students = {
    "name" : " Rajesh ",
    "age" : 20
    }
Students["age"]=21
print(Students)

#note : name is a key and rajesh is a value in dictionary

#string

a_str="Hello World"
print(a_str)
print(a_str[0]) #output will be 'H' because in python value start from 0
"""
hello world
012345678910
also note that space also count and space get 5th position in this string

"""

#slicing

print(a_str[0:5]) #output will be Hello
print(a_str[6:11]) # output will be World

#when you are using slicing use "[]" this type of square brackets
#also note that if you are using slicing you need end of the part end position you need to add on one position to get end part


#Set data types
# set they are mutable and new element can be added once sets are defined

basket = {'apple','banana','orange','pear','kiwi'}
print(basket)

a=set('abcdefghijk')
print(a)

b=set('ajskslakkkll')
print(b)

#note repeated element will not shown in output you will only get the element single times
#also order not maintain output as you tyoe in input









