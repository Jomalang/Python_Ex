#클로저

# 클래스 이용
class Averager():
    def __init__(self):
        self._series = []

    def __call__(self,v):
        self._series.append(v)
        print('inner >> {} / {}'.format(self._series, len(self._series)))
        return sum(self._series) / len(self._series)
    
# 인스턴스 생성
averager = Averager()
averager(10)
averager(10)
averager(10)
averager(10)
        
