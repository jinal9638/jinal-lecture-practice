#exception handling in python
'''
AN EXCEPTION IS AN ERROR THAT OCCURS DURING PROGRAM EXECUTING
IF AN EXCEPTION IS NOT HANDLED THAT PROGRAM STOP IMMEDIATELY
'''

#PRINT(10/0)
#TO AVOID PROGRAM CRASHES PYTHON PROVIDES EXCEPTION HANDLING THING

try:
    num=int(input("Enter no.:"))
    print(10/num)

except ZeroDivisionError:
    print("Cannnot divide by Zero.")
except ValueError:
    print("Invalid Input")

#try-->contains risky code
#except--> runs if error occurs
#else-->block executes only when no exception occurs

try:
    num=int(input("Enter no.:"))
    result=10/num

except ZeroDivisionError:
    print("Cannnot divide by Zero.")
except ValueError:
    print("Invalid Input")
else:
    print("Result:",result*10)


#try...except...finally

try:
    file=open("DUMMY\DUMMY.txt","r")
    print(file.read())

except FileNotFoundError:
    print("File Not Found")

finally:
    print("Program Finished.")


#try....except...else...finally

try:
    num=int(input("Enter no.:"))
    result=10/num

except ZeroDivisionError:
    print("Cannnot divide by Zero.")
except ValueError:
    print("Invalid Input")
else:
    print("Result:",result)
finally:
    print("Program finsihed.")

#important exception types in python

'''
1.ZeroDivisionError
2.ValueError
3.TypeError
4.IndexError
5.KeyError
6.FileNotFoundError
'''

try:
    atm_pin=int(input("Enter your ATM PIN:"))
    
except ValueError:
    print("PIN must contain numbers only")
else:
    print("PIN accepted")

#divide Two numbers using try....except

try:
    num1=int(input("Enter 1st no.:"))
    num2=int(input("Enter 2nd no.:"))
    print("Result:",num1/num2)

except ZeroDivisionError:
    print("Cannnot divide by Zero.")

except ValueError:
    print("Invalid Input")

#handle list index error

try:
    numbers=[10,20,30,40,50]
    index=int(input("Enter Index no.:"))
    print("ELEMENT:",numbers[index])

except IndexError:
    print("Index Does Not Exist.")

except ValueError:
    print("Invalid Input")


#read file using try....except...else

try:
    filename=input("Enter filename:")
    file=open(filename,"r")

except FileNotFoundError:
    print("File Not Found")

except ValueError:
    print("Invalid Input")

else:
    print("file content")
    print(file.read())

    file.close()

#handling string index error using else

try:
    text="Python"
    index=int(input("Enter index no.:"))
    result=text[index]

except IndexError:
    print("Index does not exist")

except ValueError:
    print("Invalid Input")

else:
    print("Character:",result)
