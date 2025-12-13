x = 600851475143
def xx ():
    listt = []
    for i in range (2,int(x**0.5)+1):
        if x % i == 0 :
            for j in range (2,int(i**0.5)+1):
                if i % j == 0 :
                    break
            else:
                listt.append(i)
    listt.sort()
    return listt[-1]
    
          
print(xx())

