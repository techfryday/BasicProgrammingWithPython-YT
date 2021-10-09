# num=int(input("Enter a number"))


for num in range(1,101):
    count=0
    for n in range(1,num+1):
        if num%n==0:
            count+=1

    if count==2:
        print(str(num)+" is prime number")