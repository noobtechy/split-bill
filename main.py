a = int(input("Total money used in event: "))
names = input("Enter the names of the people separated by spaces: ").split()
n = len(names)
avg = a / n
for name in names:
    print(name, "-", avg)
