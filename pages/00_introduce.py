import streamlit as st
from PIL import Image

# 1. 웹 페이지 설정
st.set_page_config(page_title="나의 자기소개 페이지", page_icon="👋")

# 2. 사이드바 구성 (연락처 등)
st.sidebar.header("Contact Info")
st.sidebar.text("📧 Email: example@email.com")
st.sidebar.text("🔗 GitHub: github.com/username")

# 3. 메인 화면 구성
st.title("안녕하세요! 반갑습니다. 👋")

# 사진 추가 (이미지 파일이 같은 폴더에 있어야 합니다. 예: profile.jpg)
# 이미지 파일이 없다면 아래 예제 이미지를 사용하거나 주석 처리하세요.
try:
    image = Image.open('profile.jpg')
    st.image(image, width=250, caption='나의 프로필 사진')
except FileNotFoundError:
    st.warning("프로필 이미지('profile.jpg')를 찾을 수 없습니다. 이미지 파일을 같은 폴더에 넣어주세요.")

st.subheader("소개")
st.write("""
여기에 본인에 대한 한 줄 소개를 적어보세요. 
예: "데이터로 세상을 변화시키고 싶은 개발자, 홍길동입니다."
""")

st.markdown("---")

# 4. 탭을 활용한 정보 정리
tab1, tab2, tab3 = st.tabs(["기술 스택", "경력", "취미"])

with tab1:
    st.write("사용 가능한 기술들을 적어주세요.")
    st.code("Python, Streamlit, SQL, TensorFlow")

with tab2:
    st.write("✨ **주요 경력**")
    st.write("- A대학교 컴퓨터공학 전공 (2020 - 2024)")
    st.write("- B사 데이터 분석 인턴 (2023.01 - 2023.06)")

with tab3:
    st.write("저는 이런 것들을 좋아해요!")
    st.write("📸 사진 찍기, ⛰️ 등산, 🎮 게임")

# 5. 간단한 방명록 기능
st.markdown("---")
st.subheader("방명록")
name = st.text_input("이름")
message = st.text_area("메시지")
if st.button("남기기"):
    st.success(f"{name}님, 따뜻한 메시지 감사합니다!")
