from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
from bson.objectid import ObjectId
import requests
import bs4
import logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://leepari20:test@cluster0.bn6xn4r.mongodb.net/')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/guestbook', methods=['POST'])
def guestbook_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    doc = {
        'name'  :name_receive,
        'comment' : comment_receive
    }
    db.guestbook_comments.insert_one(doc)
    return jsonify({'msg': '방명록이 등록되었습니다!'})

@app.route("/")
def h1():
    return render_template('img_static.html')

@app.route("/myprofile/new1", methods=["GET"])
def profiles_get():
    all_profiles = db.profiles.find_one({"_id": ObjectId(id)})
    
    return jsonify({'result': all_profiles})

@app.route("/myprofile/new", methods=["GET"])
def post_profile():
    
    return render_template('sub.html', member_id = id)

@app.route('/sub')
def sub():
    return render_template('sub.html')

@app.route('/test', methods=['GET'])
def test_get():
    title_receive = request.args.get('title_give')
    print(title_receive)
    return jsonify({'result':'success', 'msg': '이 요청은 GET!'})


@app.route("/guestbook", methods=["GET"])
def guestbook_get():
    all_comments = list(db.guestbook_comments.find({},{'_id':False}))
    #db.user.find 에서 users 바꿔야한다 일단 강의대로 fan으로 저장함
    #fan -> guestbool_comments 로 변경
    return jsonify({'result': all_comments})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)