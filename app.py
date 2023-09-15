import streamlit as st
import problem
import consept
import wazan

PAGES = {
    "問題ページ": problem,
    "アプリのコンセプト": consept,
    "和算について": wazan,
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

page = PAGES[selection]
page.show()
