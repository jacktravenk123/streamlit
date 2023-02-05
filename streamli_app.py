import streamlit
import requests

streamlit.title('My cafe')
streamlit.header('Breakfast Menu')
streamlit.text('Oatmeal')
streamlit.text('Smoothie')
streamlit.text('Boiled Eggs')

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)
