
phone_nums = {
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    0: "Zero"
}

phone = input("Phone: ")
phone_number_in_words = ""
for digit in phone:
    phone_number_in_words += phone_nums[int(digit)]
    phone_number_in_words += " "
print(phone_number_in_words)