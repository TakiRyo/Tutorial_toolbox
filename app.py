import importlib
import streamlit as st
from tools.config import TOOLS


st.set_page_config(page_title="Tutorial ToolBox", layout="wide")

st.sidebar.title("Tutorial ToolBox")
menu_names = [tool["name"] for tool in TOOLS]
selected_name = st.sidebar.selectbox("メニュー", menu_names)

selected_tool = next(tool for tool in TOOLS if tool["name"] == selected_name)
module_name = selected_tool["module"]

try:
    tool_module = importlib.import_module(f"tools.{module_name}")
    if hasattr(tool_module, "show"):
        tool_module.show()
    else:
        st.error(f"{module_name}.py に show() が見つかりません。")
except Exception as exc:
    st.error("ツールの読み込みに失敗しました。")
    st.exception(exc)
