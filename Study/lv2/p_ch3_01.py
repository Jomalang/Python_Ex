#ch3
#Special Method

print(int)
print(float)

# print(dir(int))
# print(dir(float))

n = 10
print(type(n))

n + 100
n.__add__(100)

# 클래스 예제
class Fruit:
    def __init__(self, name, price):
        self._name = name
        self._price = price
        
    def __str__(self):
        return 'Fruit Class Info : {} {}'.format(self._name, self._price)

    def __add__(self, x):
        return self._price + x._price

s1 = Fruit('Orange', 7500)
s2 = Fruit('Banana', 3000)
print(s1 + s2)
