# sum of digits of integer N until sum < 10

def sumDigits(n):
    _sum = 0
    if n == 0:
        _sum = 0
    elif n %9 == 0:
        _sum = 9
    else:
        _sum = n % 9
    return _sum



    