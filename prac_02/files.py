# 1.
name_list = open('your_name_here.txt', 'w')
name = str(input("So, what's your name? "))
print("{} ".format(name), file=name_list)
name_list.close()


# 2.
name_list = open('your_name_here.txt', 'r')
for line in name_list:
    print("Hi there {}".format(line))
name_list.close()

# 3.
file = open('numbers.txt', 'r')
x = int(file.readline(4))
y = int(file.readline(4))

total = x + y
print(total)

file.close()

# 4.
file = open('numbers.txt', 'r')
total = 0
for i in file:
    total += int(i)

print(total)
file.close()






