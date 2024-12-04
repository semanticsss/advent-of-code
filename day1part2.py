f=open('lists.txt',"r")
lines=f.readlines()
values1=[]
values2=[]
similarity_score = 0
for x in lines:
    values1.append(int(x.split('   ')[1]))
    values2.append(int(x.split('   ')[0]))
f.close()

values1.sort()
values2.sort()


for x in range(len(values1)):
    instances = 0
    for y in range (len(values1)):
        if values1[x] == values2[y]:
            instances += 1
    similarity_score += values1[x]*instances

print(similarity_score)