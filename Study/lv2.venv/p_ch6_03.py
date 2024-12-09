# corutine ex1

def coroutine1():
    print('>>> coroutine started')
    i = yield
    print('>>> coroutine received : {}'.format(i))

# 메인 루틴
# 제네레이터 선언
cr1 = coroutine1()
# print(cr1, type(cr1))

# 양방향 전달
# next(cr1)
# ret = cr1.send(100)
# print(ret)


# 코루틴 Ex2
# GEN_CREATED : 처음 대기 상태
# GEN_RUNNING : 실행 상태
# GEN_SUSPENDED : yield 대기 상태 (이때 값을 주고받을 수 있음)
# GEN_CLOSED : 실행 완료 상태

def coroutine2(x):
    print('>>> coroutine started : {}'.format(x))
    y = yield x
    print('>>> coroutine received : {}'.format(y))
    z = yield x + y
    print('>>> coroutine received : {}'.format(z))

cr3 = coroutine2(10)

from inspect import getgeneratorstate

print(getgeneratorstate(cr3))

print(next(cr3))

print(getgeneratorstate(cr3))

cr3.send(100)

# 중첩 코루틴 처리
def generator1():
    for x in 'ab':
        yield x
    for y in range(1,5):
        yield y

t1 = generator1()

print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))

t2 = generator1()
print(list(t2))


print()
print()

def generator2():
    yield from 'ab'
    yield from range(1,5)

t3 = generator2()
print(next(t3))
print(next(t3))
print(next(t3))
print(next(t3))
print(next(t3))
print(next(t3))