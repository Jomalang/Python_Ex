import os
import time
from concurrent import futures

WORK_LIST= [10000, 100000, 1000000, 10000000]

# 동시에 합계 계산 메인 루틴
# 누적 합계 함수(제네레이터)
def sum_generator(n):
    return sum(n for n in range(1, n+1))

def main():
    # Worker count
    worker = min(10, len(WORK_LIST))
    
    # 시작 시간 
    start_time = time.time()

    
    # 결과 건수
    # ProcessPollExcutor
    with futures.ProcessPoolExecutor() as excutor:
        # map -> 작업순서 유지 및 즉시 실행
        result = excutor.map(sum_generator, WORK_LIST)

    #종료 시간
    end_time =  time.time() - start_time 

    # 결과 출력 포맷
    msg = '\n result = {} Time: {:.2f}s'
    print(msg.format(list(result), end_time))

# 메인 루틴의 진입점 - 멀티프로세싱의 진입점이 필요하다.
if __name__ == '__main__':
    main()



