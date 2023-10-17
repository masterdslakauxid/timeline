import streamlit as st



with st.form("my_form"):
   st.write("Inside the form")
   # Using object notation
   

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

st.write("Outside the form")

