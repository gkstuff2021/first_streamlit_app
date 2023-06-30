import streamlit
streamlit.title("A new Streamlit App.")
streamlit.header("We will make Snowflake cool.")
streamlit.text("Complete Badge 2 Asap.")
streamlit.text("Aim for Certification.")
streamlit.text("Your emojis for the day:🥣 🥗 🐔 🥑🍞")
streamlit.header('🍌🥭 Build Your Own Training Plan 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
