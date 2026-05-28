#CRUD OPERATION IN PYTHON
#CREATE
#READ
#UPDATE
#DELETE

#EMPTY LIST

users=[]

#create

user1={
    'id':1,
    'name':'Alice',
    'email':'alice@gmail.com'
}

user2={
    'id':2,
    'name':'zeel',
    'email':'zeel@gmail.com'
}

user3={
    'id':3,
    'name':'karan',
    'email':'karan@gmail.com'
}

#add users

users.append(user1)
users.append(user2)
users.append(user3)

print("User added Successfully!")

#read
print("\n All users:")

for user in users:
    print(user)

search_id=1

print("\n Searching User :")

for user in users:
    if user['id']==search_id:
        print("User Found:",user)

#update

print("\n Updating User Email...")

for user in users:
    if user['id'] == 2:
        user['email'] = 'zeel@example.com'

print("User Updated!")

#DELETE

print("\n Deleting user...")

for user in users:
    if user['id'] ==1:
        users.remove(user)
        break
print("User Deleted!")

#count users

print("\n Total Users:",len(users))

#check email exists
check_email = 'zeel@example.com'

found = False
for user in users:
    if user['email'] == check_email:
        found=True
if found:
    print("Email Exists")
else:
    print("Email not found")

#sort by user name

sorted_users=sorted(users,key=lambda x:x['id'])
print("\n Sorted Users:")

for user in sorted_users:
    print(user)

#final user list

print("\n ==================== Final Users =====================")

for user in users:
    print(f"""
ID : {user['id']}
Name : {user['name']}
Email:{user['email']}
""")

#type casting constructor

a=[1,2,3,4]
print(tuple(a))
print(set(a))

#del keyword

x=[1,2,3,4]

del x[1]
print(x)

person = {'name':'vishwa','age':30}

del person['age']

print(person)
#del x
#print(x) #all value deleted return nothing

