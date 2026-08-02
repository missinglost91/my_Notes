import streamlit as st

st.title("知识库更新服务")

uploaded_file = st.file_uploader(
    "上传TXT文件",
    type=["txt"],
    accept_multiple_files=False, # 只允许上传一个文件
    help="上传要更新的知识库文件",



)

if uploaded_file is not None:

    st.subheader("文件内容预览")
    st.write(f"上传的文件名: {uploaded_file.name}")
    st.write(f"文件大小: {uploaded_file.size/1024:.2f} KB")
    st.write(f"文件类型: {uploaded_file.type}")

    text=uploaded_file.getvalue().decode("utf-8")
    st.write(text)
