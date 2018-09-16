# Valid arrays
# a = [121, 144, 19, 161, 19, 144, 19, 11]
# b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]

# comp(a, b) returns true because in b 121 is the square of 11,
# 14641 is the square of 121, 20736 the square of 144,
# 361 the square of 19, 25921 the square of 161, and so on.
# It gets obvious if we write b's elements in terms of squares:

# a = [121, 144, 19, 161, 19, 144, 19, 11]
# b = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]

def comp(array1, array2):
    try:
        return sorted([i ** 2 for i in array1]) == sorted(array2)
    except:
        return False