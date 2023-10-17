import streamlit as st
import numpy as np
import time
import random
import datetime


st.title("Can I book train tickets in advance?")

#Sidebar starts
with st.form("my_form"):
   st.write("Inside the form")
   
   # Using "with" notation
   with st.sidebar:
        add_radio = st.radio(
            "Choose a shipping method",
            ("Standard (5-15 days)", "Express (2-5 days)")
        )

        add_selectbox = st.selectbox(
         "How would you like to be contacted?",
        ("Email", "Home phone", "Mobile phone")
        )
        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("slider", slider_val, "checkbox", checkbox_val)


with st.form(key='Submit'):
    submit_button = st.form_submit_button(label='Submit')
    if submit_button:
        if(val1 == correct_answer.strip()):
            st.success( "'" + val1 + "' is the correct answer")
        else:
            st.error("'"+ val1 + "' is the wrong answer")
            
with st.form(key='Next'):
    st.write("next question")

# with tab2:
#    st.header("A dog")
#    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

# with tab3:
#    st.header("An owl")
#    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
   