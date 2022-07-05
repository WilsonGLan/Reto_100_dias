# Probando el paso de argumentos sin limite
from audioop import mul


def add(*args):
    #print(args)
    sum = 0
    for i in range(len(args)):
        sum += args[i]
    print (sum)


#Todo: Al llamar a la función se pueden pasar la cantidad de argumentos que uno quiera sin error
add(4,2,3,1,10)

# Pasar argumentos a modo de diccionario
def calculate(n,**kwargs):
    ({print(key):print(value) for (key, value) in kwargs.items() if value is not None and key is not None})
    #print({value for (key, value) in kwargs.items()})
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(3, add=3, multiply=5)

def bar(spam, eggs, toast='yes please!', ham=0):
    print(spam, eggs, toast, ham)
 
bar(toast='nah', spam=4, eggs=2)


def all_aboard(a, *args, **kw): 
    print(a, args, kw)
 
all_aboard(4, 7, 3, 0, x=10, y=64)