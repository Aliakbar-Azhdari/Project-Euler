def find_triplet ():
    for a in range(1000):
        for b in range(1000):
            for c in range(1000):
                if a < b < c :
                    if (a**2 + b**2) ** 0.5 == c :
                        if a + b + c == 1000 :
                            return a , b , c
                    
print(find_triplet())


