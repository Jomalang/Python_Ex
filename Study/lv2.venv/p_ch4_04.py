# Set자료형은 중복을 허용하지 않는다.

# immutable Dict
from types import MappingProxyType

# 수정 가능
d = {'key1': 'value1'}

# 수정 불가능
d_frozen = MappingProxyType(d)

# d_frozen['key1'] = 'value2'

# set
s1 = {'apple', 'orange', 'apple', 'orange', 'kiwi'}
s2 = set(['apple', 'orange', 'apple', 'orange', 'kiwi'])
s3 = {1}
# 빈 set을 선언할때는 set()을 이용해야 한다. {}는 빈 딕셔너리 생성한다.
s4 = set() 
# 읽기 전용 set선언
s5 = frozenset({'apple', 'orange', 'apple', 'orange', 'kiwi'})

# 선언 최적화
from dis import dis
print('------------------')
print(dis('{1}'))
print('------------------')
print(dis('set([10])'))

# Comprehending Set

from unicodedata import name

print({name(chr(i), '') for i in range(0, 256)})