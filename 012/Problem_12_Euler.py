n = 1

while True :
    
   temp = n * (n+1) / 2
   count = 0
   for j in range (1 , int(temp ** 0.5) + 1):
       
       if temp % j == 0 :
           count += 1
           if j != temp // j :
               count += 1
               
   if count > 500 :
        print(temp)
        break
   
   n += 1
