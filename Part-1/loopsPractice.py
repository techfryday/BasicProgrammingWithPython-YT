# count=1
# while count<=5:
#     print(count)
#     count+=1

# for count in range(1, 11, 2):
#     print(count)

data = input("Enter some string: ")
count=0
for character in data:
    if character=="a" or character=="e" or character=="i" or character=="o" or character=="u":
        count+=1

print("Total Vowels in "+data+" are "+str(count))

