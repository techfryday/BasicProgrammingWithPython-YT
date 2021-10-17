try:
    num = int(inpu("Enter a number: "))
    count=0
    for i in range(1, num+1):
        if num%i==0:
            count += 1
    if count==2:
        print(f"{num} is prime!")
except ValueError as e:
    print("Invalid Input")
except NameError as e:
    print(f"{type(e).__name__}: {str(e)}")
    print("Some exception occured. \nThe issue has been reported. \nPlease try again after some time.")
except Exception as e:
    print(type(e).__name__)
    # print("Some exception occured. \nThe issue has been reported. \nPlease try again after some time.")
