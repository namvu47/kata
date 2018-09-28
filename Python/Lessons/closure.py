def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

# Multiplier of 3
times3 = make_multiplier_of(3) #closure

# Multiplier of 5
times5 = make_multiplier_of(5) #closure

#returns a tuple of cell objects if it is a closure function
print(times3.__closure__)

#cell_contents: stores the closed value.
print(times3.__closure__[0].cell_contents)

# Output: 27
print(times3(9))

# Output: 15
print(times5(3))

# Output: 30
print(times5(times3(2)))
