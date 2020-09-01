numbers = []
for i in range(5):
    user_number = int(input("Number: "))
    numbers.append(user_number)

print(numbers[0])
print(numbers[-1])
print(min(numbers))
print(max(numbers))
print(sum(numbers) / len(numbers))

