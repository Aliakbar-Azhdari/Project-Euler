def Is_prime ():
    listt = []
    for i in range (2,21):
        for j in range ( 2 , i):
            if i % j == 0 :
                break
        else:
            listt.append(i)
    return listt

def Lcm (listt):
    count = 1
    for item in listt:
        while item **2 < 20 :
            item = item ** 2
        count *= item
    return count

primes = Is_prime()
result = Lcm(primes)
print(result)

