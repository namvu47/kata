# return value of number differs than others

def find_outlier(integers):
    array = [int(i) % 2 for i in integers]
    if array.count (1) > array.count(0):
        m = 0
    else:
        m = 1
    print (integers[array.index(m)])

find_outlier([2, 4, 6, 8, 10, 3])

'''def find_outlier(int):
    odds = [x for x in int if x%2!=0]
    evens= [x for x in int if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]'''
