#what is array
#an array is a data structure to store multiple value in a single variable
#1.find second largest element

arr=[12,45,79,89,67]
arr.sort()
print(arr)
print("Second Largest:",arr[-2])

#remove duplicate elements

arr = [10 , 20 , 30 , 10 , 30 , 40 , 20]

unique=[]

for i in arr:
    if i not in unique:
        unique.append(i)

print("Array:", unique)

#3.frequency of each element

arr = [10 , 20 , 30 , 10 , 30 , 40 , 10]

for i in set(arr):
    print(i,"appears",arr.count(i),"times")

#find missing number

arr=[1,2,3,5,6]
n=6
expected=n*(n+1)//2
print(expected)
actual=sum(arr)
print(actual)


print("Missing number:",expected-actual)

#merge and sort two array

arr1=[10,20,30]
arr2=[20,40,60]

merged=arr1+arr2
print(merged)

#kadane's algorithm

arr = [-2 , 1 , -3 , 4 , -1 , 2 , 1 , -5 , 4 ]

current=maximum=arr[0]

for i in arr[1:]:
    current=max(i,current+i)
    maximum=max(maximum,current)

print("Maximum sum:",maximum)

#2D array
#addition of two matrix

A=[
  [1,2],
  [3,4]
  ]

B=[
  [5,6],
  [7,8]
  ]

result=[]

for i in range(len(A)):
    row=[]
    for j in range(len(A[0])):
        row.append(A[i][j] + B[i][j])
    result.append(row)

for row in result:
    print(row)

#find largest element in each row:

matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]

for row in matrix:
    print("LARGEST:",max(row))
