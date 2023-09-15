import streamlit as st
import pandas as pd

def show():
    # このページの内容
    df = pd.read_csv('problems.csv')
    selected_index = st.selectbox("問題を選択:", df.index)
    selected_problem = df.iloc[selected_index]
    st.image(selected_problem['image_path'], caption='図形問題の画像', width=200)
    st.write(selected_problem['description'])
    answer = st.text_input("あなたの回答を入力してください:")
    if st.button('回答'):
        if answer == selected_problem['answer']:
            st.success("正解です！")
            st.write(f"説明: {selected_problem['answer_description']}")
        else:
            st.error("間違い。もう一度トライしてみてください。")
    if st.button('ギブアップ'):
        st.write(f"正解は: {selected_problem['answer']}")
        st.write(f"説明: {selected_problem['answer_description']}")
