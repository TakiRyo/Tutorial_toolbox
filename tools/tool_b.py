from io import BytesIO
import streamlit as st
from PIL import Image, ImageOps


def show():
    st.markdown("# ## 画像背景除去・フィルター")
    st.markdown("作った人: taki")

    uploaded = st.file_uploader("画像をアップロード", type=["png", "jpg", "jpeg"])
    if not uploaded:
        st.caption("画像をアップロードするとフィルターが使えます。")
        return

    image = Image.open(uploaded).convert("RGB")
    st.image(image, caption="元画像", use_column_width=True)

    mode = st.selectbox("処理を選択", ["グレースケール", "左右反転"])
    if mode == "グレースケール":
        processed = ImageOps.grayscale(image)
    else:
        processed = ImageOps.mirror(image)

    st.image(processed, caption="処理後", use_column_width=True)

    buf = BytesIO()
    processed.save(buf, format="PNG")
    st.download_button("画像をダウンロード", data=buf.getvalue(), file_name="processed.png", mime="image/png")
