# web2.py 
#웹서버에 요청
import requests
#크롤링
from bs4 import BeautifulSoup
 
 
url = "https://www.daangn.com/kr/buy-sell/?in=%EC%9A%A9%EC%82%B0%EA%B5%AC-36"

response = requests.get(url)
#검색이 용이한 객체 생성
soup = BeautifulSoup(response.text, "html.parser")

#<h2 class="_1b153uwk _1b153uwj _588sy41w _588sy41b">아이언 정리합니다.</h2>

posts = soup.find_all("div", attrs={"class":"card-desc"})
for post in posts:
    title = post.find("h2", attrs={"class":"card-title"})
    price = post.find("div", attrs={"class":"card-price"})
    addr = post.find("div", attrs={"class":"card-region-name"})
    print("{0} , {1} , {2}".format(title, price, addr))

# <div class="card-desc">
#       <h2 class="card-title">애플워치 1만원에 ㅍㅍ</h2>
#       <div class="card-price ">
#         10,000원
#       </div>
#       <div class="card-region-name">
#         서울 서초구 반포동
#       </div>
