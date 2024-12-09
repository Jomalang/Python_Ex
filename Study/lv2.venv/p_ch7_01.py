# ch7
# AsyncIO

import asyncio
import timeit
# urlopen은 blocking I/O방식이다.
# blocking I/O들은 보통 멀티 프로세스, 멀티 쓰레딩과 함께 사용해 non-blocking처럼 되도록 한다.
from urllib.request import urlopen 
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
import threading
import sys
import io

# 실행 시작 시간
start = timeit.default_timer()
urls = ['https://naver.com', 'https://inflearn.com', 'https://okky.kr']

async def fetch(url, executor):
    # 쓰레드명 출력
    print('Thread Name : ', threading.current_thread().getName(), 'Start', url)
    # 실행
    response = await loop.run_in_executor(executor, urlopen, url)

    soup = BeautifulSoup(response.read(), 'html.parser')

    # 전체 페이지 소스 확인
    # print(soup.prettify())

    print('Thread Name : ', threading.current_thread().getName(), 'Done', url)

    # 타이틀 확인
    result_title = soup.title
    return result_title
    

async def main():
    # 쓰레드 풀 생성
    executor = ThreadPoolExecutor(max_workers=10)

    # future 객체를 모아 gather에서 실행
    futures = [
        asyncio.ensure_future(fetch(url, executor)) for url in urls
    ]

    # 결과 취합, futures의 작업이 다 끝날때까지 대기
    result = await asyncio.gather(*futures)

    print()
    print('result : ', result)

if __name__ == '__main__':
    # 루프 초기화
    loop = asyncio.get_event_loop()
    # 작업 완료까지 대기
    loop.run_until_complete(main())
    # 수행 시간 계산
    duration = timeit.default_timer() - start
    # 총 실행 시간
    print('Total Running Time : ', duration)