# python을 사용해서 몽고디비 다루기
# pymongo -> venv(가상환경)에 설치하기
# host(url) -> 내 몽고 디비의 주소 : 포트
# ID/PW -> mongoDB 접속 id, pw

from pymongo import MongoClient

client = MongoClient('localhost',27017) # host, id ,pw 같은게 필요 여기서느 host 서버 연결함
db = client.mydata

#create
#users 공간에 insert_one 안에 있는 데이터를 insert 한번 넣으면 건들지 않아도 됨
# db.users.insert_one({'name' : '해리','age' : 20})
# db.users.insert_one( {'name' : '포터','age' : 21})
# db.users.insert_one( {'name' : '론','age' : 22})
# db.users.insert_one({'name' : '위즐리','age' : 23})


# 조회 Read
#users라는 공간에
# my_users = list(db.users.find({}))
# # print(my_users) -> list니까 for문 사용
# for i in my_users:
#     print(i)

# my_users = db.users.find_one({'name' : '해리'}) #name 이 해리인 데이터를 가져온다. 하나
# print(my_users)
#
# many_users = list(db.users.find({'name':'해리'})) #해당하는 조건의 모든 데이터를 가져온다.
# print(many_users)
#

#update 값 수정하기
# db.users.update_one({'name':'해리'},{'$set':{'age':100}}) #, 앞에는 조건(어떤걸 update하겠다) ,뒤에는 어떻게 수정할건지(age를 100으로 수정한다)
# print(list(db.users.find({'name' : '해리'})))

#delete
db.users.delete_one({'name':'해리'})