data = input("Enter Something: ")

while True:
    if ("@" in data) and ((".com" in data) or (".in" in data)):
        print("Basic Validation Successful")
        if len(data) > 10:
            print("Valid Email")
            break
        else:
            print("Not Sufficient Characters")
            data = input("Enter another string: ")
    else:
        print("Enter one more time please:")
        data = input("Enter Something: ")

