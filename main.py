import streamlit as st
st.title("My first web app!!")
st.write('Hello! Good to see you! :)')
import streamlit as st
import time

# 🎨 페이지 설정
st.set_page_config(page_title="일본 여행 가이드", page_icon="🗼", layout="centered")

# ✨ 디자인 개선을 위한 커스텀 CSS
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
    }
    
    h1, h2, h3, p, span, div {
        color: #ffffff !important;
    }

    /* 여행 일정 카드 디자인 */
    .travel-card {
        background-color: rgba(255, 255, 255, 0.05);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 20px;
        backdrop-filter: blur(5px);
    }

    /* 장소 아이템 레이아웃 (글씨 + 사진) */
    .place-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: rgba(0, 0, 0, 0.3);
        margin: 10px 0;
        padding: 15px;
        border-radius: 12px;
        border-left: 5px solid #00D2FF;
    }

    .place-info {
        flex: 1;
        padding-right: 15px;
    }

    .place-image {
        width: 120px;
        height: 80px;
        object-fit: cover;
        border-radius: 8px;
        border: 2px solid rgba(255, 255, 255, 0.2);
    }

    .time-badge {
        background-color: #E94560;
        color: white;
        padding: 2px 8px;
        border-radius: 5px;
        font-size: 0.8em;
        font-weight: bold;
    }

    .day-header {
        color: #00D2FF !important;
        font-weight: bold;
        font-size: 1.5em;
        margin-bottom: 10px;
        display: block;
    }
    </style>
    """, unsafe_allow_html=True)

# 🏯 타이틀
st.markdown("<h1 style='text-align: center;'>🏯 일본 여행 마스터 🍱</h1>", unsafe_allow_html=True)
st.write("---")

# 📅 데이터베이스 (사진 URL 포함)
travel_data = {
    "2박 3일 (도쿄 도심) ⚡": [
        {"day": "DAY 1: 도쿄의 밤", "places": [
            {"name": "신주쿠 오모이데요코초", "time": "2시간", "img": "https://images.unsplash.com/photo-1551641506-ee5bf4cb45f1?w=400", "desc": "좁은 골목길의 감성 이자카야 거리"},
            {"name": "시부야 스카이", "time": "1.5시간", "img": "https://images.unsplash.com/photo-1542051841857-5f90071e7989?w=400", "desc": "도쿄 전체가 내려다보이는 루프탑"}
        ]},
        {"day": "DAY 2: 덕후의 성지", "places": [
            {"name": "아키하바라", "time": "4시간", "img": "https://images.unsplash.com/photo-1565355026410-0967387273ae?w=400", "desc": "애니메이션과 전자제품의 메카"},
            {"name": "도쿄 타워", "time": "1시간", "img": "https://images.unsplash.com/photo-1513407030348-c983a97b98d8?w=400", "desc": "도쿄의 영원한 상징"}
        ]}
    ],
    "3박 4일 (오사카 감성) 🎡": [
        {"day": "DAY 1: 오사카 먹방", "places": [
            {"name": "도톤보리", "time": "3시간", "img": "https://images.unsplash.com/photo-1605649424854-7071994fe29a?w=400", "desc": "글리코상과 맛있는 길거리 음식"},
            {"name": "우메다 공중정원", "time": "1시간", "img": "https://images.unsplash.com/photo-1590252613531-1823933c090e?w=400", "desc": "미래지향적인 야경 명소"}
        ]},
        {"day": "DAY 2: 환상의 나라", "places": [
            {"name": "유니버설 스튜디오", "time": "8시간", "img": "https://images.unsplash.com/photo-1621252179027-94459d278660?w=400", "desc": "마리오와 해리포터를 만나는 곳"}
        ]}
    ]
}

# 🎁 선택 영역
choice = st.selectbox("어디로 떠나고 싶으신가요?", list(travel_data.keys()))

if st.button("🌟 추천 코스 확인하기"):
    st.balloons()
    
    for day_info in travel_data[choice]:
        st.markdown(f"<span class='day-header'>{day_info['day']}</span>", unsafe_allow_html=True)
        
        for p in day_info['places']:
            st.markdown(f"""
            <div class="place-container">
                <div class="place-info">
                    <h4 style="margin:0; color:#00D2FF !important;">{p['name']}</h4>
                    <p style="font-size:0.9em; margin:5px 0;">{p['desc']}</p>
                    <span class="time-badge">⏱ 예상 관람: {p['time']}</span>
                </div>
                <img src="{p['img']}" class="place-image">
            </div>
            """, unsafe_allow_html=True)
