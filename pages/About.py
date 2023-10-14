import streamlit as st
from streamlit_extras.colored_header import colored_header

st.set_page_config('About💻', layout='centered')

descp = """Introducing the Vectors Visualizer, a simple and engaging app developed by student Mohamad Bashar and supervised by teacher Alaa Hamdan. This app helps students memorize irregular verbs in a fun and interactive way.
The user-friendly interface caters to learners of all levels, making it easy for everyone to practice and improve their knowledge of Vectors."""
colored_header(label="About The Vectors Visualizer💎👍",
               description='', color_name="red-80")
st.write(descp)
