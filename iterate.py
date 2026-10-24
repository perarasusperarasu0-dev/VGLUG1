def decorate(func):
    def iterate_func(name):
        value = iter(name)    
        print(next(value))
        print(next(value))
        print(next(value))
        print(next(value))
        func()
    return iterate_func
    

@decorate
def my_func():
    print("YOUR NAME IS SUCCESSFULLY ITERATE 👍")

name = input("ENTER YOUR NAME^_^    :")

my_func(name)