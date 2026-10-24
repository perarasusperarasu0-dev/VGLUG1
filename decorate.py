def py_dec(func):
    count = [0]
    
    def another_function():
        count[0]+=1
        print("wich programming language is easy ?")
        func()
        print(count[0],"yes python is easy level programming language")
    return another_function
    


@py_dec
def my_function():
    print(" PYTHON IS EASY LEVEL LANGUAGE")

my_function()
my_function()

my_function()
my_function()

