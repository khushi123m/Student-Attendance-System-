import streamlit as st
import os
import pandas as pd
from src.utils import read_attendance_file, load_students

DATA_DIR = "dataset/"
ATTENDANCE_FILE = "attendance.csv"

st.title("👨‍🎓 View Students")

students_list = []

# Load enrolled students
if not os.path.exists(DATA_DIR):
    st.warning("No students enrolled yet.")
else:
    students_files = [f for f in os.listdir(DATA_DIR) if f.endswith(".jpg")]
    if not students_files:
        st.info("No students found.")
    else:
        # Load last attendance info if available
        if os.path.exists(ATTENDANCE_FILE):
            attendance_df = read_attendance_file()
        else:
            attendance_df = pd.DataFrame(columns=["ID", "Name", "Time", "Latitude", "Longitude"])

        for f in students_files:
            student_id = f.split("_")[0]
            student_name = f.split("_")[1].replace(".jpg", "")
            # Get last recorded location
            student_attendance = attendance_df[attendance_df["ID"] == student_id]
            if not student_attendance.empty:
                last_record = student_attendance.iloc[-1]
                lat = last_record["Latitude"]
                lon = last_record["Longitude"]
            else:
                lat, lon = None, None

            students_list.append({
                "Student ID": student_id,
                "Name": student_name,
                "Last Latitude": lat,
                "Last Longitude": lon
            })

        st.table(students_list)


