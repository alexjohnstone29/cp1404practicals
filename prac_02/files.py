outfile = open("name.txt", "w")
user_name = input("What is your name? ")
outfile.write(user_name)
outfile.close()

infile = open("name.txt", "r")
your_name = infile.readline()
print("Your name is", your_name)
infile.close()

infile = open("numbers.txt", "r")
first_number = infile.readline()
first_number_int = int(first_number)
second_number = infile.readline()
second_number_int = int(second_number)
total = first_number_int + second_number_int
print(total)
