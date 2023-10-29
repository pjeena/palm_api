from langchain.llms import GooglePalm
import streamlit as st 



api_key = 'AIzaSyAolOXNAoKHZWOlfd-Qn4pbbW3WZepJ6wU' # get this free api key from https://makersuite.google.com/

llm = GooglePalm(google_api_key=api_key, temperature=0.1)

poem = llm("Write a 10 line poem about python programming language")


st.write(poem)
