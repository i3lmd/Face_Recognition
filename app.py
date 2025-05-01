import streamlit as st
import pandas as pd
from datetime import datetime
import time
from streamlit_autorefresh import st_autorefresh

count = st_autorefresh(interval=2000, limit=100, key="fizzbuzzcounter")

if count == 0:
    st.write("count is zero")
elif count % 3==0 and count%5==0:
    st.write("count is fizzbuzz")
elif count % 3==0:
    st.write("count is fizz")
elif count % 5==0:
    st.write("count is buzz")
else:
    st.write(f"count : {count}")
    

ts=time.time()
date=datetime.fromtimestamp(ts).strftime("%Y-%m-%d")
time_stamp=datetime.fromtimestamp(ts).strftime("%H:%M-%S")
df=pd.read_csv("Attendance/Attendance_" + date + ".csv")

st.dataframe(df.style.highlight_max(axis=0, color='purple'))
