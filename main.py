import streamlit as st
st.title("My first web app!!")
st.write('Hello! Good to see you! :)')
import streamlit as st
import time

# 🎨 페이지 설정
st.set_page_config(page_title="일본 여행 마스터", page_icon="🗾", layout="wide")

# ✨ 고대비 & 고효율 레이아웃 CSS
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
        padding: 30px;
        border-radius: 25px;
        border: 1px solid rgba(255, 255, 255, 0.15);
        margin-bottom: 40px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }
    .place-box {
        display: flex;
        align-items: center;
        background: rgba(0, 0, 0, 0.6);
        margin: 15px 0;
        padding: 20px;
        border-radius: 18px;
        border-left: 6px solid #00D2FF;
    }
    .place-text {
        flex: 1;
        padding-right: 25px;
    }
    .place-img {
        width: 220px;
        height: 140px;
        object-fit: cover;
        border-radius: 12px;
        border: 2px solid #00D2FF;
    }
    .time-tag {
        background: linear-gradient(90deg, #FF4B2B, #FF416C);
        padding: 5px 15px;
        border-radius: 8px;
        font-size: 0.9em;
        font-weight: bold;
        display: inline-block;
        margin-top: 10px;
    }
    .day-header {
        color: #FFD700 !important;
        font-size: 2.2em;
        font-weight: bold;
        margin-bottom: 20px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>🗺️ 알찬 4박 5일 일본 여행 코스 🏯</h1>", unsafe_allow_html=True)
st.write("---")

# 🛠️ 데이터베이스 (하루 2~3곳, 동선 최적화)
travel_db = {
    "도쿄 (Tokyo) 🗼": {
        "1일차": {"title": "시부야 & 신주쿠 힙스터 코스", "places": [
            {"name": "시부야 스카이", "time": "1.5시간", "img": "https://images.unsplash.com/photo-1542051841857-5f90071e7989?w=500", "desc": "도쿄에서 가장 핫한 루프탑 전망대"},
            {"name": "하라주쿠 다케시타 거리", "time": "2시간", "img": "https://images.unsplash.com/photo-1570111974158-958087962478?w=500", "desc": "일본의 독특한 패션과 디저트 천국"},
            {"name": "신주쿠 오모이데요코초", "time": "2시간", "img": "https://images.unsplash.com/photo-1551641506-ee5bf4cb45f1?w=500", "desc": "좁은 골목 속 일본식 이자카야 감성"}
        ]},
        "2일차": {"title": "전통과 현대의 조화", "places": [
            {"name": "아사쿠사 센소지", "time": "2시간", "img": "https://images.unsplash.com/photo-1545569341-9eb8b30979d9?w=500", "desc": "거대한 제등 앞에서 인생샷 찍기"},
            {"name": "도쿄 스카이트리", "time": "1.5시간", "img": "https://images.unsplash.com/photo-1513407030348-c983a97b98d8?w=500", "desc": "세계 최고의 높이를 자랑하는 전파탑"},
            {"name": "아키하바라 전자상가", "time": "3시간", "img": "https://images.unsplash.com/photo-1565355026410-0967387273ae?w=500", "desc": "애니메이션, 게임 덕후들의 성지"}
        ]},
        "3일차": {"title": "테마파크 올인 데이", "places": [
            {"name": "도쿄 디즈니랜드/씨", "time": "8시간", "img": "https://images.unsplash.com/photo-1505993597083-3bd19fb75e57?w=500", "desc": "꿈과 희망의 마법 세계에서 하루 종일!"},
            {"name": "익스피어리 쇼핑몰", "time": "2시간", "img": "https://images.unsplash.com/photo-1567427017947-545c5f8d16ad?w=500", "desc": "디즈니랜드 옆 화려한 쇼핑 단지"}
        ]},
        "4일차": {"title": "바다와 슬램덩크 가마쿠라", "places": [
            {"name": "가마쿠라 고교앞", "time": "1시간", "img": "https://images.unsplash.com/photo-1585250005324-9b378031e427?w=500", "desc": "슬램덩크 오프닝의 바로 그 건널목"},
            {"name": "에노시마 섬", "time": "3시간", "img": "https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?w=500", "desc": "아름다운 바다뷰와 신비로운 동굴 탐험"},
            {"name": "고토쿠인 대불", "time": "1시간", "img": "https://images.unsplash.com/photo-1590252613531-1823933c090e?w=500", "desc": "거대한 야외 청동 불상 관람"}
        ]},
        "5일차": {"title": "도심 힐링과 쇼핑 마무리", "places": [
            {"name": "우에노 공원", "time": "2시간", "img": "https://images.unsplash.com/photo-1583098357022-d049753e834b?w=500", "desc": "박물관과 미술관이 모여있는 도심 폐"},
            {"name": "아메요코 시장", "time": "2시간", "img": "https://images.unsplash.com/photo-1503899036084-c55cdd92da26?w=500", "desc": "시장 음식 먹방과 기념품 쇼핑"}
        ]}
    }
}

# 🎁 필터 선택 영역
region = st.selectbox("지역을 선택하세요", list(travel_db.keys()))
duration = st.selectbox("일정을 선택하세요", ["2박 3일", "3박 4일", "4박 5일"])

days_count = int(duration[0]) + 1 if "박" in duration else 5 # 박 수 + 1일

if st.button("🚀 꽉 찬 여행 코스 생성!"):
    st.balloons()
    selected_data = travel_db[region]
    
    for i in range(1, days_count + 1):
        day_key = f"{i}일차"
        if day_key in selected_data:
            day_info = selected_data[day_key]
            st.markdown(f"<div class='day-container'>", unsafe_allow_html=True)
            st.markdown(f"<div class='day-header'>🗓️ {day_key}: {day_info['title']}</div>", unsafe_allow_html=True)
            
            for place in day_info['places']:
                st.markdown(f"""
                <div class="place-box">
                    <div class="place-text">
                        <h4 style="margin:0; color:#00D2FF !important; font-size:1.4em;">{place['name']}</h4>
                        <p style="margin:10px 0; font-size:1.1em; opacity:0.8;">{place['desc']}</p>
                        <span class="time-tag">⏱ 권람 예상: {place['time']}</span>
                    </div>
                    <img src="{place['place-img' if 'place-img' in place else 'img']}" class="place-img">
                </div>
                """, unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("<p style='text-align: center; opacity: 0.5;'>✈️ 이동 시간은 대중교통 기준으로 약 30분~1시간 내외로 구성된 최적 동선입니다.</p>", unsafe_allow_html=True)
