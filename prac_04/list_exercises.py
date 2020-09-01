numbers = []
for i in range(5):
    user_number = int(input("Number: "))
    numbers.append(user_number)

print(numbers[0])
print(numbers[-1])
print(min(numbers))
print(max(numbers))
print(sum(numbers) / len(numbers))

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
name = input("What is your username? ")
if name in usernames:
    print("Access granted")
else:
    print("Access Denied")

