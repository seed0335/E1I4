from pymongo import MongoClient

# client = MongoClient('mongodb+srv://sparta:test@cluster0.w1iiuru.mongodb.net/?retryWrites=true&w=majority')
client = MongoClient('mongodb+srv://sparta:test@cluster0.rsr8xyc.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

doc = {
    'imoge':'💍',                           
    'blog1' : 'https://chun-k.tistory.com/',
    'blog2' : 'https://chun-k.tistory.com/',
    'name' : '이현경',
    'about_me':'안녕하세요! E1I4의 페이지에서 멤버 소개파트를 제작한 이현경입니다.',
    'Q1':'HTML, CSS, JAVASCRIPT, JAVA, PYTHON',
    'Q2':'화가 없는 편입니다.',
    'Q3':'모든게 100%으로 쏠려있어 중간이 없는 극ISTP',
    'Q4':'아침마다 헬스장 다녀요!! 근손실 절대 지켜~',
}

db.profiles.insert_one(doc) 

# 이현경님 본인 데이터 저장해주세요. (위에 주소 본인DB로 변경 한 후 테스트하기)
# DB에 profiles가 없어서 오류가 나면 이 코드 주석 풀고 터미널 실행하기 (더미데이터)