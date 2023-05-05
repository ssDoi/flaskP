from flask import Flask, request, render_template,redirect,url_for
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World'

@app.route('/hello')
def hellohtml():
    return render_template("hello.html")

@app.errorhandler(404)
def page_not_found(error):
    return "페이지가 없습니다. URL를 확인 하세요", 404

@app.route('/move/<url>')
def naverhtml(url):
    if url == "naver":
        return redirect("https://www.naver.com")
    elif url == "daum":
        return redirect("https://www.daum.net")
    
@app.route('/urltest')
def url_test():
    return redirect(url_for(naverhtml))

@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method == 'GET':
        # args_dict = request.args.to_dict()
        # print(args_dict)
        num = request.args["num"]
        name = request.args.get("name")
        return "GET으로 전달된 데이터({}, {})".format(num, name)
    else:
        num = request.form["num"]
        name = request.form["name"]
        return "POST로 전달된 데이터({}, {})".format(num, name)
    
if __name__ == '__main__':
    #with app.test_request_context():
     #   print(url_for('naverhtml'))
    app.run(debug=True)