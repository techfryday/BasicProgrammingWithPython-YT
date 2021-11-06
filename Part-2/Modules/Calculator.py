pi = 3.14

def add(n1, n2):
    return n1+n2

def sub(n1, n2):
    return n1-n2

def mult(n1, n2):
    return n1*n2

def divi(n1, n2):
    return n1/n2

if __name__=="__main__":
    import sys
    num1 = int(sys.argv[2])
    num2 = int(sys.argv[3])
    if sys.argv[1]=="addition":
        print(add(num1, num2))
    elif sys.argv[1]=="subtraction":
        print(sub(num1, num2))
    elif sys.argv[1]=="multiplication":
        print(mult(num1, num2))
    elif sys.argv[1]=="division":
        print(divi(num1, num2))
    else:
        print("INVAID_OPERATION")
