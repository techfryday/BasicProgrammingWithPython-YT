def log(msg):
    file = open("./Part-2/error.log")
    file.write(msg)
    file.close()


try:
    for i in range(1,11):
        if i%2==0:
            prin(i)
except Exception as e:
    try:
        log(str(e))
        print("Some ERORR")
    except Exception as e:
        print("Some Error While logging the error \n Please contact developer with the screenshot")
finally:
    print("END OF THE CODE")