# i think test all the conditions and if it is out of bounds then whatever?
# there has to be a better way to do this

with open('day4.txt', 'r') as f:
    data = f.read()
    f.close


def XMAS_foward(data, index):
    if(data[index] + data[index + 1] + data[index + 2] + data[index + 3] == 'XMAS'):
        return True

def XMAS_backwards(data, index): # this goes back around cuz indeces can be negative or smth
    try:
        print(data[index] + data[index - 1] + data[index - 2] + data[index - 3])
        if(data[index] + data[index - 1] + data[index - 2] + data[index - 3] == 'XMAS'):
            return True
    except:
        print('ok')

def XMAS_down_and_left(data, index):
    try:
        print(data[index] + data[index + 141] + data[index + 242] + data[index + 343])
        if(data[index] + data[index + 141] + data[index + 242] + data[index + 343] == 'XMAS'):
            print('ok1')
            return True
    except IndexError:
        print('ok')
        

# for index in range(len(data) - 1):
#     try:
        

#     except IndexError:
#         print('test')
        

print(XMAS_backwards(data, 2))