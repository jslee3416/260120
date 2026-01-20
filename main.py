import streamlit as st
st.title("My first web app!!")
st.write('Hello! Good to see you! :)')
import streamlit as st
import time

# 🎨 페이지 설정
st.set_page_config(page_title="일본 여행 가이드", page_icon="🗼", layout="centered")

# ✨ 가독성을 극대화한 커스텀 CSS
st.markdown("""
    <style>
    /* 전체 배경: 밝지만 눈이 아프지 않은 그라데이션 */
    .stApp {
        background: linear-gradient(135deg, #e0f2f1 0%, #fce4ec 100%);
    }
    
    /* 메인 컨테이너 글씨색 설정 */
    h1, h2, h3, p, span {
        color: #1a237e !important; /* 진한 네이비색으로 가독성 확보 */
    }

    /* 여행 일정 카드: 불투명도 조절 및 테두리 강조 */
    .travel-card {
        background-color: rgba(255, 255, 255, 0.95); /* 거의 불투명한 흰색 */
        padding: 25px;
        border-radius: 20px;
        border-left: 8px solid #ff1744; /* 강렬한 레드 포인트 */
        box-shadow: 0 8px 16px rgba(0,0,0,0.15); /* 그림자를 진하게 */
        margin-bottom: 25px;
    }

    /* 요일 배지: 가독성을 위해 배경색 진하게 */
    .day-badge {
        background-color: #311b92;
        color: white !important;
        padding: 6px 16px;
        border-radius: 12px;
        font-weight: 800;
        display: inline-block;
        margin-bottom: 12px;
        font-size: 0.9em;
    }

    /* 선택박스 및 입력창 가독성 */
    .stSelectbox label {
        color: #1a237e !important;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# 🏯 헤더 섹션
st.markdown("<h1 style='text-align: center;'>🍱 일본 여행 코스 메이커 🍣</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.2em;'>나에게 딱 맞는 여행 일정을 확인해 보세요!</p>", unsafe_allow_html=True)
st.write("---")

# 📅 데이터 (가독성을 위해 핵심 내용 위주 배치)
travel_data = {
    "2박 3일 (도심 핵심 정복) ⚡": {
        "tag": "짧고 굵게! 도쿄 핫플레이스 투어",
        "days": [
            {"day": "Day 1", "title": "도쿄 타워와 야경 🗼", "plan": "나리타 공항 입국 ✈️ → 숙소 체크인 → 신주쿠 도청 전망대 → 오모이데요코초 정복"},
            {"day": "Day 2", "title": "쇼핑과 문화의 거리 🛍️", "plan": "하라주쿠 다케시타 거리 → 시부야 스카이 전망대 → 돈키호테 쇼핑"},
            {"day": "Day 3", "title": "전통 시장 체험 🍣", "plan": "츠키지 장외 시장 (초밥 조식) → 아사쿠사 센소지 사원 → 귀국"}
        ]
    },
    "3박 4일 (테마파크 & 감성) 🎡": {
        "tag": "오사카 먹방과 유니버셜 스튜디오",
        "days": [
            {"day": "Day 1", "title": "글리코상과의 만남 🏃", "plan": "간사이 공항 도착 → 도톤보리 운하 구경 → 타코야끼 & 쿠시카츠 맛집 투어"},
            {"day": "Day 2", "title": "유니버설 스튜디오 🎢", "plan": "USJ 오픈런! 닌텐도 월드 & 해리포터 존 완전 정복"},
            {"day": "Day 3", "title": "교토의 고즈넉함 🍵", "plan": "아라시야마 대나무숲 → 기요미즈데라(청수사) → 기온거리 산책"},
            {"day": "Day 4", "title": "마지막 사슴 공원 🦌", "plan": "나라 사슴 공원 → 나라공원 동대사 → 간사이 공항 이동"}
        ]
    },
    "4박 5일 (일본 완전 정복) 🗺️": {
        "tag": "도쿄 근교와 온천 힐링 여행",
        "days": [
            {"day": "Day 1", "title": "도쿄 중심가 산책 🍜", "plan": "긴자 백화점 구경 → 이치란 라멘 먹방 → 롯폰기 힐즈 야경"},
            {"day": "Day 2", "title": "디즈니랜드의 마법 ✨", "plan": "도쿄 디즈니랜드에서 하루 종일 환상의 시간 보내기"},
            {"day": "Day 3", "title": "가마쿠라 바다 여행 🌊", "plan": "에노덴 열차 타기 → 가마쿠라 고교 앞(슬램덩크 배경지) → 에노시마 섬"},
            {"day": "Day 4", "title": "하코네 온천 힐링 ♨️", "plan": "하코네 로프웨이 체험 → 아시노코 호수 유람선 → 온천 료칸 숙박"},
            {"day": "Day 5", "title": "마지막 기념품 쇼핑 🎁", "plan": "우에노 공원 산책 → 아메요코 시장 기념품 구매 → 나리타 공항"}
        ]
    }
}

# 🎁 인터랙션 영역
with st.container():
    st.markdown("### 🗓️ 여행 일정을 선택하세요")
    choice = st.selectbox("", list(travel_data.keys()))

if st.button("🚀 여행 일정 생성하기"):
    with st.status("🗺️ 최적의 루트를 계산하고 있습니다...", expanded=True) as status:
        st.write("📍 주요 명소 확인 중...")
        time.sleep(0.6)
        st.write("🍱 맛집 리스트업 중...")
        time.sleep(0.6)
        st.write("🏨 숙소 위치 분석 중...")
        time.sleep(0.6)
        status.update(label="✅ 코스 생성 완료!", state="complete", expanded=False)
    
    st.balloons()
    
    res = travel_data[choice]
    st.markdown(f"## 🎌 {choice}")
    st.markdown(f"🚩 **여행 컨셉:** `{res['tag']}`")
    st.write("")

    for item in res['days']:
        st.markdown(f"""
        <div class="travel-card">
            <div class="day-badge">{item['day']}</div>
            <h3 style='margin-top:0;'>{item['title']}</h3>
            <p style='font-size: 1.15em; line-height: 1.6;'>{item['plan']}</p>
        </div>
        """, unsafe_allow_html=True)

    st.success("📝 **체크리스트:** 여권, 돼지코(110V), 구글 맵, 그리고 설레는 마음! ❤️")

# 🌈 푸터
st.markdown("---")
st.markdown("<p style='text-align: center; color: #7f8c8d !important;'>© 2024 Japan Travel Guide. Enjoy your trip! 🌸</p>", unsafe_allow_html=True)
