def star(**kwargs):
    def inner(func):
        # Execute this code before anything else
        print("*" * 30)
        print(f"Star decorator received {kwargs.get('msg')}")
        print("*" * 30)
        # Return func so that it will be executed with the callers params
        return func

    return inner  # this will be called with the function as the argument

if __name__ == '__main__':
    @star(msg='star_message')
    def printer(**kargs):
        print(kargs.get('msg'))

    printer(msg="Hello")