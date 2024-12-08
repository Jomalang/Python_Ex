# 파이썬의 모든 객체는 id와 type으로 구분된다.

# 일반적인 튜플
point1 = (1.0, 5.0)
point2 = (2.5, 1.5)

from math import sqrt
l_leng1 = sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

print(l_leng1)

# named tuple 사용
from collections import namedtuple

# named tuple 선언
Point = namedtuple('Point', 'x y')

# 두 점 선언 및 할당
pt3 = Point(1.0, 5.0)
pt4 = Point(2.5, 1.5)

l_lent2 = sqrt((pt3.x - pt4.x) ** 2 + (pt3.y - pt4.y) ** 2)


# named tuple 선언 방법1 (리스트 사용)
Point1 = namedtuple('Point', ['x', 'y'])

# named tuple 선언 방법2 (콤마 사용)
Point2 = namedtuple('Point', 'x, y')

# named tuple 선언 방법3 (띄어쓰기 사용)
Point3 = namedtuple('Point', 'x y')

# named tuple 선언 방법4 (예약어나 중복되는 키 사용 시 - rename옵션 true)
Point4 = namedtuple('Point', 'x y x class', rename=True) # Default=False
print(Point4)

# 출력
print(Point1, Point2, Point3, Point4)

# 객체 생성
p1 = Point1(x=10, y=35)
p2 = Point2(20, 40)
p3 = Point3(45, y=20)
p4 = Point4(10, 20, 30, 40)

print(p4)


# Dict to Unpacking
temp_dict = {'x': 75, 'y': 55}
p5 = Point1(**temp_dict)
print(p5)

# named tuple method
temp = [52, 38]
p6 = Point1._make(temp)
print(p6)

print(p6._fields)

print(p6._asdict())

# 예제
Classes = namedtuple('Classes', 'rank, number')

# 그룹 리스트 선언
numbers = [str(n) for n in range(1,21)]
ranks = 'A B C D'.split()
print(numbers)
print(ranks)

# List Comprehension
students = [Classes(rank, number) for rank in ranks for number in numbers]
print(len(students))

# 추천하는 방식
students2 = [Classes(rank, number)
             for rank in 'A B C D'.split()
                for number in [str(n) for n in range(1, 21)]]

print(students2)


