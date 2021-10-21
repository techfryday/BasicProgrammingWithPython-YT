name = "Sagar"
age = 25

# Tranditional way of concatinating
print("Welcone, "+name+"\nPlease review the details you have provided\nName: "+name+"")

# Using % Operator
print("Name: %s " %name)
print("Name: %d " %age)

# Fith format method
print(f'''
Welcome, {0}
Please review the details provided by you
Name: {1}
Age: {2}
'''.format(name, name, age))

name="sagar mahajan"
# String formatting types
print("Right align: {:>20} done".format(name))
print("Left align: {:<20} done".format(name))
print("Center align: {:^20} done".format(name))

# With fstring
print(f'''
Welcome, {name}
Please review the details provided by you
Name: {name}
Age: {age}
''') 


