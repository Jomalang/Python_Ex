# 데코레이터

# 실행시간 측정
import time
def perf_clock(func):
    def perf_clocked(*args):
        # 함수 시작 시간 측정
        st = time.perf_counter()
        # 함수 실행
        result = func(*args)
        # 함수 종료 시간 측정
        et = time.perf_counter() - st
        # 실행 함수 명
        name = func.__name__
        # 함수 매개변수
        arg_str = ', '.join(repr(arg) for arg in args)
        # 결과 출력
        print('[%0.5fs] %s(%s) -> %r' % (et, name, arg_str, result))
        return result
    return perf_clocked
     
# 데코레이터 사용
@perf_clock
def test_func(numbers):
    return sum(numbers)

# 데코레이터 미사용
# none_deco = perf_clock(test_func)
# none_deco([i for i in range(100)])

test_func([i for i in range(100)])