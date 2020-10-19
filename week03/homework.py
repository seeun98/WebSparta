import requests
from bs4 import BeautifulSoup

#타겟 url 읽어서 html을 받아온다.
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
my_url = 'https://banksalad.com/savings'
res = requests.get(my_url)

#응답 분석
# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(res.text, 'html.parser')
print(soup)
banks = soup.select('#bankListContainer_1adds > ul  #cardList_1E5c4 > #header_M05Gy')

for bank in banks:
    a_tag = movie.select_one('h4')
    if a_tag is not None:
        print(a_tag.text)