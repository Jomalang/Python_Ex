# Generator ex1

def generator_ex1():
    print('start')
    yield 'A point'
    print('Continue')
    yield 'B point'
    print('End')

temp = iter(generator_ex1())
# print(temp)

# print(next(temp))
# print(next(temp))
# print(next(temp))

# Generator ex2
# temp2 = [x * 3 for x in generator_ex1()]
# temp3 = (x * 3 for x in generator_ex1())

# print(temp2)
# print(temp3)

# for i in temp3:
#     print(i)


# Generator ex3(중요 함수, filterfalse, accumlate, chain, product, groupby)
import itertools
gen1 = itertools.count(1, 2.5)
# print(next(gen1))
# print(next(gen1))
# print(next(gen1))
# print(next(gen1))
# print(next(gen1))

# 조건 추가
gen2 = itertools.takewhile(lambda n : n < 1000, itertools.count(1, 2.5))

# while True:
    # print(next(gen2))

print()
print()

# 필터의 반대 조건
gen3 = itertools.filterfalse(lambda n : n < 3, [1,2,3,4,5])

# for v in gen3:
    # print(v)

# 누적 합계
gen4 = itertools.accumulate([x for x in range(1,101)])

# for v in gen4:
    # print(v)


# 이터러블 체이닝
# gen5 = itertools.chain('abced', range(1,11,3))
# print(list(gen5))

# 이터러블 체이닝2
# gen6 = itertools.chain(enumerate('abcde'))
# print(list(gen6))
# temp = enumerate('abcde')
# print(list(temp))

# print(temp, gen6)

# 개별 튜플화
# gen7 = itertools.product('abcde', repeat=2)
# print(list(gen7))

# 그룹화
gen8 = itertools.groupby('aaabbccccddeeee')

# print(list(gen8))

for chr, group in gen8:
    print(chr, ' : ', list(group))