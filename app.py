import streamlit as st
import pandas as pd

# CSVファイルを読み込む
df = pd.read_csv('problems.csv')

# 問題を選択するためのセレクトボックス
selected_index = st.selectbox("問題を選択:", df.index)

# 選択された問題の詳細を表示
selected_problem = df.iloc[selected_index]
st.image(selected_problem['image_path'], caption='図形問題の画像', width=200)
st.write(selected_problem['description'])

# 回答入力欄
answer = st.text_input("あなたの回答を入力してください:")

# 回答ボタン
if st.button('回答'):
    if answer == selected_problem['answer']:
        st.success("正解です！")
        st.write(f"説明: {selected_problem['answer_description']}")
    else:
        st.error("間違い。もう一度トライしてみてください。")

# ギブアップボタン
if st.button('ギブアップ'):
    st.write(f"正解は: {selected_problem['answer']}")
    st.write(f"説明: {selected_problem['answer_description']}")