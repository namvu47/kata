def maskify (cc):
    print('#' * (len(cc) - 4) + cc[-4:])

for i in range(0,3):
    cc = str(input('Enter your credit card number: \n'))
    maskify(cc)


