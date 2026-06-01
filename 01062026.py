#program with *args with udf function

def filter_args(*args):

    strings=()
    numbers=()

    for item in args:
        if type(item) == str:
            strings += (item, )
        elif type(item) in (int,float):
            numbers += (item, )

    return strings , numbers

result=filter_args("apple",10,"orange",25,3.5,"manan")

print(result)

print("Strings :", result[0])
print("Numbers :",result[1])

# write a program create 1D array with integer element and display using a loop

list_1=[10,20,30,40,50]

for item in list_1:
    print(item)

list_2=[10,45,20,78,89]
total=0

for item in list_2:
    total+=item
    print(total)

print("Array of sum:", sum(list_2))

#write a program to find the length of a 1D array without using built in function

arr=[]

size=int(input("Enter array size:"))

for item in range(size):
    value=int(input(f"a[{item}]="))
    arr.append(value)

count=0

for i in arr:
    count+=1

print("Length of array:",count)
print("arr=",arr)

#write a program to find average of a 1d array without using any built in method

arr=[]

size=int(input("Enter array size:"))

for item in range(size):
    value==int(input(f"a[{item}])="))
    arr.append(value)

sums=0
count=0

for i in arr:
    sums+=i
    count+=1           
average=sums/count

print("Average of array",average)


#write a program to perform addition operation of two 1D arrats and store in another  array

arr1=[]
arr2=[]
arr3=[]

size=int(input("Enter array size:"))

print("Enter arr1 Elements:")
for item in range(size):
    value=int(input(f"a[{item}]="))
    arr1.append(value)

print("Enter arr2 Elements:")
for item in range(size):
    value=int(input(f"a[{item}]="))
    arr2.append(value)

for i in range(size):
    arr3.append(arr1[i]+arr2[i])

print("Array 3:",arr3)


#write a progrma an array of numbers from 1 to 10

arr=[]

for i in range(1,11):
    arr.append(i)

print(arr)

#Take user input for a number and check if it exists in the array

arr=[10,20,30,40,50]

num=int(input("Enter number to search:"))

found=False

for i in range(len(arr)):
    if arr[i] == num:
        print("Found at index:",i)
        found = True
        break
if found == False:
    print("Not found")

#print all even numbers from the array
arr=[]
size=int(input("Enter size of array:"))

for i in range(size):
    value=int(input(f"a[{i}]="))
    arr.append(value)

print("Even number:")

for i in arr:
    if i%2==0:
        print(i)

print("Odd number:")

for i in arr:
    if i%2!=0:
        print(i)


#PRINT THE FIRST AND MIDDLE AND LAST ELEMENT IN ARRAY

arr=[10,20,3,4,5,0,30]

print(f"First ELement:{arr[0]} \nMiddle element:{len(arr)//2} \nLast Element:{arr[-1]}")


#2D array:array inside another array
#It store data in rows,columns
#it look like a table or matrix

arr=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
    ]
print(arr)

#accessing element in 2d array

#arr[row][column]

print(arr[0][1])
print(arr[2][2])

#take input in 2d array

arr=[]

rows=int(input("Enter rows:"))
columns=int(input("Enter columns:"))

for i in range(rows):
    row=[]
    for j in range(columns):
        value=int(input(f"a[{i}][{j}]="))
        row.append(value)
    arr.append(row)

print(arr)

#print 2d array using nested loop

arr=[
    [1,2],
    [3,4]
    ]

for i in arr:
    for j in i:
        print(j,end=" ")
        print()

#sorting collection datatypes

numbers=[1,8,5,2,9,4]

numbers.sort()
print(numbers)

numbers.sort(reverse = True)

print(numbers)

#sorting string list

fruits=["mango","apple","banana","orange"]
fruits.sort()
print(fruits)

