import streamlit as st
st.title("My first web app!!")
st.write('Hello! Good to see you! :)')
import streamlit as st
import time

# 🎨 페이지 설정
st.set_page_config(page_title="일본 여행 플래너", page_icon="🗾", layout="centered")

# ✨ 다크 & 네온 커스텀 CSS
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
    }
    h1, h2, h3, h4, p, span, div, label {
        color: #ffffff !important;
    }
    /* 카드 디자인 */
    .day-card {
        background-color: rgba(255, 255, 255, 0.05);
        padding: 20px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 30px;
        backdrop-filter: blur(10px);
    }
    /* 장소 아이템 레이아웃 */
    .place-box {
        display: flex;
        align-items: center;
        background: rgba(0, 0, 0, 0.4);
        margin: 15px 0;
        padding: 15px;
        border-radius: 15px;
        transition: transform 0.2s;
    }
    .place-box:hover {
        transform: scale(1.02);
        background: rgba(0, 0, 0, 0.6);
    }
    .place-text {
        flex: 1;
        padding-right: 15px;
    }
    .place-img {
        width: 140px;
        height: 100px;
        object-fit: cover;
        border-radius: 12px;
        border: 2px solid #00D2FF;
    }
    .time-tag {
        background: #E94560;
        padding: 3px 10px;
        border-radius: 8px;
        font-size: 0.85em;
        font-weight: bold;
    }
    .day-label {
        color: #00D2FF !important;
        font-size: 1.8em;
        font-weight: bold;
        border-bottom: 2px solid #00D2FF;
        margin-bottom: 15px;
        display: inline-block;
    }
    </style>
    """, unsafe_allow_html=True)

# 🏯 메인 타이틀
st.markdown("<h1 style='text-align: center;'>✈️ 일본 맞춤 여행 플래너 🏯</h1>", unsafe_allow_html=True)
st.write("---")

# 🛠️ 여행 데이터 구성
data = {
    "도쿄 (Tokyo) 🗼": {
        "2박 3일": [
            {"day": "Day 1", "places": [
                {"name": "시부야 스카이", "time": "1.5시간", "img": "https://images.unsplash.com/photo-1542051841857-5f90071e7989?w=400", "desc": "도쿄에서 가장 힙한 전망대!"},
                {"name": "신주쿠 골든가이", "time": "2시간", "img": "https://images.unsplash.com/photo-1551641506-ee5bf4cb45f1?w=400", "desc": "일본 특유의 심야 식당 감성"}
            ]},
            {"day": "Day 2", "places": [
                {"name": "아사쿠사 센소지", "time": "2시간", "img": "https://images.unsplash.com/photo-1545569341-9eb8b30979d9?w=400", "desc": "도쿄에서 가장 큰 전통 사원"},
                {"name": "아키하바라", "time": "3시간", "img": "https://images.unsplash.com/photo-1565355026410-0967387273ae?w=400", "desc": "애니메이션과 게임의 성지"}
            ]}
        ],
        "3박 4일": [
            {"day": "Day 3 추가", "places": [
                {"name": "도쿄 디즈니씨", "time": "8시간", "img": "https://images.unsplash.com/photo-1505993597083-3bd19fb75e57?w=400", "desc": "바다를 테마로 한 환상의 테마파크"}
            ]}
        ]
    },
    "오사카 (Osaka) 🐙": {
        "2박 3일": [
            {"day": "Day 1", "places": [
                {"name": "도톤보리", "time": "3시간", "img": "https://images.unsplash.com/photo-1605649424854-7071994fe29a?w=400", "desc": "글리코상 앞에서 인증샷 필수!"},
                {"name": "오사카성", "time": "1.5시간", "img": "https://images.unsplash.com/photo-1590252613531-1823933c090e?w=400", "desc": "일본의 역사를 느끼는 랜드마크"}
            ]},
            {"day": "Day 2", "places": [
                {"name": "유니버설 스튜디오", "time": "전일", "img": "https://images.unsplash.com/photo-1621252179027-94459d278660?w=400", "desc": "슈퍼 닌텐도 월드는 꼭 가야죠!"}
            ]}
        ],
        "3박 4일": [
            {"day": "Day 3 추가", "places": [
                {"name": "교토 청수사", "time": "3시간", "img": "https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?w=400", "desc": "사계절이 아름다운 교토의 절"}
            ]}
        ]
    }
}

# 🗺️ 사이드바 / 상단 선택 영역
col1, col2 = st.columns(2)
with col1:
    region = st.selectbox("어디로 가고 싶나요?", list(data.keys()))
with col2:
    duration = st.selectbox("며칠 동안 머무나요?", ["2박 3일", "3박 4일", "4박 5일"])

if st.button("✨ 나만의 일정 생성 ✨"):
    with st.spinner("최고의 장소를 선별하고 있습니다..."):
        time.sleep(1)
    
    st.balloons()
    
    # 데이터 가져오기 (예외 처리 포함)
    target_region = data.get(region, {})
    itinerary = target_region.get("2박 3일", []) # 기본 일정
    
    if duration == "3박 4일" or duration == "4박 5일":
        itinerary = itinerary + target_region.get("3박 4일", [])
        
    # 결과 출력
    st.markdown(f"## 🍱 {region} - {duration} 추천 코스")
    
    for day in itinerary:
        st.markdown(f"<div class='day-card'>", unsafe_allow_html=True)
        st.markdown(f"<span class='day-label'>{day['day']}</span>", unsafe_allow_html=True)
        
        for p in day['places']:
            st.markdown(f"""
            <div class="place-box">
                <div class="place-text">
                    <h4 style="margin:0; color:#00D2FF !important;">{p['name']}</h4>
                    <p style="margin:5px 0; opacity:0.8;">{p['desc']}</p>
                    <span class="time-tag">⏱ 관람 예상: {p['time']}</span>
                </div>
                <img src="{p['img']}" class="place-img">
            </div>
            """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# 🌈 하단 가이드
st.info("💡 장소에 마우스를 올리면 살짝 커지는 효과가 있어요! 사진을 보며 여행을 상상해보세요.")
