numbers = []

while True:
    inp = input("Enter your input: ")
    if inp=="end":
        break
    else:
        numbers.append(int(inp))

print(numbers)
for j in range(0, len(numbers)):
    if numbers[j]%2==0:
        print(numbers[j])





