import streamlit as st
import pandas as pd

st.title("STREAMLIT APP NI GELO THE GREAT")
#if sir want mo nung katulad sa Screenshot something like this

name = st.text_input("Enter your name: ")

if name:
    st.write("Hello, ", name) #parang c++ lang


love = st.slider("Gano mo ako ka love: ", 1, 5, 10)

st.write("You love me: ", love, "%")

data = pd.DataFrame({
    "Lambing Schedule": ["Monday", "Wednesday", "Friday", "Sunday"], "Kiss Count": [10, 2, 20, 12]
})

st.subheader("Lambing Table")
st.dataframe(data)

st.subheader("Kiss Chart")
st.line_chart(data.set_index("Lambing Schedule"))

st.button("Submit")
