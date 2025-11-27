# streamlit_app.py

# ---------------------------------------------------
# Import module
# ---------------------------------------------------
import streamlit as st
import module.github as github
import module.gpt as gpt
import module.gemini as gemini

# ---------------------------------------------------
# Streamlit config
# ---------------------------------------------------
st.set_page_config(
    page_title="Repositorie Radar",
    page_icon=":shark:",
    layout="wide",
)

# ---------------------------------------------------
# Sidebar(API,URL input)
# ---------------------------------------------------
if "api_key" not in st.session_state:
    st.session_state["api_key"] = ""
if "api_type" not in st.session_state:
    st.session_state["api_type"] = ""
if "repository_url" not in st.session_state:
    st.session_state["repository_url"] = ""

st.sidebar.title("Input")
api_key = st.sidebar.text_input("GPT/Gemini API key", value=st.session_state["api_key"], type="password")
repository_url = st.sidebar.text_input("Github repository url", value=st.session_state["repository_url"])

if st.sidebar.button("Save"):
    if gpt.api_check(api_key):
        st.session_state["api_key"] = api_key
        st.session_state["api_type"] = "gpt"
        st.sidebar.success("올바른 API 키(Gpt)")
    elif gemini.api_check(api_key):
        st.session_state["api_key"] = api_key
        st.session_state["api_type"] = "gemini"
        st.sidebar.success("올바른 API 키(Gemini)")
    else:
        st.sidebar.error("잘못된 API 키")
    if github.url_check(repository_url):
        st.session_state["repository_url"] = repository_url
        st.sidebar.success("올바른 Repository 링크")
    else:
        st.sidebar.error("잘못된 Repository 링크")

# ---------------------------------------------------
# Home Page
# ---------------------------------------------------
st.title("Repositorie Radar")
st.write("GitHub 저장소를 자동 분석하는 웹 기반 오픈소스 탐색 도구입니다.")

st.header(" Home")
api_key = st.session_state.get("api_key", "")
repository_url = st.session_state.get("repository_url", "")

# ---------------------------------------------------
# Check input
# ---------------------------------------------------
if api_key and repository_url:
    st.success("GitHub URL과 API Token이 확인되었습니다. 왼쪽 사이드바에서 분석 페이지로 이동하세요!")
else:
    st.error("API Token 과 GitHub URL를 입력해야 합니다.")
