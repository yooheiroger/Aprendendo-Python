def is_prime_number(number):
    if number <= 2 :
        return True
    for i in range(2, number):
        print(i)
        if number % i == 0:
            return False
    return True
num = is_prime_number(13)
print(num)