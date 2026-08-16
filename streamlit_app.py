import streamlit as st

st.title("My Streamlit Demo")
st.write("Hello, world from Hugging Face Spaces!")

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    st.success(f"Uploaded: {uploaded_file.name}")