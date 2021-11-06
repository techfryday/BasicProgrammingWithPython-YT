def log(msg):
    file = open("./Part-2/error.log")
    file.write(msg)
    file.close()

try:
    num = int(input("Enter a number: "))
    for i in range(1,num+1):
        if i%2==0:
            prin(i)
except NameError as e:
    print("CONTACT DEVELOPER")
except ValueError as e:
    print("INVALID VALUE GIVEN AS INPUT")
except Exception as e:
    try:
        log(str(e))
        print("Some ERORR")
    except Exception as e:
        print("Some Error While logging the error \n Please contact developer with the screenshot")
finally:
    print("END OF THE CODE")

