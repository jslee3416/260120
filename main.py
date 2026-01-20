import streamlit as st
st.title("My first web app!!")
st.write('Hello! Good to see you! :)')
import streamlit as st
import time

# 🎨 페이지 설정
st.set_page_config(page_title="일본 여행 가이드", page_icon="🏮", layout="centered")

# ✨ 다크 테마 기반의 고대비 커스텀 CSS (툴팁 포함)
st.markdown("""
    <style>
    /* 전체 배경: 어두운 네이비와 보라색 그라데이션 */
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

    /* 툴팁 컨테이너 */
    .tooltip {
        position: relative;
        display: inline-block;
        cursor: help; /* 도움말 커서로 변경하여 툴팁이 있음을 암시 */
        border-bottom: 1px dotted rgba(255,255,255,0.5); /* 밑줄 추가 */
    }

    /* 툴팁 내용 (기본 숨김) */
    .tooltip .tooltiptext {
        visibility: hidden;
        width: 250px; /* 툴팁 너비 */
        background-color: rgba(0,0,0,0.8);
        color: #fff;
        text-align: center;
        border-radius: 6px;
        padding: 10px;
        position: absolute;
        z-index: 1000; /* 다른 요소 위에 표시 */
        bottom: 125%; /* 요소 위로 띄움 */
        left: 50%;
        margin-left: -125px; /* 중앙 정렬 */
        opacity: 0;
        transition: opacity 0.3s;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        font-size: 0.9em;
        line-height: 1.4;
    }
    
    /* 툴팁 이미지 */
    .tooltip .tooltiptext img {
        max-width: 100%;
        height: auto;
        border-radius: 5px;
        margin-bottom: 5px;
    }

    /* 툴팁 화살표 */
    .tooltip .tooltiptext::after {
        content: "";
        position: absolute;
        top: 100%;
        left: 50%;
        margin-left: -5px;
        border-width: 5px;
        border-style: solid;
        border-color: rgba(0,0,0,0.8) transparent transparent transparent;
    }

    /* 마우스 오버 시 툴팁 표시 */
    .tooltip:hover .tooltiptext {
        visibility: visible;
        opacity: 1;
    }
    
    /* Streamlit 기본 Selectbox 배경색 변경 */
    .stSelectbox > div > div {
        background-color: #1a1a2e !important;
        border-color: rgba(255, 255, 255, 0.3) !important;
        color: white !important;
    }
    .stSelectbox > div > div > div > div {
        color: white !important;
    }
    .stSelectbox > div > div > div > svg { /* 드롭다운 화살표 색상 */
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 🏯 헤더 섹션 (이모지와 네온 컬러 조합)
st.markdown("<h1 style='text-align: center; color: #E94560 !important;'>🌠 일본 여행 코스 마스터 🌠</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.2em; opacity: 0.9;'>어두운 곳에서도 선명하게 보이는 최적의 여행 가이드</p>", unsafe_allow_html=True)
st.write("---")

# 📅 여행 데이터 (가독성 높은 이모지 배치)
# 각 장소에 대한 정보 추가: 'image' (사진 URL), 'time' (예상 관람 시간)
travel_data = {
    "2박 3일 (도심 핵심 정복) ⚡": {
        "tag": "#도쿄 #쇼핑 #야경",
        "days": [
            {"day": "DAY 1", "title": "도쿄의 화려한 밤 🗼", "plan": [
                {"name": "나리타 도착", "info": "✈️ 도쿄의 관문!", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Narita_International_Airport_Terminal_1.jpg/800px-Narita_International_Airport_Terminal_1.jpg", "time": "입국 수속 1~2시간"},
                {"name": "신주쿠/시부야 야경", "info": "✨ 도쿄의 상징적인 밤 풍경", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Shibuya_Scramble_Crossing_in_2019.jpg/800px-Shibuya_Scramble_Crossing_in_2019.jpg", "time": "2~3시간"},
                {"name": "라멘 맛집 투어", "info": "🍜 일본의 대표 먹거리", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Shoyu_Ramen_at_Sekiya_Restaurant.jpg/800px-Shoyu_Ramen_at_Sekiya_Restaurant.jpg", "time": "1시간"}
            ]},
            {"day": "DAY 2", "title": "서브컬처와 쇼핑 🛍️", "plan": [
                {"name": "아키하바라 덕질 투어", "info": "🎮 애니메이션, 게임의 성지", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Akihabara_at_night.jpg/800px-Akihabara_at_night.jpg", "time": "3~4시간"},
                {"name": "긴자 쇼핑 거리", "info": "💎 명품 브랜드와 백화점", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Ginza_Street_in_Tokyo.jpg/800px-Ginza_Street_in_Tokyo.jpg", "time": "2~3시간"},
                {"name": "도쿄 타워 인증샷", "info": "🗼 도쿄의 랜드마크", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Tokyo_Tower_2008.JPG/800px-Tokyo_Tower_2008.JPG", "time": "1~2시간"}
            ]},
            {"day": "DAY 3", "title": "전통과 마무리 🍣", "plan": [
                {"name": "아사쿠사 센소지 탐방", "info": "⛩️ 도쿄의 가장 오래된 절", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Sensoji_Temple_Tokyo_2007.jpg/800px-Sensoji_Temple_Tokyo_2007.jpg", "time": "2시간"},
                {"name": "스시 오마카세", "info": "🍣 신선한 제철 해산물!", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Sushi_set_with_various_nigiri.jpg/800px-Sushi_set_with_various_nigiri.jpg", "time": "1~1.5시간"},
                {"name": "면세점 털기 후 귀국", "info": "🎁 마지막 쇼핑 찬스", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Narita_airport_duty_free.jpg/800px-Narita_airport_duty_free.jpg", "time": "1시간"}
            ]}
        ]
    },
    "3박 4일 (테마파크 & 감성) 🎡": {
        "tag": "#오사카 #교토 #유니버설",
        "days": [
            {"day": "DAY 1", "title": "글리코상 하이파이브 🏃", "plan": [
                {"name": "간사이 공항", "info": "✈️ 오사카 여행 시작", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Kansai_International_Airport_Terminal_1.jpg/800px-Kansai_International_Airport_Terminal_1.jpg", "time": "입국 수속 1~2시간"},
                {"name": "도톤보리 먹방", "info": "🦀 화려한 간판과 맛집 천국", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Dotonbori_at_night.jpg/800px-Dotonbori_at_night.jpg", "time": "3~4시간"},
                {"name": "돈키호테 털기", "info": "🛒 없는 게 없는 쇼핑 성지", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Don_Quijote_Dotonbori.jpg/800px-Don_Quijote_Dotonbori.jpg", "time": "1~2시간"}
            ]},
            {"day": "DAY 2", "title": "환상의 세계로 🎢", "plan": [
                {"name": "유니버설 스튜디오 재팬", "info": "🌍 마리오, 해리포터!", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Universal_Studios_Japan_entrance.jpg/800px-Universal_Studios_Japan_entrance.jpg", "time": "하루 종일 (8시간 이상)"}
            ]},
            {"day": "DAY 3", "title": "천년의 수도 교토 🍵", "plan": [
                {"name": "기요미즈데라 산책", "info": "🏯 교토의 아름다운 사찰", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Kiyomizu-dera%2C_Kyoto.jpg/800px-Kiyomizu-dera%2C_Kyoto.jpg", "time": "2~3시간"},
                {"name": "금각사", "info": "✨ 황금빛 찬란한 절", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/Kinkakuji_Golden_Pavilion.jpg/800px-Kinkakuji_Golden_Pavilion.jpg", "time": "1.5시간"},
                {"name": "기온거리", "info": "🌸 게이샤를 만날 수 있는 곳", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Gion_Kyoto_Japan.jpg/800px-Gion_Kyoto_Japan.jpg", "time": "1~2시간"}
            ]},
            {"day": "DAY 4", "title": "사슴과 작별 🦌", "plan": [
                {"name": "나라 사슴 공원", "info": "🦌 자유롭게 다니는 사슴들", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Nara_Park_deer.jpg/800px-Nara_Park_deer.jpg", "time": "2~3시간"},
                {"name": "나라 대불", "info": "🗿 거대한 불상이 있는 동대사", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Todai-ji_Great_Buddha.jpg/800px-Todai-ji_Great_Buddha.jpg", "time": "1~1.5시간"},
                {"name": "간사이 공항 이동", "info": "✈️ 즐거웠던 오사카 여행 안녕!", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Kansai_International_Airport_Terminal_1.jpg/800px-Kansai_International_Airport_Terminal_1.jpg", "time": "출국 수속 2시간"}
            ]}
        ]
    },
    "4박 5일 (완전 정복 힐링) 🗺️": {
        "tag": "#도쿄근교 #온천 #여유",
        "days": [
            {"day": "DAY 1", "title": "도쿄 시내 안착 🍱", "plan": [
                {"name": "긴자 백화점", "info": "🛍️ 도쿄의 쇼핑 중심지", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Ginza_Street_in_Tokyo.jpg/800px-Ginza_Street_in_Tokyo.jpg", "time": "2~3시간"},
                {"name": "이치란 라멘", "info": "🍜 혼밥 성지, 중독성 강한 맛", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Ichiran_Ramen_Shinjuku_Tokyo.jpg/800px-Ichiran_Ramen_Shinjuku_Tokyo.jpg", "time": "1시간"},
                {"name": "롯폰기 힐즈 야경", "info": "🌃 도쿄 타워가 보이는 전망대", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/Roppongi_Hills_Mori_Tower_Tokyo_at_dusk.jpg/800px-Roppongi_Hills_Mori_Tower_Tokyo_at_dusk.jpg", "time": "1.5~2시간"}
            ]},
            {"day": "DAY 2", "title": "꿈과 희망의 나라 ✨", "plan": [
                {"name": "디즈니씨(DisneySea)", "info": "🧜‍♀️ 환상적인 해상 테마파크", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Tokyo_DisneySea.jpg/800px-Tokyo_DisneySea.jpg", "time": "하루 종일 (8시간 이상)"}
            ]},
            {"day": "DAY 3", "title": "가마쿠라 바다 열차 🌊", "plan": [
                {"name": "에노덴 열차", "info": "🚃 바다를 따라 달리는 감성 기차", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Enoshima_Electric_Railway_Type_1000.jpg/800px-Enoshima_Electric_Railway_Type_1000.jpg", "time": "이동 포함 3~4시간"},
                {"name": "슬램덩크 배경지", "info": "🏀 만화 속 명장면 속으로", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/Kamakurakoko-mae_Station_level_crossing.jpg/800px-Kamakurakoko-mae_Station_level_crossing.jpg", "time": "30분~1시간"},
                {"name": "에노시마 섬", "info": "🏝️ 전망대와 신사, 바다뷰", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Enoshima_Island%2C_Fujisawa_Japan.jpg/800px-Enoshima_Island%2C_Fujisawa_Japan.jpg", "time": "2~3시간"}
            ]},
            {"day": "DAY 4", "title": "하코네 온천 휴식 ♨️", "plan": [
                {"name": "하코네 로프웨이", "info": "🚠 후지산과 화산 지대 조망", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/Hakone_Ropeway.jpg/800px-Hakone_Ropeway.jpg", "time": "1~1.5시간"},
                {"name": "아시노코 호수 유람선", "info": "🚢 해적선 타고 호수 구경", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Hakone_pirate_ship_on_Lake_Ashino_2017.jpg/800px-Hakone_pirate_ship_on_Lake_Ashino_2017.jpg", "time": "1시간"},
                {"name": "료칸 가이세키", "info": "🧖‍♀️ 일본 전통 온천과 만찬", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Kaiseki_Ryori_in_Japan.jpg/800px-Kaiseki_Ryori_in_Japan.jpg", "time": "저녁 식사 및 휴식"}
            ]},
            {"day": "DAY 5", "title": "마지막 장보기 🎁", "plan": [
                {"name": "우에노 아메요코 시장", "info": "🛍️ 활기찬 전통 시장, 먹거리", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Ameyoko_Market.jpg/800px-Ameyoko_Market.jpg", "time": "2~3시간"},
                {"name": "나리타 공항", "info": "✈️ 다음 여행을 기약하며", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Narita_International_Airport_Terminal_1.jpg/800px-Narita_International_Airport_Terminal_1.jpg", "time": "출국 수속 2시간"}
            ]}
        ]
    }
}

# 🎁 선택 영역
st.markdown("### 🗓️ 여행 기간을 선택하세요")
choice = st.selectbox("", list(travel_data.keys()), label_visibility="collapsed")

if st.button("✨ 나만의 여행 코스 보기 ✨"):
    # 로딩 애니메이션
    with st.status("🗺️ 최적의 루트를 계산하고 있습니다...", expanded=True) as status:
        st.write("📍 주요 명소 확인 중...")
        time.sleep(0.6)
        st.write("📸 추천 포토존 탐색 중...")
        time.sleep(0.6)
        st.write("⏰ 예상 관람 시간 산정 중...")
        time.sleep(0.6)
        status.update(label="✅ 코스 생성 완료!", state="complete", expanded=False)
    
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
            <ul style='list-style-type: none; padding-left: 0;'>
        """, unsafe_allow_html=True)
        
        for place in item['plan']:
            st.markdown(f"""
                <li style='margin-bottom: 10px;'>
                    <span class='tooltip'>
                        <span class='highlight-text'>📸 {place['name']}</span>
                        <span class='tooltiptext'>
                            <img src='{place['img']}' alt='{place['name']}'/>
                            <strong>{place['name']}</strong><br/>
                            <small>{place['info']}</small><br/>
                            <span style='color: #00D2FF; font-weight: bold;'>⏰ 예상: {place['time']}</span>
                        </span>
                    </span>
                </li>
            """, unsafe_allow_html=True)
        st.markdown("</ul></div>", unsafe_allow_html=True)

    st.success("🎫 모든 일정은 현지 사정에 따라 변경될 수 있으니 구글 맵을 꼭 확인하세요!")

# 🌈 푸터
st.markdown("---")
st.markdown("<p style='text-align: center; opacity: 0.6;'>🏮 본 프로그램은 일본 여행 진로 교육용 예제입니다. 즐거운 상상을 시작해보세요! 🌸</p>", unsafe_allow_html=True)
