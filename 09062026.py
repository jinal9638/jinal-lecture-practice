#raise keyword
'''
age=-5
if age<=0:
    raise ValueError("Age cannot be negative")
'''

#assert

num=10
assert num>0,"Number must be positive"
print("Valid Number")

#custom exception with try...except

class InsufficientBalanceError(Exception):
    pass

balance=1000
withdrawal=1500

try:
    if withdrawal>balance:
        raise InsufficientBalanceError("Not enough balance")
    print("Withdrawal Successfully")

except InsufficientBalanceError as e:
        print("Error:",e)

#check even number using type error and value error

def check_even():
    num=int(input("Enter an integer:"))

    if not isinstance(num,int):
        raise TypeError("Input must be an Integer")
    if num%2!=0:
        raise ValueError("Number is odd")
    print("Number is even")


try:
    check_even()

except ValueError:
    print("Entered value must be contains only number")

except Exception as e:
    print("Error:",e)

#Student grade validation

class InvalidGradeError(Exception):
    pass
try:
    grade=int(input("Enter a grade:"))
    assert grade !=" ","Grade input cannot be empty."

    if grade<0 or grade>100:
        raise ValueError("Grade must be between 0 to 100.")

    if grade<40:
        raise InvalidGradeError("Student has failed.")

    print("Student Passed.")

except AssertionError as e:
    print("Assertion Error:",e)

except ValueError as e:
    print("ValueError:",e)

except InvalidGradeError as e:
    print("Invalid Grade Error:",e)

#Temperature conversion validation

class HighTemperatureError(Exception):
    pass

try:
    temp=float(input("Enter temperature in celsius:"))

    if not isinstance(temp,(int,float)):
        raise TypeError("Temperature must be number.")
    assert -273<=temp<=10000,"Temperature out of valid range."

    if temp>1000:
        raise HighTemperatureError("Temperature exceed 1000 C")

except TypeError as e:
    print("TypeError:",e)

except AssertionError as e:
    print("Assertion Error:",e)

except HighTemperatureError as e:
    print("High Temperature Error:",e)
