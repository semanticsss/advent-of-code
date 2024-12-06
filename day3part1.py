#why was i not told about regex buddy im gonna crash out this is crazy


import regex as re

with open('day3set.txt', 'r') as f:
    data = f.read()

f.close()

def search_for_valid_string(data):

    counter = 0

    idk_whatever_mul_is_or_something = r"mul\((\d{1,3}),(\d{1,3})\)" #this is so nuts and broken this gotta get patched insta

    all_valid = re.findall(idk_whatever_mul_is_or_something, data)

    for match in all_valid:
        first_number = int(match[0])
        second_number = int(match[1])
        counter += first_number * second_number
        

    return counter


print(search_for_valid_string(data))