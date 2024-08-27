def num(*digits):
    sum = 0
    for d in digits:
        sum += d
    print(sum)

num(1, 2, 3, 4)

def sum(**kwargs):
    sum = 0
    for num in kwargs:
        sum += kwargs.get(num)
    return sum, kwargs

print(sum(a=1, b=2, c=3, d=4))