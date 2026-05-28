#string formatting

name="Alisha"
age=21

print(f"My name is {name} and I am {age} years old.")

#using format
print("My name is {} and I am {} years old.".format(name,age))

#using% formatting

print("My name is %s and I am %d years old."%(name,age))

price=199.456

print(f"Price:{price:.2f}")#output will be 2 decimal value only

# list

my_list=[10,20,30]

print("Original List:", my_list)

my_list[1]=200

print("Modified List:", my_list)

my_list.append(50)

print("After append List:", my_list)

my_list.remove(10)

print("After remove List:", my_list)

#tuple

my_tuple=(10,20,30,40)

print("Tuple:",my_tuple)

#access element

print("First Tuple Element:",my_tuple[0])

#indexing

text="Python"

print("First letter:",text[0])
print("Last letter:",text[-1])

#slicing

print("First 3 letters:", text[0:3])
print("Last 3 letters:",text[3:])
print("Last 3 letters:", text[-3:])

#reverse string

print("Reversed string:",text[::-1])

#using list with slicing and formatting

students=["Dixit","Jinal","Raj","Janvi","Jiya","Rutva"]

print(f"\nOriginal List: , {students}\nFirst three students: {students[:3]}")

for student in students:
    print(f"Welcome,{student}")

print("Length of list:", len(students))
print("Is Jiya present?:","Jiya" in students)

matrix=[
       [1,2,3],
       [4,5,6],
       [7,8,9]
       ]
print(f"Matrix:{matrix} \nMiddle Element:{matrix[1][1]}")

message = "python programming"

print(f"Uppercase:{message.upper()} \nCapitalized:{message.capitalize()} \nReplace:{message.replace("python","AI/ML")} \nSplit:{message.split()}")


numbers=[5,8,2,7,1]
numbers.sort()
print("Sorted List:",numbers)
numbers.reverse()
print("Reversed List:",numbers)
numbers.insert(1,100)
print("After insert:",numbers)

