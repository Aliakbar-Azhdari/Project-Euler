def sum_of_primes ():
    temp = 0
    for i in range (2 , 2000000):
        for j in range (2 , int(i ** 0.5)+1):
            if i % j == 0 :
                break
        else:
            temp += i
    return temp

print(sum_of_primes())


        