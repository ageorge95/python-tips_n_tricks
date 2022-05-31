# The MRO works from the bottom to the top

class First():
    # it is a good practice to let people know
    # that this variable will be used in the inheritor
    final_arg: int

    def __init__(self):
        print("first", self.final_arg)
        super(First, self).__init__()

class Second():
    # it is a good practice to let people know
    # that this variable will come from the inheritor
    final_arg: int

    def __init__(self):
        print("second", self.final_arg)
        super(Second, self).__init__()

class Third(First,
            Second):

    def __init__(self):
        self.final_arg = 0
        print('third')
        super(Third, self).__init__()

obj = Third()