f=open('reports.txt', 'r')
data=[]
for line in f:
    row = line.split()
    for x in range(len(row)):
        row[x] = int(row[x])
    data.append(row)

f.close()


counter = 0


def test_unsafe(x): # returns a boolean, if true then unsafe, if false then safe
    increasing = False
    decreasing = False
    for y in range(len(x) - 1):
        if abs(x[y]-x[y+1]) > 3:
            return True
            
        if x[y] < x[y+1]:
            increasing = True
        elif x[y] > x[y+1]:
            decreasing = True
        elif x[y] == x[y+1]:
            return True
    if (increasing and decreasing):
        return True
    else:
        return False
    
            
def safe_with_damping(list):
    if not test_unsafe(list):
        return True
    
    for i in range(len(list)):
        temp = list[:i] + list[i+1:]
        if not test_unsafe(temp):
            return True
        
    return False

for x in data:

    if safe_with_damping(x):
        counter += 1

print(counter)

# bro im so slow i put the unsafe checked inside of the fucking y loop not the x loop

