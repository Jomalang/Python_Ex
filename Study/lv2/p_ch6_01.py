# ch6
# 병행성(Concurrency)
# 이터레이터와 제네레이터

t = 'abcdefghijklmnopqrstuvwxyz'
# print(dir(t))

# i = iter(t)
# print(dir(i))

# print(hasattr(t, '__iter__')) #true

class WordSplitter:
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(' ')
    
    def __next__(self):
        try:
            word = self._text[self._idx]
        except IndexError:
            raise StopIteration('stopped Iteration')
        self._idx += 1
        return word
    
    def __repr__(self):
        return 'WordSplit(%s)' % (self._text)

# wi = WordSplitter('do today what you could do tommorrow')
# print(wi)
# print(next(wi))
# print(next(wi))
# print(next(wi))
# print(next(wi))
# print(next(wi))
# print(next(wi))
# print(next(wi))

class wordSplitGenerator:
    def __init__(self, text):
        self._text = text.split(' ')

    def __iter__(self):
        for word in self._text:
            yield word # yield키워드 사용
    
    def __repr__(self):
        return 'WordSplit(%s)' % (self._text)

wg = wordSplitGenerator('do today what you could do tommorrow')
wt = iter(wg)
print(type(wt), type(wg))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))