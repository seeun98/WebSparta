import requests
from bs4 import BeautifulSoup


my_url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200716'

res = requests.get(my_url) # HTML, CSS, JS가 응답으로 들어옴

#응답을 분석한다.
soup = BeautifulSoup(res.text, 'html.parser')


movies = soup.select('#old_content > table > tbody > tr')

for movie in movies:
    a_tag = movie.select_one('td.title > div > a')
    if a_tag is not None: # a is None
        print(a_tag.text)

"#old_content > table > tbody > tr:nth-child(2) > td.title > div > a" #반복되는 것 기준으로 select 안에 넣고




