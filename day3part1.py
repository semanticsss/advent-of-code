f = open('day3set.txt', 'r')
data = f.read()

counter = 0

def search_for_valid_strings(data):
    while len(data) > 1:
        counter = 0
        x = data.find("mul(") # x is the position of the mul( string bullshit
        data = data[x:]
        print(data)
        comma_index = data.index(",")
        paren_index = data.index(")")
        if data[(x+5):comma_index].isdigit() and data[(comma_index + 1):paren_index].isdigit():
            number1 = int(data[(x+5):comma_index])
            number2 = int(data[(comma_index + 1):paren_index])
            k = number1 * number2
            data = data[:paren_index]
            counter += k
    print(counter)

search_for_valid_strings(data)



