#python data types
#frozen sets they are immutable and new elements cannot added after its defined
fs=frozenset("hellopython")
print(fs)
cities=frozenset(["surat","ahemdabad","vadodara","pune","mumbai"])
print(cities)

#number data types
#number have four type in python : int,float,complex,long

int_num=10
float_num=10.5
#complex_num=3.15jk
#long_num=123456789l
print(int_num)
print(float_num)

#list data types in python
#a list contain items seperated by commas and enclosed by square[] brackets 0000list is similar to arrays in "C programming"

# but difference is that all the items belonging to a list can be of different data types

list=[123,"abcd",10.2,"D"]
print(list)
list1=["hello","world"]
print(list[2:4])
print(list1*2)
print(list+list1)
#dictionary data types
#dict consists of key value pairs it is enclosed by curly braces{} and values can be using square brackest[]

dict={'name':"red",'age':10}
print(dict)
print(dict["name"])#return the value of 'name' key
print(dict.values())#return all value of dict
print(dict.keys())#return all keys of dict

#tuple data types
#lists are enclosed in square brakets [] and tuple are closed in parentheses() and cannot be update tuple are immutable
tuple=(123,"hello",True)
tuple1=("world")
print(tuple)
print(tuple[0])
t2=(1,2,3,4)
t3=(5,6,7,8)
print(t2+t3)
print(type(t2))
print(type(t3))
#note that string cannot be added in tuple when you try to concatenate a tuple which contains int string that will not concatenate
#print(tuple+tuple1)
#TypeError: can only concatenate tuple (not "str") to tuple
t4=(1,1.1,2.3,4.5)
t5=(7.5,5.2,6.3,4.5)
print(t4+t5)



       
