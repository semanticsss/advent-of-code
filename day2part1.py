f=open('reports.txt', 'r')
data=[]
for line in f:
    row = line.split()
    for x in range(len(row)):
        row[x] = int(row[x])
    data.append(row)

counter = 0

for x in data:
    increasing = False
    decreasing = False
    unsafe = False
    # print('test')
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



        


    
# for report in data:
#     print(unsafe)
#     increasing = False
#     decreasing = False
#     print(report)
#     for x in range(len(report) - 1):
#         if(report[x] < report[x+1]):
#             increasing = True
#         if(report[x] > report[x+1]):
#             decreasing = True
#         if((increasing and decreasing) or (report[x] == report[x+1]) or (abs(report[x] - report[x+1]) > 3)):
#             unsafe += 1
#             print(unsafe)
#             break


# print(unsafe)