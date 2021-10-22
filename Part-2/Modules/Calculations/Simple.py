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
    op = sys.argv[1]
    n1 = int(sys.argv[2])    
    n2 = int(sys.argv[3])
    if op=='add':
        print(add(n1, n2))
    elif op=='sub':
        print(sub(n1, n2))
    elif op=='mult':
        print(mult(n1, n2))
    elif op=='divi':
        print(divi(n1, n2))
    else:
        print("Invalid Operation Type")
    
