pip install streamlit
import streamlit as st

# 1. 페이지 설정
st.set_page_config(page_title="나의 자기소개 페이지", page_icon="🍃")

# 2. 사이드바 (선택 사항)
st.sidebar.title("연락처")
st.sidebar.info("📧 이메일: example@email.com")
st.sidebar.info("💻 GitHub: github.com/username")

# 3. 메인 화면 구성
st.title("안녕하세요! 만나서 반가워요 👋")

# 토토로 이미지 추가 (URL 사용)
# 만약 로컬 이미지를 쓰고 싶다면 이미지 파일명을 따옴표 안에 넣으세요.
totoro_url = "https://upload.wikimedia.org/wikipedia/en/0/02/My_Neighbor_Totoro_poster_main_characters.jpg"
st.image(totoro_url, caption="귀여운 토토로와 함께하는 저의 공간입니다!", width=400)

st.header("소개")
st.write("""
안녕하세요! 저는 새로운 기술을 배우고 공유하는 것을 좋아하는 개발자입니다. 
지브리 애니메이션처럼 따뜻하고 재미있는 가치를 만드는 것에 관심이 많아요.
""")

# 4. 간단한 정보 테이블
st.subheader("관심 분야")
col1, col2, col3 = st.columns(3)
with col1:
    st.button("Python")
with col2:
    st.button("Streamlit")
with col3:
    st.button("Data Science")

# 5. 방명록 기능 (간단한 입력창)
st.divider()
name = st.text_input("당신의 성함은 무엇인가요?")
if name:
    st.success(f"{name}님, 방문해 주셔서 감사합니다!  Totoro says Hi! 🍃")
