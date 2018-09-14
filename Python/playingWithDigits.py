

def dig_pow(n, p):
    _ln = {}
    _sum = 0
    for i in range (0,len(str(n))):
        _ln[i] = int(str(n)[i])
        _sum += _ln[i] ** (p+i)

    if _sum % n == 0:
        return _sum // n
    else:
        return -1