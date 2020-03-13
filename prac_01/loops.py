"""
Just some lööpy bois asking for input
"""
#Eg
for i in range(1, 21, 2):
    print(i, end=' ')
print()

#a
for j in range(0, 101, 10):
    print(j, end=' ')
print()

#b
for k in range(20, 0, -1):
    print(k, end=' ')
print()

#c
number = int(input("Number of stars: "))
for x in range(1):
    stars = '*'
    number_of_stars = stars * number
    print(number_of_stars, end=' ')
print()

#d
number_d = int(input("Number of Stars: "))
for number_d in range(0, number_d+1):
    stars_d = '*'
    number_of_stars_d = stars_d * number_d
    print(number_of_stars_d, "\n", end=' ')
print()