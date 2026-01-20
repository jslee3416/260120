import streamlit as st
st.title("My first web app!!")
st.write('Hello! Good to see you! :)')
import streamlit as st
import time

# 🎨 페이지 설정
st.set_page_config(page_title="일본 여행 가이드", page_icon="🏮", layout="centered")

# ✨ 다크 테마 기반의 고대비 커스텀 CSS
st.markdown("""
    <style>
    /* 전체 배경: 어두운 네이비와 보라색 그라데이션으로 시력 보호 및 대비 강화 */
    .stApp {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
    }
    
    /* 모든 텍스트 기본색을 흰색으로 강제 설정 */
    h1, h2, h3, p, span, div, label {
        color: #ffffff !important;
    }

    /* 여행 일정 카드: 어두운 배경과 대비되는 약간 밝은 박스 */
    .travel-card {
        background-color: rgba(255, 255, 255, 0.1); /* 반투명한 흰색 레이어 */
        padding: 25px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-left: 8px solid #E94560; /* 네온 핑크 포인트 */
        box-shadow: 0 10px 30px rgba(0,0,0,0.5); 
        margin-bottom: 25px;
        backdrop-filter: blur(10px); /* 배경 흐림 효과로 고급스러움 추가 */
    }

    /* 요일 배지: 눈에 확 띄는 형광색 */
    .day-badge {
        background-color: #E94560;
        color: white !important;
        padding: 5px 15px;
        border-radius: 8px;
        font-weight: 800;
        display: inline-block;
        margin-bottom: 12px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* 강조 텍스트 (제목 등) */
    .highlight-text {
        color: #00D2FF !important; /* 형광 하늘색 */
        font-weight: bold;
    }

    /* 선택창(Selectbox) 스타일 조정 */
    .stSelectbox div[data-baseweb="select"] {
        background-color: #1a1a2e !important;
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 🏯 헤더 섹션 (이모지와 네온 컬러 조합)
st.markdown("<h1 style='text-align: center; color: #E94560 !important;'>🌠 일본 여행 코스 마스터 🌠</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.2em; opacity: 0.9;'>어두운 곳에서도 선명하게 보이는 최적의 여행 가이드</p>", unsafe_allow_html=True)
st.write("---")

# 📅 여행 데이터 (가독성 높은 이모지 배치)
travel_data = {
    "2박 3일 (도심 핵심 정복) ⚡": {
        "tag": "#도쿄 #쇼핑 #야경",
        "days": [
            {"day": "DAY 1", "title": "도쿄의 화려한 밤 🗼", "plan": "나리타 도착 → <span class='highlight-text'>신주쿠/시부야</span> 야경 감상 → 라멘 맛집 투어"},
            {"day": "DAY 2", "title": "서브컬처와 쇼핑 🛍️", "plan": "<span class='highlight-text'>아키하바라</span> 덕질 투어 → 긴자 쇼핑 거리 → 도쿄 타워 인증샷"},
            {"day": "DAY 3", "title": "전통과 마무리 🍣", "plan": "아사쿠사 센소지 탐방 → 스시 오마카세 → 면세점 털기 후 귀국"}
        ]
    },
    "3박 4일 (테마파크 & 감성) 🎡": {
        "tag": "#오사카 #교토 #유니버설",
        "days": [
            {"day": "DAY 1", "title": "글리코상 하이파이브 🏃", "plan": "간사이 공항 → <span class='highlight-text'>도톤보리</span> 먹방 → 돈키호테 털기"},
            {"day": "DAY 2", "title": "환상의 세계로 🎢", "plan": "<span class='highlight-text'>유니버설 스튜디오 재팬</span> 올인 (마리오 카트 필수!)"},
            {"day": "DAY 3", "title": "천년의 수도 교토 🍵", "plan": "기요미즈데라 산책 → 금각사 → 기온거리에서 인생샷"},
            {"day": "DAY 4", "title": "사슴과 작별 🦌", "plan": "나라 사슴 공원 → 나라 대불 정복 → 간사이 공항 이동"}
        ]
    },
    "4박 5일 (완전 정복 힐링) 🗺️": {
        "tag": "#도쿄근교 #온천 #여유",
        "days": [
            {"day": "DAY 1", "title": "도쿄 시내 안착 🍱", "plan": "숙소 체크인 → 하라주쿠 다케시타 거리 → 메이지 신궁"},
            {"day": "DAY 2", "title": "꿈과 희망의 나라 ✨", "plan": "<span class='highlight-text'>디즈니씨(DisneySea)</span> 탐방 및 퍼레이드 관람"},
            {"day": "DAY 3", "title": "가마쿠라 바다 열차 🌊", "plan": "에노덴 열차 → <span class='highlight-text'>슬램덩크 배경지</span> 인증샷 → 해변 산책"},
            {"day": "DAY 4", "title": "하코네 온천 휴식 ♨️", "plan": "로프웨이 타고 화산 구경 → 호수 유람선 → 고급 료칸 가이세키"},
            {"day": "DAY 5", "title": "마지막 장보기 🎁", "plan": "우에노 아메요코 시장 → 로컬 맛집 → 아쉬운 작별"}
        ]
    }
}

# 🎁 선택 영역
st.markdown("### 🗓️ 여행 기간을 선택하세요")
choice = st.selectbox("", list(travel_data.keys()), label_visibility="collapsed")

if st.button("✨ 나만의 여행 코스 보기 ✨"):
    # 로딩 애니메이션
    msg = st.empty()
    for i in range(3):
        msg.markdown(f"### ✈️ 비행기 준비 중{'.' * (i+1)}")
        time.sleep(0.4)
    msg.empty()
    
    st.balloons()
    
    res = travel_data[choice]
    st.markdown(f"## 🏁 {choice}")
    st.markdown(f"💡 **키워드:** <span class='highlight-text'>{res['tag']}</span>", unsafe_allow_html=True)
    st.write("")

    for item in res['days']:
        st.markdown(f"""
        <div class="travel-card">
            <div class="day-badge">{item['day']}</div>
            <h3 style='margin-top:0;'>{item['title']}</h3>
            <p style='font-size: 1.1em; line-height: 1.6;'>{item['plan']}</p>
        </div>
        """, unsafe_allow_html=True)

    st.success("🎫 모든 일정은 현지 사정에 따라 변경될 수 있으니 구글 맵을 꼭 확인하세요!")

# 🌈 푸터
st.markdown("---")
st.markdown("<p style='text-align: center; opacity: 0.6;'>🏮 본 프로그램은 일본 여행 진로 교육용 예제입니다. 즐거운 상상을 시작해보세요! 🌸</p>", unsafe_allow_html=True)
