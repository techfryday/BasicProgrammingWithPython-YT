# def welcome():
#     print("This is welcome function")

# welcome()

# def calculate(num1, num2, op):
#     if op=="+":
#         print(num1+num2)
#     elif op=="-":
#         print(num1-num2)
#     elif op=="*":
#         print(num1*num2)
#     elif op=="/":
#         print(num1/num2)
#     else:
#         print(num1%num2)

# n1 = int(input("Enter a number: "))
# n2 = int(input("Enter another number: "))
# operation = input('''
# Press + to perform addition
# Press - to perform subtraction
# Press * to perform multiplication
# Press / to perform division
# Press % to perform mod
# Enter your choice: 
# ''')
# calculate(n1,n2,operation)

# def primeOrNot(num):
#     count=0
#     for n in range(1,num+1):
#         if num%n==0:
#             count+=1

#     if count==2:
#         return True
#     else:
#         return False

# if primeOrNot(4):
#     print("Cool! You can build an encryption Key.")
# else:
#     print("Prime number is reuired to build an encryption Key.")

# def countFriends(*params):
#     return len(params)

# print(countFriends("Tony Stark", "Steve Rogers", "Thor", "Dr Banner"))

# def calucate(*params):
#     if params[2]=="+":
#         return params[0]+params[1]
#     elif params[2]=="-":
#         return params[0]-params[1]
#     elif params[2]=="*":
#         return params[0]*params[1]
#     elif params[2]=="/":
#         return params[0]/params[1]
#     else:
#         return params[0]%params[1]

# print(calucate(12,23,"%"))

def calculate(**dt):
    print(dt)
    if dt['op']=="+":
        print(dt['num1']+dt['num2'])
    elif dt['op']=="-":
        print(dt['num1']-dt['num2'])
    elif dt['op']=="*":
        print(dt['num1']*dt['num2'])
    elif dt['op']=="/":
        print(dt['num1']/dt['num2'])
    else:
        print(dt['num1']%dt['num2'])

n1 = int(input("Enter a number: "))
n2 = int(input("Enter another number: "))
operation = input('''
Press + to perform addition
Press - to perform subtraction
Press * to perform multiplication
Press / to perform division
Press % to perform mod
Enter your choice: 
''')
calculate(op=operation, num2=n2, num1=n1)
