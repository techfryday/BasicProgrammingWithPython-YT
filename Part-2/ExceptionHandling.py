# Exception handling in python

# Defined a log function to log the exception messages into a log file
def log(msg):
    file = open("./Part-2/log", "a")
    file.write(msg+"\n")
    file.close()
    
# Try block starts it's execution ,
# If no error then except block Won't get executed.
try:
    for i in range(1, 11):
        if i%2==0:
            prins(i)
# If any error occurs in try block 
# then code written inside except block will get executed
except Exception as e:
    try:
        log(str(e))
        # raise NameError(str(e))
        print(str(e))
    except FileNotFoundError as e:
        raise FileNotFoundError("File is not WRITABLE")     
else:
    print("Nothing went wrong")
# Statements writte inside finally block will execute in any condition
finally:
    print("END")
    
print("**************Last Line***************")