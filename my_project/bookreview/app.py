from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.bookreview
#페이지 띄우기
#응답 : html 파일 -> render_template
@app.route("/")
def home():
    return render_template('bookreview.html') #templates 안에 있는 html가져온다.

#GET 요청 -> 데이터 읽어오기 -> mongoDB에서 읽어오기
# 응답 : JSON -> jsonify() 사용
@app.route('/review', methods=['GET'])
def get_review():
    my_data = list(db.review.find({}, {'_id' : 0})) #db에 있는 걸 list로 저장해서 my_data 에 저장
    return jsonify({'result' : 'success' , 'data' : my_data}) #읽은 것이 success 구문으로 간다.

# POST 요청 -> 데이터를 작성/수정/삭제 -> mongoDB
# 응답 : JSON
@app.route("/review", methods=['POST'])
def post_review():
    title = request.form['title_post']
    author = request.form['author_post']
    review = request.form['review_post']
    print(title, author, review)

    my_dict = {
        'title' : title,
        'author' : author,
        'review' : review
    }

    db.review.insert_one(my_dict)
    return jsonify({'result':'success', 'msg':'POST 입니다'})


if __name__ == '__main__':
    app.run('127.0.0.1', port=5000, debug=True)
