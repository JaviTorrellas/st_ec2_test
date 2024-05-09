import streamlit as st
import pandas as pd


print('app starts')
# Set the app title
st.set_page_config(page_title="Test Streamlit AWS App")
st.header("Test Streamlit AWS App")

# Create tabs
tabs = st.tabs(["View DataFrame", "Insert Text"])
print('tab1')
# Tab 1: View DataFrame
with tabs[0]:
    st.header("View DataFrame")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        if st.button("Preview DataFrame"):
            st.write(df)
print('tab2')
# Tab 2: Insert Text
with tabs[1]:
    st.header("Insert Text")
    text_input = st.text_input("Enter some text")
    if text_input:
        st.write(text_input)