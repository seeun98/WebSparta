from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route("/my-project")
def my_test_page():
    return render_template('myhtml.html') #페이지 전달 html,javascript,,

@app.route('/posttest', methods=['POST']) #url은 psttest, POST 방식
def post_my_test():
    form = request.form['query'] #변수명이 query인걸 받아와서
    print(form) #출력하고
    return jsonify({'result':'success','msg':form}) #돌려준다.

@app.route('/mytest', methods=['GET']) #app.route(주소 만들어주는.. /mytest : url 만들기 methods(['GET']) get방식의 통신만 하겠다.
def get_my_test():
    query_string = request.args.get('q') #request.args.get -> url의 ? 뒤에 있는 변수를 가져온다.
    print(query_string)
    return jsonify({'result':'success','msg':query_string}) #json 형태로 만들어주겠다.

@app.route("/test")
def my_test():
    return 'this is test page' #json 데이터 전달


@app.route("/")

def home():
    return "hello world!"

if __name__ == '__main__': #이걸 써야 실행됨
    app.run('127.0.0.1', port=5000, debug=True)



