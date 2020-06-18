import streamlit as st

st.title("My First Web App Using Streamlit")

# # Header/Subheader
st.header("This is a header") 
st.subheader("This is a subheader")


input = st.file_uploader("Upload a file", type=("png", "jpg"))

if input == None:
  st.warning('No file selected.')
else:
  st.image(input)