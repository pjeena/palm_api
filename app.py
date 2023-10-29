from langchain.llms import GooglePalm
import streamlit as st 



api_key = '' # get this free api key from https://makersuite.google.com/

llm = GooglePalm(google_api_key=api_key, temperature=0.1)

poem = llm("Write a 30 line poem about pizza and Italian people")


st.write(poem)
