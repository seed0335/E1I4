from pymongo import MongoClient

import certifi
ca = certifi.where()

client = MongoClient('mongodb+srv://sparta:test@cluster0.rsr8xyc.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

doc = {
    'imoge':'🍜',                           
    'blog1' : 'https://velog.io/@owiiwo',
    'blog2' : 'https://velog.io/@owiiwo',
    'name' : '이은비',
    'about_me':'안녕하세요! E1I4의 페이지에서 팀 소개를 제작한 이은비입니다.',
    'Q1':'HTML, JavaScript, CSS, Python(flask)',
    'Q2':'밝고 긍정적이다!',
    'Q3':'ISTJ',
    'Q4':'컵누들을 좋아합니다😍'
}
db.profiles.insert_one(doc) 

# 이은비님 본인 데이터 저장해주세요. (위에 주소 본인DB로 변경 한 후 테스트하기)
# DB에 profiles가 없어서 오류가 나면 이 코드 주석 풀고 터미널 실행하기 (더미데이터)