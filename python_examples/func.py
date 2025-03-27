import math

def circle_stats(radius):
    area = math.pi * radius **2
    circumference = 2 * math.pi *radius
    return (f"Area = {round(area,4)}, circumference = {round(circumference,4)}")

print(circle_stats(2))

area = lambda y: math.pi * y ** 2             #, lambda x: 2 * math.pi * x
circumference = lambda x: 2 * math.pi * x

print(f"Area = {round(area(2),4)} circumference = {round(circumference(2),4)}")



def sum_all(*args):
    print(args)
    for i in args:
        print(i*2)
    return sum(args)

print(sum_all(1,2,3))


def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        return(f"{key}:{value}")

print(print_kwargs(name="wasiy",age=16,enemy="Emon",friend="Farhan"))


