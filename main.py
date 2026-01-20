import streamlit as st
st.title("My first web app!!")
st.write('Hello! Good to see you! :)')
import streamlit as st
import time

# 🎨 페이지 설정
st.set_page_config(page_title="일본 여행 올인원 가이드", page_icon="🗾", layout="wide")

# ✨ 다크 & 네온 커스텀 CSS
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f0c29 0%, #24243e 100%);
    }
    h1, h2, h3, h4, p, span, div, label {
        color: #ffffff !important;
    }
    .day-container {
        background-color: rgba(255, 255, 255, 0.08);
        padding: 25px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.15);
        margin-bottom: 30px;
    }
    .place-box {
        display: flex;
        align-items: center;
        background: rgba(0, 0, 0, 0.5);
        margin: 15px 0;
        padding: 20px;
        border-radius: 15px;
        border-left: 6px solid #00D2FF;
    }
    .place-text {
        flex: 1;
        padding-right: 25px;
    }
    .place-img {
        width: 200px;
        height: 130px;
        object-fit: cover;
        border-radius: 12px;
        border: 2px solid #00D2FF;
    }
    .time-tag {
        background: linear-gradient(90deg, #FF4B2B, #FF416C);
        padding: 4px 12px;
        border-radius: 6px;
        font-size: 0.85em;
        font-weight: bold;
        display: inline-block;
        margin-top: 8px;
    }
    .day-header {
        color: #FFD700 !important;
        font-size: 1.8em;
        font-weight: bold;
        margin-bottom: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>🌸 일본 맞춤형 여행 코스 마스터 🏯</h1>", unsafe_allow_html=True)
st.write("---")

# 🛠️ 여행 데이터베이스 (도쿄, 오사카, 후쿠오카)
travel_db = {
    "오사카 & 교토 (Osaka/Kyoto) 🐙": {
        "1일차": {"title": "오사카 도착 & 먹방 투어", "places": [
            {"name": "도톤보리", "time": "3시간", "img": "https://images.unsplash.com/photo-1605649424854-7071994fe29a?w=500", "desc": "글리코상 앞에서 인증샷 찍고 타코야키 정복!"},
            {"name": "우메다 공중정원", "time": "1.5시간", "img": "https://images.unsplash.com/photo-1590252613531-1823933c090e?w=500", "desc": "오사카 도심의 화려한 야경을 360도로 감상"}
        ]},
        "2일차": {"title": "환상의 세계, USJ", "places": [
            {"name": "유니버설 스튜디오 재팬", "time": "전일", "img": "https://images.unsplash.com/photo-1621252179027-94459d278660?w=500", "desc": "마리오 월드와 해리포터 존은 필수 코스!"},
            {"name": "신세카이 쿠시카츠 거리", "time": "2시간", "img": "https://images.unsplash.com/photo-1618585933663-886f32230113?w=500", "desc": "하루의 마무리는 바삭한 튀김 꼬치와 맥주로!"}
        ]},
        "3일차": {"title": "교토 천년의 감성", "places": [
            {"name": "기요미즈데라(청수사)", "time": "2시간", "img": "https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?w=500", "desc": "사계절이 아름다운 절벽 위의 사찰"},
            {"name": "산넨자카/니넨자카", "time": "2시간", "img": "https://images.unsplash.com/photo-1528164344705-4754268799af?w=500", "desc": "교토 특유의 고즈넉한 골목길 산책"},
            {"name": "후시미 이나리 신사", "time": "1.5시간", "img": "https://images.unsplash.com/photo-1563200020-f571b058ed0b?w=500", "desc": "끝없이 이어지는 붉은 토리이 터널"}
        ]},
        "4일차": {"title": "나라 사슴 공원 & 쇼핑", "places": [
            {"name": "나라 공원", "time": "3시간", "img": "https://images.unsplash.com/photo-1571408835012-70b7498c464b?w=500", "desc": "자유롭게 다니는 귀여운 사슴들과의 교감"},
            {"name": "신사이바시 쇼핑몰", "time": "3시간", "img": "https://images.unsplash.com/photo-1563469503417-66a7b212f45c?w=500", "desc": "마지막 기념품과 돈키호테 쇼핑 털기!"}
        ]},
        "5일차": {"title": "온천 힐링 후 귀국", "places": [
            {"name": "소라니와 온천", "time": "3시간", "img": "https://images.unsplash.com/photo-1545569341-9eb8b30979d9?w=500", "desc": "유카타를 입고 즐기는 일본식 테마 온천"},
            {"name": "간사이 공항 면세점", "time": "1.5시간", "img": "https://images.unsplash.com/photo-1542452255191-c85a99f0c5ee?w=500", "desc": "로이스 초콜릿과 도쿄 바나나 구매 타임"}
        ]}
    },
    "후쿠오카 & 큐슈 (Fukuoka/Kyushu) 🍜": {
        "1일차": {"title": "후쿠오카 도심 산책", "places": [
            {"name": "캐널시티 하카타", "time": "2시간", "img": "https://images.unsplash.com/photo-1624286105315-776b25139c89?w=500", "desc": "분수쇼와 복합 쇼핑몰 구경"},
            {"name": "나카스 포장마차 거리", "time": "2시간", "img": "https://images.unsplash.com/photo-1526481280693-3bfa75ac88b1?w=500", "desc": "강변을 따라 즐기는 일본 노점 감성"}
        ]},
        "2일차": {"title": "다자이후 & 온천", "places": [
            {"name": "다자이후 텐만구", "time": "2시간", "img": "https://images.unsplash.com/photo-1582265008064-a690d7945d81?w=500", "desc": "학업의 신을 모시는 아름다운 신사"},
            {"name": "유후인 긴린코 호수", "time": "3시간", "img": "https://images.unsplash.com/photo-1540959733332-eab4deabeeaf?w=500", "desc": "물안개가 피어오르는 몽환적인 호수와 상점가"}
        ]},
        "3일차": {"title": "벳부 지옥 온천 투어", "places": [
            {"name": "가마도 지옥", "time": "1.5시간", "img": "https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?w=500", "desc": "신기한 온천 연기와 맛있는 온천 달걀"},
            {"name": "유메타운 벳부", "time": "2시간", "img": "https://images.unsplash.com/photo-1563469503417-66a7b212f45c?w=500", "desc": "바다 전망의 쇼핑몰에서 여유 즐기기"}
        ]},
        "4일차": {"title": "모모치 해변 & 쇼핑", "places": [
            {"name": "모모치 해변공원", "time": "2시간", "img": "https://images.unsplash.com/photo-1585250005324-9b378031e427?w=500", "desc": "인공 해변과 이국적인 마리존 배경"},
            {"name": "후쿠오카 타워", "time": "1시간", "img": "https://images.unsplash.com/photo-1540959733332-eab4deabeeaf?w=500", "desc": "해변 바로 옆 랜드마크 전망대"}
        ]},
        "5일차": {"title": "마무리 라멘 & 귀국", "places": [
            {"name": "이치란 본점", "time": "1시간", "img": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?w=500", "desc": "후쿠오카 본토의 돈코츠 라멘 맛보기"},
            {"name": "텐진 지하상가", "time": "2시간", "img": "https://images.unsplash.com/photo-1503899036084-c55cdd92da26?w=500", "desc": "마지막 드럭스토어 쇼핑 정복!"}
        ]}
    }
}

# 🎁 선택 영역
col1, col2 = st.columns(2)
with col1:
    region = st.selectbox("어디로 떠나볼까요?", list(travel_db.keys()))
with col2:
    duration = st.selectbox("여행 기간을 골라주세요", ["2박 3일", "3박 4일", "4박 5일"])

# 일수 계산
days_count = int(duration[0]) + 1

if st.button("🚀 나만의 알찬 코스 확인하기"):
    st.balloons()
    selected_region = travel_db[region]
    
    st.markdown(f"## 🍱 {region} - {duration} 추천 일정")
    
    for i in range(1, days_count + 1):
        day_key = f"{i}일차"
        if day_key in selected_region:
            day_info = selected_region[day_key]
            st.markdown(f"<div class='day-container'>", unsafe_allow_html=True)
            st.markdown(f"<div class='day-header'>🗓️ {day_key}: {day_info['title']}</div>", unsafe_allow_html=True)
            
            for place in day_info['places']:
                st.markdown(f"""
                <div class="place-box">
                    <div class="place-text">
                        <h4 style="margin:0; color:#00D2FF !important; font-size:1.3em;">{place['name']}</h4>
                        <p style="margin:8px 0; opacity:0.9;">{place['desc']}</p>
                        <span class="time-tag">⏱ 관람/체험 예상: {place['time']}</span>
                    </div>
                    <img src="{place['img']}" class="place-img">
                </div>
                """, unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")
st.caption("🏮 팁: 일본 여행 전 '트래블로그' 카드를 준비하면 수수료 없이 환전/결제가 가능해요! 💳")
