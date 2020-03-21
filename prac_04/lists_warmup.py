numbers = [3, 1, 4, 1, 5, 9, 2]

# numbers[0] will return 3
# numbers[-1] will return error  -- actually returned 2
# numbers[3] will return 1
# numbers[:-1] will return 2 -- [3, 1, 4, 1, 5, 9]
# numbers[3:4] will return [1, 5] -- [1]
# 5 in numbers will return 1 -- True
# 7 in numbers will return False
# "3" in numbers will return true -- false
# numbers + [6, 5, 3] will return [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

numbers[0] = "ten"
print(numbers)

numbers[-1] = 1
print(numbers)

element = slice(2, 7, 1)
print(numbers[element])

print(9 in numbers)
