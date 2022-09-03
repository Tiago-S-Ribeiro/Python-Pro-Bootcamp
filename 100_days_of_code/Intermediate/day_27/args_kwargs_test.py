def add (*args):
    sum = 0
    for n in args:
        sum += n
    return sum

def calc(n, **kwargs):
    #print(kwargs)
    n += kwargs["add"]
    n *= kwargs["mult"]
    print(n)


print(add(10,20,30))
calc(2, add=3, mult=5)

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        #self.model = kwargs["model"]  isto dá erro se nao for passado model por parametro
        self.model = kwargs.get("model") #com get não dá erro, fica 'None'
        self.color = kwargs.get("color")
        self.year = kwargs.get("year")

my_car = Car(make="bmw", model="gtr")
my_car2 = Car(make="fiat")

print(my_car2.model)
