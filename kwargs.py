# **kwargs = parameter that will pack all arguments into a dictionary
#            useful so that a function can accept a varying amount of keyword arguments

def hello(**names):
    # print("hello "+kwargs['first']+" "+kwargs['last'])
    print("Hello",end=" ")
    for key,value in names.items():
        print(value,end=" ")


hello(title = "Mr.", first="Bro", middle = "Dude",last="Code")