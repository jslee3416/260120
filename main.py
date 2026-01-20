import streamlit as st
st.title("My first web app!!")
st.write('Hello! Good to see you! :)')
import streamlit as st
import time

# 🎨 페이지 설정
st.set_page_config(page_title="일본 여행 플래너", page_icon="🗾", layout="wide")

# ✨ 다크 & 네온 커스텀 CSS (가독성 강화)
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f0c29 0%, #24243e 100%);
    }
    h1, h2, h3, h4, p, span, div, label {
        color: #ffffff !important;
    }
    /* 일정 카드 스타일 */
    .day-container {
        background-color: rgba(255, 255, 255, 0.07);
        padding: 25px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 25px;
    }
    /* 장소 박스 스타일 */
    .place-box {
        display: flex;
        align-items: center;
        background: rgba(0, 0, 0, 0.5);
        margin: 15px 0;
        padding: 15px;
        border-radius: 15px;
        border-left: 6px solid #00D2FF;
    }
    .place-text {
        flex: 1;
        padding-right: 20px;
    }
    .place-img {
        width: 180px;
        height: 120px;
        object-fit: cover;
        border-radius: 10px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5);
    }
    .time-tag {
        background: #FF4B4B;
        padding: 4px 12px;
        border-radius: 6px;
        font-size: 0.9em;
        font-weight: bold;
    }
    .day-header {
        color: #FFD700 !important;
        font-size: 1.8em;
        font-weight: bold;
        margin-bottom: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# 🏯 타이틀
st.markdown("<h1 style='text-align: center;'>✨ 일본 맞춤형 여행 코스 가이드 ✨</h1>", unsafe_allow_html=True)
st.write("---")

# 🛠️ 여행 데이터베이스 (지역별/일차별 완벽 분리)
travel_db = {
    "도쿄 (Tokyo) 🗼": {
        "1일차": {"title": "도쿄 상륙 & 야경", "places": [{"name": "시부야 스카이", "time": "1.5시간", "img": "https://images.unsplash.com/photo-1542051841857-5f90071e7989?w=500", "desc": "도쿄의 상징적인 스카이라인을 한눈에 담으세요!"}]},
        "2일차": {"title": "덕질 & 전통 탐방", "places": [{"name": "아키하바라", "time": "4시간", "img": "https://images.unsplash.com/photo-1565355026410-0967387273ae?w=500", "desc": "애니메이션, 게임, 피규어의 성지입니다."}]},
        "3일차": {"title": "환상의 디즈니", "places": [{"name": "디즈니랜드", "time": "전일", "img": "https://images.unsplash.com/photo-1505993597083-3bd19fb75e57?w=500", "desc": "꿈과 희망이 넘치는 마법 같은 하루!"}]},
        "4일차": {"title": "근교 힐링 여행", "places": [{"name": "가마쿠라 바다", "time": "5시간", "img": "https://images.unsplash.com/photo-1585250005324-9b378031e427?w=500", "desc": "슬램덩크의 배경지에서 바다 열차를 타보세요."}]},
        "5일차": {"title": "마지막 쇼핑", "places": [{"name": "긴자 거리", "time": "3시간", "img": "https://images.unsplash.com/photo-1503899036084-c55cdd92da26?w=500", "desc": "세련된 백화점과 맛집에서 여행을 마무리하세요."}]}
    },
    "오사카 (Osaka) 🐙": {
        "1일차": {"title": "오사카 먹방 시작", "places": [{"name": "도톤보리", "time": "3시간", "img": "https://images.unsplash.com/photo-1605649424854-7071994fe29a?w=500", "desc": "글리코상 앞에서 타코야키 먹방!"}]},
        "2일차": {"title": "유니버설 스튜디오", "places": [{"name": "USJ", "time": "전일", "img": "https://images.unsplash.com/photo-1621252179027-94459d278660?w=500", "desc": "슈퍼 닌텐도 월드 오픈런은 필수입니다."}]},
        "3일차": {"title": "교토 역사 산책", "places": [{"name": "기요미즈데라", "time": "3시간", "img": "https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?w=500", "desc": "교토에서 가장 아름다운 사찰에서 힐링하세요."}]},
        "4일차": {"title": "사슴과 문화재", "places": [{"name": "나라 사슴공원", "time": "4시간", "img": "https://images.unsplash.com/photo-1571408835012-70b7498c464b?w=500", "desc": "귀여운 사슴들에게 센베 과자를 줘보세요."}]},
        "5일차": {"title": "온천과 공항", "places": [{"name": "소라니와 온천", "time": "3시간", "img": "https://images.unsplash.com/photo-1545569341-9eb8b30979d9?w=500", "desc": "여행의 피로를 풀고 공항으로 향합니다."}]}
    }
}

# 🎁 필터 선택 영역
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        region = st.selectbox("어디로 가고 싶으신가요?", list(travel_db.keys()))
    with col2:
        days_input = st.selectbox("여행 기간을 선택하세요", ["2박 3일", "3박 4일", "4박 5일"])

# 일수 변환 (숫자만 추출)
days_count = int(days_input[0])

if st.button("🚀 추천 코스 생성하기"):
    with st.spinner("전문 가이드가 일정을 짜는 중입니다..."):
        time.sleep(1)
    
    st.balloons()
    
    selected_region_data = travel_db[region]
    
    st.markdown(f"## 🍱 {region} - {days_input} 추천 일정")
    
    # 루프를 통해 선택한 일수만큼 정확히 반복
    for i in range(1, days_count + 1):
        day_key = f"{i}일차"
        if day_key in selected_region_data:
            day_data = selected_region_data[day_key]
            
            st.markdown(f"<div class='day-container'>", unsafe_allow_html=True)
            st.markdown(f"<div class='day-header'>📍 {day_key}: {day_data['title']}</div>", unsafe_allow_html=True)
            
            for place in day_data['places']:
                st.markdown(f"""
                <div class="place-box">
                    <div class="place-text">
                        <h4 style="margin:0; color:#00D2FF !important;">{place['name']}</h4>
                        <p style="margin:8px 0; opacity:0.9;">{place['desc']}</p>
                        <span class="time-tag">⏱ 관람 예상: {place['time']}</span>
                    </div>
                    <img src="{place['img']}" class="place-img">
                </div>
                """, unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")
st.caption("🏮 본 웹앱은 교육용으로 제작되었습니다. 사진 옆 관람 시간을 참고하여 알찬 여행을 계획해 보세요!")
