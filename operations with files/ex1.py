numbers = []
with open ("ex1.txt", 'r') as file:
    for line in file:
        number = line.strip().split()
        for n in number:
            numbers.append(int(n))

print(numbers)

