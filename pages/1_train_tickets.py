import streamlit as st
import time
import random
import datetime
from datetime import date

st.header("Can I book train tickets in advance now?")

start_date = date.today()
st.write("Todays date = " + str(start_date))

date_1 = datetime.datetime.strptime(str(start_date), "%Y-%m-%d")
end_date = date_1 + datetime.timedelta(days=122)
st.write("The earliest date you can book from is " + str(end_date))

st.header("Mandira")
st.header("Baby Ele")
st.header("Bal Ganesh")

today = datetime.date.today()
future = datetime.date(2024,5,15)
diff = future - today
st.write("Still there are ", diff.days, "days for bithday")


target_date = st.date_input("When's your birthday", datetime.date.today())

date_2 = datetime.datetime.strptime(str(target_date), "%Y-%m-%d")
end_date = date_2 + datetime.timedelta(days=122)
st.header("You can start booking from " + str(end_date))


