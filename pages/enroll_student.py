import streamlit as st
import os
from PIL import Image
import cv2
import numpy as np
from src.utils import mark_attendance

DATA_DIR = "dataset/"
os.makedirs(DATA_DIR, exist_ok=True)

st.title("➕ Enroll Student / Mark Attendance")

# ---------------- Inputs ---------------- #
student_id = st.text_input("Enter Student ID")
student_name = st.text_input("Enter Student Name")
uploaded_image = st.camera_input("Capture student photo")

# ---------------- Enrollment ---------------- #
if uploaded_image and student_id and student_name:
    # Convert uploaded image to OpenCV format
    img = Image.open(uploaded_image)
    frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

    # Save the student image
    filename = os.path.join(DATA_DIR, f"{student_id}_{student_name}.jpg")
    cv2.imwrite(filename, frame)
    st.success(f"Enrollment completed! Saved as {filename}")

    st.write("📍 Automatically capturing location...")

    # ---------------- Location Capture ---------------- #
    # Streamlit can't directly access GPS, but we can get approximate location via JS
    location_html = """
    <script>
    navigator.geolocation.getCurrentPosition(
        function(position) {
            const coords = position.coords;
            document.getElementById('coords').innerText = coords.latitude + ',' + coords.longitude;
        },
        function(err) {
            document.getElementById('coords').innerText = 'ERROR';
        }
    );
    </script>
    <div id="coords">Waiting for location...</div>
    """
    location_component = st.components.v1.html(location_html, height=50)

    # Fallback for manual entry
    latitude = st.number_input("Latitude (if automatic fails)")
    longitude = st.number_input("Longitude (if automatic fails)")

    if st.button("Mark Attendance with Location"):
        mark_attendance(student_id, student_name, latitude, longitude)
        st.success(f"Attendance marked for {student_name} at ({latitude}, {longitude})")

