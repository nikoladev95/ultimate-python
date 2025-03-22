
numbers = [5, 2, 7, 5, 8, 2, 11, 7, 46, 7, 5]
new_array = []

for number in numbers:
    if number not in new_array:
        new_array.append(number)
print(new_array)
