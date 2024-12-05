f = open('day3set.txt', 'r')
data = f.read()


# define something has mul(x,y)
# look through the string to find things in the form mul(x,y)
# return the index of that to get the string out of it
# parse the x and the y out, probably checking to see if they are integers

x = data.find("mul")

print(x)