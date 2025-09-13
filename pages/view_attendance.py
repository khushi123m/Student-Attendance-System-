import streamlit as st
import pandas as pd
from src.utils import read_attendance_file

st.title("📊 View Attendance")

try:
    df = read_attendance_file()
    st.dataframe(df)
except Exception:
    st.warning("No attendance file found.")

