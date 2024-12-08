# Dict 구조
# print(__builtins__.__dict__)

t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40, 50])

print(hash(t1))
# print(hash(t2))

# Dict Setdefault
source = (('k1', 'val1'),
          ('k1', 'val2'),
          ('k2', 'val3'),
          ('k3', 'val4'))

new_dict1 = {}

# No use Setdefault
for k, v in source:
    if k in new_dict1: #이미 존재하는 키가 순회되었을때
        new_dict1[k].append(v) #기존의 키에 추가
    else:
        new_dict1[k] = [v]

print(new_dict1)
        

new_dict2 = {}

# Use Setdefault
for k ,v in source:
    new_dict2.setdefault(k, []).append(v)

print(new_dict2)

# 주의
new_dict3 = {k: v for k, v in source}
print(new_dict3)