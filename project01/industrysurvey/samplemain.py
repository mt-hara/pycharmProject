class MyClass():
    def __init__(self,var1, var2):
        self.var1 = var1
        self.var2 = var2

if __name__ == "__main__":
    mc = MyClass(10,20)
    print(mc)
    for k,v in vars(mc).items():
        print("{} = {}".format(k,v))