import streamlit
import requests
import pandas

streamlit.title('My cafe')
streamlit.header('Breakfast Menu')
streamlit.text('Oatmeal')
streamlit.text('Smoothie')
streamlit.text('Boiled Eggs')

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

streamlit.dataframe(fruityvice_normalized)
