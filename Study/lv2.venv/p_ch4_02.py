# Tuple Advanced
# Unpacking

print(divmod(100, 9))
# 인자를 언패킹해서 전달
print(divmod(*(100, 9)))
# 결과를 언패킹해서 출력
print(*(divmod(100,9)))

x, y, *rest = range(10)
print(x, y, rest)

x, y, *rest = 1,2,3,4,5
print(x, y, rest)

# Mutable(가변) vs Immutable(불변)
t = (15, 20, 24)
l = [15, 20, 24]
print(t, id(t))
print(l, id(l))
t = t * 2
l = l * 2
print(t, id(t))
print(l, id(l))

t *= 2
l *= 2
print(t, id(t))
print(l, id(l))
