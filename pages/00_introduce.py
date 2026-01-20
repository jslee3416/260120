import streamlit as st

# 1. 페이지 설정
st.set_page_config(
    page_title="Marine's Briefing Room",
    page_icon="🔫",
    layout="centered"
)

# 2. 제목 및 인사말
st.title("🛡️ 테란 마린의 자기소개")
st.subheader("“Go, go, go! 작전 개시합니다.”")

# 3. 마린 이미지 추가 (Unsplash 또는 외부 링크 사용)
# 공식 이미지를 직접 제공할 수 없으므로, 테란 마린 느낌의 로봇/SF 이미지를 불러옵니다.
st.image(
    "https://images.unsplash.com/photo-1550745165-9bc0b252726f?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80", 
    caption="준비 완료! (Ready to Rollout!)",
    use_container_width=True
)

# 4. 자기소개 섹션
st.markdown("---")
st.header("👤 프로필")
col1, col2 = st.columns(2)

with col1:
    st.write("**이름:** 테란 마린 (Terran Marine)")
    st.write("**소속:** 테란 연합 (Terran Confederacy)")
    st.write("**주특기:** 가우스 라이플 사격, 스팀팩 복용")

with col2:
    st.write("**계급:** 해병 (Private)")
    st.write("**취미:** 벙커 안에서 수다 떨기")
    st.write("**좌우명:** " "You want a piece of me, boy?" "")

# 5. 기술 스택 (능력치)
st.markdown("---")
st.header("⚔️ 전투 능력치")
st.write("공격력")
st.progress(60)
st.write("방어력")
st.progress(40)
st.write("스팀팩 활용도")
st.progress(95)

# 6. 연락처
st.markdown("---")
st.info("📧 사령부로 연락하기: marine@terran.com")

# 하단 푸터
st.caption("© 2026 Koprulu Sector. All rights reserved.")
