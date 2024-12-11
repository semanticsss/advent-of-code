import regex as re

with open('day3set.txt', 'r') as f:
    data = f.read()

f.close()

counter = 0

mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

do = r"(do\(\))"
dont = r"(don't\(\))"

big_pattern = f"{mul_pattern}|{do}|{dont}"

instructions = re.findall(big_pattern, data)
do_or_dont = True


for instruction in instructions:
    print(instruction)
    if instruction[0] and instruction[1]:
        if do_or_dont:
            counter = counter + (int(instruction[0]) * int(instruction[1]))
    elif re.match(do, instruction[2]):
            print('made it true')
            do_or_dont = True
    elif re.match(dont, instruction[3]):
            print('made it false')
            do_or_dont = False

print(counter)


        # 
        # search for the next mul