from pymongo import MongoClient

client = MongoClient('mongodb+srv://sparta:test@cluster0.rsr8xyc.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

doc = {
    'imoge':'🐶',
    'blog1' : 'https://velog.io/@hoy503007',
    'blog2' : 'https://velog.io/@hoy503007',
    'name' : '임수영',
    'about_me':'강아지를 키우고 있습니다.',
    'Q1':'Java👍, Spring✨',
    'Q2':'같은 화면을 계속 봐도 지루해 하지 않음(코딩특화)',
    'Q3':'ISTP',
    'Q4':'강아지를 키우고 있습니다.',
}
db.profiles.insert_one(doc) 

# 임수영님 본인 데이터 저장해주세요.(위에 주소 본인DB로 변경 한 후 테스트하기)
# DB에 profiles가 없어서 오류가 나면 이 코드 주석 풀고 터미널 실행하기 (더미데이터)