# concurrent wati, as_complete

import os
import time
from concurrent.futures import wait, as_completed, ProcessPoolExecutor

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

    # futures
    future_list = []

    
    # 결과 건수
    # ProcessPollExcutor
    with ProcessPoolExecutor() as excutor:
        for work in WORK_LIST:
            # 각각의 작업을 담는 future객체 생성
            future = excutor.submit(sum_generator, work)
            # 스케쥴링
            future_list.append(future)
            # 스케쥴링 확인
            print('Scheduled for {} : {}'.format(work, future))
            print()
        
        # wait 사용
        
        # # 7초의 시간이 넘는 작업은 실패한 것으로 간주함.
        # result = wait(future_list, timeout=7)
        # # 성공한 작업들 표시
        # print('Completed Tasks : ' + str(result.done))
        # # 실패한 작업들 표시
        # print('Failed Tasks : ' + str(result.not_done))
        # # 결과 값 출력
        # print([future.result() for future in result.done])

        # as_complted
        for future in as_completed(future_list):
            result = future.result()
            done = future.done()
            cancelled = future.cancelled

            #future 결과 확인
            print('Future Result : {}, Done : {}'.format(result, done))
            print('Future Cancelled : {}'.format(cancelled))

    #종료 시간
    end_time =  time.time() - start_time 

    # 결과 출력 포맷
    # msg = '\n result = {} Time: {:.2f}s'
    # print(msg.format(list(result), end_time))

# 메인 루틴의 진입점 - 멀티프로세싱의 진입점이 필요하다.
if __name__ == '__main__':
    main()



