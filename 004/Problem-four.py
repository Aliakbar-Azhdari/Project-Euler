def is_palindrome():
    container = 0
    for i in range (999,99,-1):
        for j in range (i,99,-1):
            number = i * j
            if number <= container :
                break
            x = str(number)
            if x == x[::-1] and number > container:
                container = number
    return container
print(is_palindrome())

