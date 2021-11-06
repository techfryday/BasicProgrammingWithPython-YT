# The problem with concatenation (Confusing syntaxt)
agelimit = 18
city = "mumbai"
salarylimit = 50000
# print("SELECT * FROM table_name WHERE age>"+str(agelimit)+" AND city='"+city+"' AND salary<"+str(salarylimit))
print(f"SELECT * FROM table_name WHERE age>{agelimit} AND city='{city}' AND salary<{salarylimit}")

data = {
 "full_name":"Sagar"   ,
 "email":"sagar@gmail.com",
 "phone":"1231231232"
}

print(f"INSERT INTO user (full_name, email, phone) VALUES('{data['full_name']}', '{data['email']}', '{data['phone']}')")

""" name = "sagar"
age = 25
 """
""" # With % sign
print("My Name: %s \nAge: %d" %(name, age)) """

""" # With format() function
print("Welcome, {0} Please confirm your details\nMy Name: {0}  \nAge: {1} ".format(name, age)) """

""" # With f-string
print(f"Welcome, {name} Please confirm your details\nMy Name: {name}  \nAge: {age} ") """

