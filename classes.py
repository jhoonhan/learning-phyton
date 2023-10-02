class Printer:
    def __init__(self, name):
        self.name = name

    # def __str__(self):
    #     return f"{self.name} wtf"

    def testfn(self):
        print("aaaang!")

    def my_func(self):
        self.testfn()
        # print(f"{self.name} func yeah")


child = Printer("aang").my_func()

# child.my_func()
