import streamlit

streamlit.title("A new Streamlit App.")
streamlit.header("We will make Snowflake cool.")
streamlit.text("Complete Badge 2 Asap.")
streamlit.text("Aim for Certification.")
streamlit.text("Your emojis for the day:🥣 🥗 🐔 🥑🍞")
streamlit.header('🍌🥭 Build Your Own Training Plan 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected =  streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Grapes','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

import requests
streamlit.header("Fruityvice Fruit Advice.")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)


import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)

my_cur = my_cnx.cursor()
my_cur.execute("SELECT * FROM FRUIT_LOAD_LIST")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)

streamlit.header("More Fruityvice Fruit Advice to add fruit of your choice...")
add_fruit_choice = streamlit.text_input('What fruit would you like to add information about?','Kiwi')
streamlit.write('The user wanted to add this fruit: ', add_fruit_choice)

my_cur.execute("insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values ('test')");

