import requests
from bs4 import BeautifulSoup

# 크롤링할 URL
url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%B0%98%EB%8F%84%EC%B2%B4"

# HTTP 요청
response = requests.get(url)

# 응답 상태 확인
if response.status_code == 200:
    # BeautifulSoup 객체 생성
    soup = BeautifulSoup(response.text, 'html.parser')

    # 신문기사 제목 크롤링
    titles = soup.find_all('a', class_='news_tit')  # class 이름은 페이지 구조에 따라 다를 수 있음
    for idx, title in enumerate(titles, start=1):
        print(f"{idx}. {title.get_text()} - {title['href']}")
else:
    print(f"HTTP 요청 실패: {response.status_code}")
