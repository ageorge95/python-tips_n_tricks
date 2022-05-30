def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        # execute func() here
        func(*args, **kwargs)
        print("*" * 30)

    return inner

def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        # execute func() here
        func(*args, **kwargs)
        print("%" * 30)

    return inner

if __name__ == '__main__':
    # this code
    @star
    @percent
    def printer(msg):
        print(msg)
    printer("Hello")
    print('\n')


    # is equivalent to
    def printer(msg):
        print(msg)
    printer = star(percent(printer))
    printer("Hello")