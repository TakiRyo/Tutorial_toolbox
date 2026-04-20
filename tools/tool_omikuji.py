import random
import streamlit as st


def show():
    st.markdown("# ## おみくじ・占い")
    st.markdown("作った人: taki")

    fortunes = ["大吉", "中吉", "小吉", "吉", "末吉", "凶"]
    lucky_items = ["赤いペン", "ヘッドホン", "青いノート", "小さな鏡", "折りたたみ傘"]

    if st.button("おみくじを引く"):
        fortune = random.choice(fortunes)
        item = random.choice(lucky_items)
        st.success(f"運勢: {fortune}")
        st.info(f"ラッキーアイテム: {item}")
