#ch5
# 일급 함수(일급 객체)
# 1. 런타임 시점에 초기화된다.
# 2. 변수에 할당가능하다.
# 3. 함수를 다른 함수의 인수에 전달 가능하다.
# 4. 함수를 함수의 결과로 반환가능하다.

# 함수 객체
def factorial(n):
    '''Factorial Function -> n : int'''
    if n ==1:
        return 1
    return n*factorial(n-1)

# 비교를 위한 임시 클래스
class A:
    pass

print(set(sorted(dir(factorial))) - set(sorted(dir(A))))

# reduce
from functools import reduce
from operator import add

# 1부터 10까지 더하기
print(sum(range(1,11)))
print(reduce(add, range(1,11)))
print(reduce(lambda x, t: x+t, range(1,11)))

# partial
from operator import mul
from functools import partial

# 인수 고정 - 첫 인자를 5로 고정시킴
five = partial(mul, 5)

print([five(i) for i in range(1,10)])