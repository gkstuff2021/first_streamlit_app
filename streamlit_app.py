import streamlit
import pandas
import requests
import snowflake.connector

from urllib.error import URLError;

streamlit.title("A new Streamlit App.")
streamlit.header("We will make Snowflake cool.")
streamlit.text("Complete Badge 2 Asap.")
streamlit.text("Aim for Certification.")
streamlit.text("Your emojis for the day:🥣 🥗 🐔 🥑🍞")
streamlit.header('🍌🥭 Build Your Own Training Plan 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected =  streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Grapes','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)


def get_fruity_vice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized

streamlit.header("Fruityvice Fruit Advice.")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get info.")
  else:
    back_from_function = get_fruity_vice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
   
except URLError as e:
  streamlit.error()


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)


streamlit.header("The fruit load list contains:")
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("SELECT * FROM FRUIT_LOAD_LIST")
        return my_cur.fetchall()


if streamlit.button('View My Fruit Load List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    my_cnx.close()
    streamlit.dataframe(my_data_rows)


streamlit.header("More Fruityvice Fruit Advice to add fruit of your choice...")

def insert_row_snowflake(new_fruit):
    with  my_cnx.cursor() as my_cur:
        my_cur.execute("insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values ('" + new_fruit +"')");
        return "Thanks for adding:" + new_fruit
        

add_fruit_choice = streamlit.text_input('What fruit would you like to add information about?')

if streamlit.button('Add a fruit to the list'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    back_from_function = insert_row_snowflake(add_fruit_choice)
    my_cnx.close()
    streamlit.text(back_from_function)
   


#streamlit.write('The user wanted to add this fruit: ', add_fruit_choice)



