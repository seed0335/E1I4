from pymongo import MongoClient

import certifi
ca = certifi.where()

#client = MongoClient('mongodb+srv://sparta:test@cluster0.rsr8xyc.mongodb.net/?retryWrites=true&w=majority')
client = MongoClient('mongodb+srv://sparta:test@cluster0.txlb0px.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

doc = {
    'imoge':'🖥',                           
    'blog1' : 'https://dilution0216.tistory.com/',
    'blog2' : 'https://dilution0216.tistory.com/',
    'name' : '김희석',
    'about_me':'안녕하세요! E1I4의 페이지에서 방명록를 제작한 김희석입니다.',
    'Q1':'HTML, JavaScript, CSS, Python(flask,Django)',
    'Q2':'JUST DO IT',
    'Q3':'유일한 E! ESTJ',
    'Q4':'딸기와 딸기라떼를 좋아합니다!'
}
db.profiles.insert_one(doc) 

# 김희석님 본인 데이터 저장해주세요. (위에 주소 본인DB로 변경 한 후 테스트하기)
# DB에 profiles가 없어서 오류가 나면 이 코드 주석 풀고 터미널 실행하기 (더미데이터)