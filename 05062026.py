#text file handling in python
'''
what is file handling?
text file handling in pyhton is the process of creating,opening ,reading,writing,appending,
managing text files 
using python programs

it allows data to be stored permanently in files instead of temporary memory
'''
#defination of modes of opening file in python

'''
file modes are the different ways use to open a file and write data into a file in python
for performing operation like reading,writing,appending or binary handling
'''

#defination of I/O operation with files in python
'''
I/O operation in python are used to read data from a file and write a data into a file
input operation --> reading data from a file
output operation--> writing data into a file
'''

#1.read mode

file=open("DUMMY\DUMMY.txt","r")
content=file.read()
print(content)
file.close()

#2.write mode

file=open("DUMMY\DUMMY.txt","w")
file.write("\ninput operation --> reading data from a file")
file.close()

#3.append mode

file=open("DUMMY\DUMMY.txt","a")
file.write("\noutput operation--> writing data into a file")
file.close()

#4.create mode
'''
file=open("DUMMY\\newdummy.txt","x")
file.close()
'''

file=open("DUMMY\DUMMY.txt","r")
print(file.readlines(1))   #read first line
file.close()

file=open("DUMMY\DUMMY.txt","r")
print(file.readlines()) #read all lines
file.close()

file=open("DUMMY\DUMMY.txt","r")
print(file.readline())
file.close()

#write text into file
file=open("DUMMY\\newdummy.txt","w")
file.write("it allows data to be stored permanently in files instead of temporary memory")
file.close()

#write lines
file=open("DUMMY\\newdummy.txt","w")
lines=[
    "hello!everyone\n",
    "I am learning python\n",
    "Increasing my knowledge\n"
    ]
file.writelines(lines)
file.close()

#using with statement
#best method for file handling because file closes automatically

with open("DUMMY\\newdummy.txt","r") as file:
    content=file.read()
    print(content)

#binary file handling
#use for images audio videos etc...

file=open("DUMMY\\newdummy.txt","rb")
content=file.read()
print(content)
file.close()


#read and write binary file

file=open("DUMMY\\newdummy.txt","r+")
print(file.read)
file.write("text file handling in python")
file.close()

#create and read file
'''
file=open("DUMMY\\files.txt","x")
file.close()
'''
file=open("DUMMY\\files.txt","w")
file.write("hello")
file.close()

