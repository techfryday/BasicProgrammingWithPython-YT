data = input("Enter Something: ")

# if num>0:
#     print("Number is positive")
# elif num<0:
#     print("Number is negative")
# else:
#     print("Number is zero")

# if num%2==0 and num>0:
#     print("Number is positive and even")
# elif num%2==0 and num<0:
#     print("Number is negative and even")
# elif num%2!=0 and num>0:
#     print("Number is positive and odd")
# elif num%2!=0 and num<0:
#     print("Number is negative and odd")
# else:
#     print("The number is zero")

if ("@" in data) and ((".com" in data) or (".in" in data)):
    print("Basic Validation Successful")
    if len(data) > 10:
        print("Valid Email")
    else:
        print("Not Sufficient Characters")
else:
    print("Invalid Email")




