# pages/home.py
import streamlit as st
import shutil
import os
from src.utils import clear_attendance

DATA_DIR = "dataset/"  # your student images folder

st.title("📊 Student Attendance Admin Panel")

st.markdown(
    """
    Welcome! Use the sidebar to navigate:
    - View Students
    - Enroll Student
    - Recognize & Mark Attendance
    - View Attendance
    """
)

st.subheader("⚠️ Reset System")

st.warning("This will delete all student images and attendance records. Use carefully!")

if st.button("Reset System"):
    # Clear attendance
    clear_attendance()

    # Remove all student images
    if os.path.exists(DATA_DIR):
        shutil.rmtree(DATA_DIR)
        os.makedirs(DATA_DIR, exist_ok=True)
    
    st.success("✅ System has been reset. All student data and attendance records cleared.")


