# 클래스 예제2
class Vector(object):
    def __init__(self, *arg):
        '''
        Create a vector, example: v = Vector(1,2)
        '''
        if len(arg) == 0:
            self._x, self._y = 0, 0
        else:
            self._x, self._y = arg
    
    def __repr__(self):
        '''Returns the vector informations.'''
        return 'Vector(%r, %r)' % (self._x, self._y)

    def __add__(self, other):
        return Vector(self._x + other._x, self._y + other._y)
    
    def __mul__(self, s):
        return Vector(self._x * s, self._y * s)

    def __bool__(self):
        return bool(max(self._x, self._y))

# Vector 인스턴스 생성
v1 = Vector(3, 5)
v2 = Vector(15, 20)
v3 = Vector()

for vector in (v1, v2, v3):
    print(vector)
