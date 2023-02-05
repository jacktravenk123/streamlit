import streamlit
import requests
import pandas
import snowflake.connector
#from urllib import URLError

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

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.text("Hello from Snowflake:")
streamlit.dataframe(my_data_row)

fruit_add = streamlit.text_input('What fruit would you like add?','Ex: Kiwi')
streamlit.write("Thanks for adding :", fruit_add)

my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values ('" + fruit_add + "')")
