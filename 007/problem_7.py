def prime_10001():
    
    number = 0
    i = 1

    while number < 10001 :
    
        i += 1
    
        is_prime = True
    
        for j in range (2 , int(i**0.5)+1):
        
            if i % j == 0 :
                is_prime = False
                break
        
        if is_prime :
            number += 1
    return i
print(prime_10001())