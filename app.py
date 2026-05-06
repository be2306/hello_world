import streamlit as st

st.set_page_config(
    page_title="Hello World GUI",
    page_icon="👋",
    layout="centered"
)

st.title("Hello, World GUI")
st.write("This is a simple Python GUI running in GitHub Codespaces.")

name = st.text_input("Enter your name:", value="World")

if st.button("Say hello"):
    st.success(f"Hello, {name}!")

st.caption("Built with Python and Streamlit.")
