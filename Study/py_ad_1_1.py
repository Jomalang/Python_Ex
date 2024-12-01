"""
Chapter 1
Python Variable Scope
keyword - scope, globa, nonlocal, locals, globals 
"""

"""
전역변수와 지역변수
"""

# Ex1
a = 10

def foo():
    # 전역변수 읽기 가능
    print('Ex1 > ', a)

foo()

# Ex2
b= 20
def bar():
    # 지역변수 선언
    b = 30
    print('Ex2 > ', b)

bar()
print('Ex2 > ', b)

# Ex3
c = 40
def foobar():
    # c = c + 10
    print('Ex3 > ', c)

foobar() # Error

# Ex4
d = 50
def barfoo():
    global d
    d = d + 10
    print('Ex4 > ', d)

barfoo()

# Ex5
def outer():
    e=60
    def inner():
        nonlocal e
        e += 10
        print('Ex5 > ', e)
    return inner

in_test = outer() #Closure

in_test()
in_test()
in_test()
in_test()

# Ex6
def func(var):
    x = 10
    def printer():
        print('Ex6 > ', "Printer Func Inner")
    print('Func Inner', locals())

func('hello wolrd')

#Ex7
print('Ex7 > ', globals())

#Ex8
for i in range(1, 10):
    for k in range(1, 10):
        globals()['mul_{}_{}'.format(i, k)] = i * k

print(globals())



