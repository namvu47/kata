myStr = input("Please type a sentence: \n")
print("Numbers of vowels a, e, i, o, u a relatively:")
print(*map(myStr.lower().count,'aeiou'))

# Reference: 1.1 map, 1.2 packing - unpacking arg# https://docs.python.org/3.3/library/functions.html#map
#-----------------------------------------------------------

# https://www.geeksforgeeks.org/python-map-function/
# map (fun, iter)
# fun: function to which map passes each element of given iterable.
# iter: iterable which is to be mapped.
#-----------------------------------------------------------

# https://www.geeksforgeeks.org/packing-and-unpacking-arguments-in-python/
# NOTE: applications and important points:
# 1. Used in socket programming to send a vast number of requests to a server.
# 2. Used in Django framework to send variable arguments to view functions.
# 3. There are wrapper functions that require us to pass in variable arguments.
# 4. Modification of arguments become easy,
# but at the same time validation is not proper, so they must be used with care.
#-----------------------------------------------------------

# Unpacking
# A sample function that takes 4 arguments
# and prints the,
def fun(a, b, c, d):
    print(a, b, c, d)

my_list = [1, 2, 3, 4]

# Unpacking list into four arguments
fun(*my_list)
#-----------------------------------------------------------

# Packing
# This function uses packing to sum
# unknown number of arguments
def mySum(*args):
    sum = 0
    for i in range(0, len(args)):
        sum = sum + args[i]
    return sum

print(mySum(1, 2, 3, 4, 5))
print(mySum(10, 20))
#-----------------------------------------------------------

# Packing + Unpacking
# A sample python function that takes three arguments
# and prints them
def fun1(a, b, c):
    print(a, b, c)

# Another sample function.
# This is an example of PACKING. All arguments passed
# to fun2 are packed into tuple *args.
def fun2(*args):
    # Convert args tuple to a list so we can modify it
    args = list(args)

    # Modifying args
    args[0] = 'Geeksforgeeks'
    args[1] = 'awesome'

    # UNPACKING args and calling fun1()
    fun1(*args)

fun2('Hello', 'beautiful', 'world!')
#-----------------------------------------------------------

# For dic
# using **
def fun(a, b, c):
    print(a, b, c)

# A call with unpacking of dictionary
d = {'a': 2, 'b': 4, 'c': 10}
fun(**d)
