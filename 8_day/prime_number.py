def prime_number(n):
    div = 2
    is_prime = True
    while div < n:
        if n % div == 0:
            is_prime = False
        div += 1
    if is_prime == True:
        print("{} is a prime number".format(n))
    else:
        print("{} is a not prime number".format(n))
        
num = input("Type a number and check if it's a prime number  ")
num = int(num)
prime_number(n=num)