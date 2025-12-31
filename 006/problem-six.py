def Sum_of_squares ():
    x = 0
    for i in range (1 , 101):
        x += i ** 2
    return x


def Square_of_the_sum ():
    c = 0
    for j in range (1,101):
        c += j
    return c ** 2

number_1 = Square_of_the_sum()
number_2 = Sum_of_squares()

def xx (number_1 , number_2):
    temp = 0
    if number_1 > number_2 :
        temp = number_1 - number_2
    else:
        temp = number_2 - number_1
    return temp

print(xx(number_1 , number_2))
    
    
    
    
