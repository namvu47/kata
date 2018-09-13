# Pick the position of number that differ from the others

''' def iqTest(numbers):
    array = [int(i) % 2 for i in numbers.split()]
    if array.count (1) > array.count(0):
        m = 0
    else:
        m = 1
    return array.index(m) + 1

print(iqTest('1 2 2'))
print(iqTest('2 4 7 8 10')) '''


def iq_test(numbers):
    number = numbers.split()
    rel = [x for x in number if int(x) % 2 == 0]
    if len(rel) == 1:
        return number.index(rel[0]) + 1
    else:
        return number.index((''.join([x for x in number if x not in rel]))) + 1

print(iq_test('1 2 2'))
print(iq_test('2 4 7 8 10'))
print(iq_test('1 3 2 5 7'))



