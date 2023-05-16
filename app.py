from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/")
def h1():
    return render_template('img_static.html')

@app.route("/myprofile/new", methods=["GET"])
def post_profile():

    return render_template('sub.html')

@app.route('/test', methods=['GET'])
def test_get():
   title_receive = request.args.get('title_give')
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 GET!'})

@app.route('/test', methods=['POST'])
def test_post():
   title_receive = request.form['title_give']
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 POST!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)