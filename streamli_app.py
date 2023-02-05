import streamlit
import requests

streamlit.title('My cafe')
streamlit.header('Breakfast Menu')
streamlit.text('Oatmeal')
streamlit.text('Smoothie')
streamlit.text('Boiled Eggs')

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")

fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

streamlit.dataframe(fruityvice_normalized)
