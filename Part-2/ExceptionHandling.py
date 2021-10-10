def log(msg):
    file = open("./Part-2/error.log", "a")
    file.write(msg)
    file.close()

try:
    for i in range(1,11):
        if i%2==0:
            prin(i)
except Exception as e:
    try:
        log(str(e))
        print("Some error. Please contact developer.1")
    except Exception as e:
        print("Some error. Please contact developer.2")
finally:
    print("END OF EXECUTION")