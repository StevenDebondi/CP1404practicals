# 1. Write code that asks the user for their name, then opens a file called "name.txt" and writes that name to it.

name = input("Name?")
names = open("names.txt", 'w')
print(name, file=names)
names.close()

# 2. Write code that opens "name.txt" and reads the name (as above) then prints,
# "Your name is Bob" (or whatever the name is in the file).

names = open("names.txt", 'r')
print(f'Your name is {name}')
names.close()

# 3. Create a text file called numbers.txt and save it in your prac_02 directory. Put the following three numbers on separate lines in the file and save it:
# 17
# 42
# 400
# Write code that opens "numbers.txt", reads only the first two numbers and adds them together then prints the result, which should be... 59.

numbers = open("numbers.txt", 'r')
lineone = int(numbers.readline())
linetwo = int(numbers.readline())
numbers.close()
print(linetwo + lineone)

# 4. Now write a fourth block of code that prints the total for all lines in numbers.txt or a file with any number of numbers.

numbers = open("numbers.txt", 'r')
total = 0
for line in numbers:
    number = int(line)
    total += number
print(total)
numbers.close()