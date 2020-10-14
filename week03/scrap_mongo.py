from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup

client = MongoClient('localhost', 27017)
db = client.mydata
my_url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200716'

res = requests.get(my_url) # HTML, CSS, JS가 응답으로 들어옴

#응답을 분석한다.
soup = BeautifulSoup(res.text, 'html.parser')


movies = soup.select('#old_content > table > tbody > tr')

for movie in movies: #한줄씩 뽑음
    a_tag = movie.select_one('td.title > div > a')
    if a_tag is not None: # a is None
        title = a_tag.text
        rank = movie.select_one('td:nth-child(1) > img')['alt']
        star = movie.select_one('td.point').text
        # print("저장 >>>   ", rank, title, star)
        # print(a_tag.text)
        #PYMONGO를 사용해서 DATA 저장하기
        # nmovie
        # 저장되는 데이터의 형태는 dictionary
        movie_dict = {
            'title' : title,
            'rank' : rank,
            'star' : star
        }
        db.movie.insert_one(movie_dict)
        my_movie = db.movie
"#old_content > table > tbody > tr:nth-child(2) > td.title > div > a" #반복되는 것 기준으로 select 안에 넣고




