#break statement

#stop the loop immediately:
for i in range(1,7):
    if i==4:
        break
    print(i)

#continue statement

for i in range(1,7):
    if i==4:
        continue # continue skip statement 
    print(i)

#pass statement

for i in range(1,7):
    if i==4:
        pass   #does nothing null statement
    print(i)

#PATTERN IN PYTHON
#right angled triangle

for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
    print()

#number triangle

for i in range(1,6):
    for j in range(i):
        print(i,end=" ")
    print()

#inverted triangle

for i in range(6,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()

#pyramid pattern

row=5

for i in range(1,row+1):
    for j in range(row-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()

#floyd's triangle

num=1

#pyramid pattern

row=5

for i in range(1,6):
    for j in range(i):
        print(num,end=" ")
        num+=1
    print()

#else with loops
# the else block runs when loop finished normally

for i in range(5):
    print(i)
else:
    print("Loop Finished.")

#break

for i in range(5):
    if i==3:
        break
    print(i)
else:
    print("Loop Finished.")
#else does not run because loop stopped using break

#list and tuple

my_list=[10,20,30,40]
print("Original List:", my_list)
my_list[0]=50
print("Modified List:", my_list)

#tuple in python
"""
my_tuple=(10,20,30)
print("Tuple:", my_tuple)
my_tuple[0]=50
TypeError: 'tuple' object does not support item assignment
"""


    
