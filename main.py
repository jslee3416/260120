import streamlit as st
st.title("My first web app!!")
st.write('Hello! Good to see you! :)')
import streamlit as st
import time

# 🎨 페이지 설정 (아이콘과 제목)
st.set_page_config(page_title="MBTI 진로 탐색기", page_icon="🌟", layout="centered")

# ✨ 커스텀 CSS로 화려함 더하기
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3em;
        background-color: #FF4B4B;
        color: white;
        font-weight: bold;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #FF8787;
        transform: scale(1.05);
    }
    .mbti-card {
        padding: 20px;
        border-radius: 15px;
        background-color: white;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# 🌈 헤더 섹션
st.title("🌈 MBTI 꿈의 지도 🗺️")
st.subheader("나의 성격에 딱! 맞는 미래 직업을 찾아봐요! ✨")
st.write("---")

# 🎭 MBTI 데이터베이스
mbti_jobs = {
    "ISTJ": {"emoji": "📏", "title": "현실적인 관리자", "jobs": ["회계사", "공무원", "데이터 분석가"], "desc": "철저하고 규칙적인 당신! 질서 정연한 일이 최고예요!"},
    "ISFJ": {"emoji": "🛡️", "title": "용감한 수호자", "jobs": ["간호사", "교사", "사회복지사"], "desc": "타인을 돕는 따뜻한 마음! 배려심 깊은 일이 어울려요!"},
    "INFJ": {"emoji": "🔮", "title": "선의의 옹호자", "jobs": ["상담사", "작가", "심리학자"], "desc": "통찰력이 뛰어난 당신! 사람들의 마음을 치유해봐요!"},
    "INTJ": {"emoji": "🧠", "title": "용의주도한 전략가", "jobs": ["소프트웨어 개발자", "과학자", "전략 기획자"], "desc": "논리적이고 분석적인 당신! 복잡한 문제를 해결해보세요!"},
    "ISTP": {"emoji": "🛠️", "title": "만능 재주꾼", "jobs": ["엔지니어", "파일럿", "프로그래머"], "desc": "손재주가 좋고 적응력이 빨라요! 기술적인 분야가 딱!"},
    "ISFP": {"emoji": "🎨", "title": "호기심 많은 예술가", "jobs": ["디자이너", "작곡가", "사진작가"], "desc": "예술적 감각이 폭발! 당신의 미적 감각을 뽐내보세요!"},
    "INFP": {"emoji": "🧚", "title": "열정적인 중재자", "jobs": ["시인", "예술가", "NGO 활동가"], "desc": "이상주의적인 당신! 세상을 아름답게 만드는 일을 해봐요!"},
    "INTP": {"emoji": "🧪", "title": "논리적인 사색가", "jobs": ["대학교수", "연구원", "철학자"], "desc": "끊임없이 탐구하는 천재! 아이디어를 현실로 만들어봐요!"},
    "ESTP": {"emoji": "⚡", "title": "모험을 즐기는 사업가", "jobs": ["기업가", "스포츠 에이전트", "마케터"], "desc": "행동이 먼저! 스릴 넘치고 변화무쌍한 환경이 좋아요!"},
    "ESFP": {"emoji": "🎉", "title": "자유로운 영혼의 연예인", "jobs": ["연예인", "이벤트 플래너", "승무원"], "desc": "에너지 뿜뿜! 사람들 앞에서 빛나는 주인공이 되어봐요!"},
    "ENFP": {"emoji": "🎈", "title": "재기발랄한 활동가", "jobs": ["크리에이티브 디렉터", "홍보 전문가", "카피라이터"], "desc": "창의력 대장! 자유롭고 즐거운 분위기에서 능력이 발휘돼요!"},
    "ENTP": {"emoji": "💡", "title": "뜨거운 논쟁을 즐기는 변론가", "jobs": ["변호사", "발명가", "정치인"], "desc": "두뇌 회전이 빨라요! 새로운 도전을 즐기는 리더가 되세요!"},
    "ESTJ": {"emoji": "👔", "title": "엄격한 관리자", "jobs": ["경영자", "프로젝트 매니저", "군인"], "desc": "조직의 리더! 체계적이고 확실하게 목표를 달성해요!"},
    "ESFJ": {"emoji": "🤝", "title": "사교적인 외교관", "jobs": ["홍보 담당자", "호텔리어", "초등교사"], "desc": "친절함의 대명사! 사람들과 협동하며 에너지를 얻어요!"},
    "ENFJ": {"emoji": "📢", "title": "정의로운 사회운동가", "jobs": ["정치인", "강연가", "코치"], "desc": "영향력이 큰 리더! 사람들을 이끄는 카리스마가 대단해요!"},
    "ENTJ": {"emoji": "👑", "title": "대담한 통솔자", "jobs": ["CEO", "비즈니스 컨설턴트", "투자 전문가"], "desc": "결단력 최고! 커다란 비전을 실행에 옮기는 힘이 있어요!"},
}

# 🎁 선택 영역
st.info("💡 본인의 MBTI를 선택하고 '진로 탐색하기' 버튼을 눌러보세요!")
choice = st.selectbox("나의 MBTI는?", list(mbti_jobs.keys()))

if st.button("🚀 나의 미래 직업 확인하기! 🚀"):
    with st.spinner('🔮 당신의 미래를 분석 중입니다...'):
        time.sleep(1.5) # 감성적인 로딩 시간
    
    res = mbti_jobs[choice]
    
    # 결과 출력
    st.balloons() # 축하 풍선 효과
    
    st.markdown(f"""
    <div class="mbti-card">
        <h1 style='font-size: 80px;'>{res['emoji']}</h1>
        <h2>{choice}: {res['title']}</h2>
        <p style='font-size: 1.2em; color: #555;'>"{res['desc']}"</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    
    # 추천 직업 리스트
    st.success(f"### 🎯 {choice} 유형에게 추천하는 직업군")
    cols = st.columns(3)
    for idx, job in enumerate(res['jobs']):
        with cols[idx]:
            st.info(f"**{job}**")

# 🌈 하단 푸터
st.markdown("---")
st.caption("✨ 여러분의 꿈을 항상 응원합니다! | MBTI Career Explorer v1.0 🎈")
