f=open('reports.txt', 'r')
data=[]
for line in f:
    row = line.split()
    for x in range(len(row)):
        row[x] = int(row[x])
    data.append(row)
f.close()

counter = 0

for x in data:
    increasing = False
    decreasing = False
    unsafe = False
    for y in range(len(x) - 1):
        if abs(x[y]-x[y+1]) > 3:
            unsafe = True
            break

        if x[y] < x[y+1]:
            increasing = True
        elif x[y] > x[y+1]:
            decreasing = True
        elif x[y] == x[y+1]:
            unsafe = True
            break
        
    if unsafe or (increasing and decreasing):
        counter += 1

print(1000-counter)

# bro im so slow i put the unsafe checked inside of the fucking y loop not the x loop

