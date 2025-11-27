# 02_⚙️EnvironmentSetup.py

# ---------------------------------------------------
# Import module
# ---------------------------------------------------
import streamlit as st

# ---------------------------------------------------
# Get session state
# ---------------------------------------------------
api_key = st.session_state.get("api_key", "")
repository_url = st.session_state.get("repository_url", "")

# ---------------------------------------------------
# Sidebar(API,URL input)
# ---------------------------------------------------
st.sidebar.title("Input")
api_key = st.sidebar.text_input("GPT/Gemini API token", value=api_key, type="password", disabled=True)
repository_url = st.sidebar.text_input("Github repository url", value=repository_url, disabled=True)

# ---------------------------------------------------
# Page
# ---------------------------------------------------
if not (api_key and repository_url):
    st.error("API Token 과 GitHub URL를 입력해야 이 페이지를 이용할 수 있습니다.")
    st.stop()

st.title("Repositorie Radar")
st.write("GitHub 저장소를 자동 분석하는 웹 기반 오픈소스 탐색 도구입니다.")

st.header("⚙️Environment Setup")
# 아래 2줄은 디버깅 용입니다 api, url 변수 활용 하세요(이 줄은 지우시고요)
st.write("api_key : " + api_key)
st.write("repository_url : " + repository_url)
