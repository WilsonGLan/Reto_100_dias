# Probando el paso de argumentos sin limite
def add(*args):
    #print(args)
    sum = 0
    for i in range(len(args)):
        sum += args[i]
    print (sum)


#Todo: Al llamar a la función se pueden pasar la cantidad de argumentos que uno quiera sin error
add(4,2,3,1,10)