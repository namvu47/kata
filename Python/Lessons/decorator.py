# def make_pretty(func):
#     def inner():
#         print("I got decorated")
#         func()
#     return inner
#
# def ordinary():
#     print("I am ordinary")

# make_pretty: decorator
# func ordinary got decorated and returned pretty
# pretty = make_pretty(ordinary)

def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

@make_pretty
def ordinary():
    print("I am ordinary")

# equal to
# def ordinary():
#     print("I am ordinary")
# ordinary = make_pretty(ordinary)

ordinary()

# parameters of the nested inner() function inside the decorator is same as the parameters of functions it decorates

# general decorators that work with any number of parameter.
# args: the tuple of positional arguments
# kwargs will be the dictionary of keyword arguments.

# def works_for_all(func):
#     def inner(*args, **kwargs):
#         print("I can decorate any function")
#         return func(*args, **kwargs)
#     return inner

def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner

def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner

@star
@percent
def printer(msg):
    print(msg)
printer("Hello")

# equal to
# def printer(msg):
#     print(msg)
# printer = star(percent(printer))