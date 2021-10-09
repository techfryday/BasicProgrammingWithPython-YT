def validateEmail(emailToValidate):
    while True:
        if ("@" in emailToValidate) and ((".com" in emailToValidate) or (".in" in emailToValidate)):
            print("Basic Validation Successful")
            if len(emailToValidate) > 10:
                print("Valid Email")
                break
            else:
                print("Not Sufficient Characters")
                emailToValidate = input("Enter another string: ")
        else:
            print("Enter one more time please:")
            emailToValidate = input("Enter Something: ")

email1 = input("Enter first email")
validateEmail(email1)

email2 = input("Enter second email")
validateEmail(email2)
