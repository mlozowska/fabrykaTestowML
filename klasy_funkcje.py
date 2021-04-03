# def function(name, age):
#     print('My name is ' + name+ '. I am ' + str(age) +' old!')
#
#
# function('Magda', 31)
# funkcja dzielenie przez 0
'''
def divide(divident, divisor):
    if (divisor == 0):
        return False
    else:
        return divident / divisor


print(divide(3, 0))
print(divide(3, 1))


# funkcja z atrybutami
def my_function(arg1, arg2='Kasia'):
    return f'{arg1}, {arg2}'


print(my_function('Zosia', 'Marek'))
print(my_function(arg1='Seat'))

# funkcja czesciowa
from functools import partial


def division(x, y):
    return x / y


divide_by_two = partial(division, 2)
print(divide_by_two(6))
print(divide_by_two(11))
print(divide_by_two(7))
'''

# Klasy i obiekty

class MyFirstClass():
    var1 = [1,22,3.4]
    var2 = 2
    def function(self): # jak funkcja w klasie to parametr SELF obowiazkowy
        print('Hi')

object = MyFirstClass
# object.var1
print(object.var1[-1])
print(object.var2)

object2 = MyFirstClass()
print(object2.function())
