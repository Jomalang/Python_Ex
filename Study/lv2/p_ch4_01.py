#ch04 - 시퀀스
# 파이썬에선 시퀀스 타입을 컨테이너와 플랫, 두개로 나눈다.

# 지능형 리스트(Comprehending Lists)
chars = '+_)(*&^%$#@!)'
code_list1 = []

for s in chars:
    code_list1.append(ord(s))

code_list2 = [ord(s) for s in chars]
# print(code_list2)

# Comprehending Lists + Map, Filter
code_list3 = [ord(s) for s in chars if ord(s) > 40]
# print(code_list3)

code_list4 = list(filter(lambda x : x > 40, map(ord, chars)))
# print(code_list4)

# Generator 생성
import array 

tuple_g = (ord(s) for s in chars)
# print(next(tuple_g))
# print(next(tuple_g))
# print(next(tuple_g))
# print(next(tuple_g))
# print(next(tuple_g))

# array생성
array_g = array.array('I', (ord(s) for s in chars))
# print(type(array_g))
# print(array_g.tolist())

#제네레이터 예제
# for s in ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1,21)):
#     print(s)

# 리스트 사용시 주의(깊은 복사, 얕은 복사)
mk1 = [['~'] * 3 for _ in range(3)]
print(mk1)

mk2 = [['~'] * 3] * 3
mk2[0][1] = '*'
print(mk2)

print([id(i) for i in mk1])
print([id(i) for i in mk2])



