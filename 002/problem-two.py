listt = [1 , 2]
x = 0
c = 0
y = 1
while listt[-1] < 4000000 :
    z = listt[x] + listt[y]
    x += 1
    y += 1
    listt.append(z)
for i in listt :
    if i % 2 == 0:
        c += i
print(c)
    
    
    
    
