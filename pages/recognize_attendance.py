import streamlit as st
import os
import cv2
import numpy as np
from PIL import Image
from src.utils import mark_attendance, load_students

# Classroom coordinates and allowed radius
CLASSROOM_COORDS = (28.997564325294377, 77.01760864020346)
RADIUS_METERS = 50

st.title("📸 Recognize & Mark Attendance")

# Capture student photo
uploaded_image = st.camera_input("Capture student photo")

# Initialize latitude and longitude
latitude = None
longitude = None

# -------------------- Auto Capture Location -------------------- #
if "latitude" not in st.session_state:
    st.session_state.latitude = None
if "longitude" not in st.session_state:
    st.session_state.longitude = None

# Inject JavaScript to capture location in browser
st.markdown(
    """
    <script>
    navigator.geolocation.getCurrentPosition(
        function(position) {
            const lat = position.coords.latitude;
            const lon = position.coords.longitude;
            document.dispatchEvent(new CustomEvent("streamlit:setComponentValue", {
                detail: {key: "latitude", value: lat}
            }));
            document.dispatchEvent(new CustomEvent("streamlit:setComponentValue", {
                detail: {key: "longitude", value: lon}
            }));
        }
    );
    </script>
    """,
    unsafe_allow_html=True
)

# Retrieve captured location
latitude = st.session_state.latitude
longitude = st.session_state.longitude

# -------------------- Face Recognition -------------------- #
if uploaded_image:
    # Convert Streamlit image to OpenCV format
    img = Image.open(uploaded_image)
    frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

    recognized = False
    students = load_students()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame_resized = cv2.resize(gray_frame, (100, 100))

    for student in students:
        template = cv2.imread(student["file"], cv2.IMREAD_GRAYSCALE)
        template = cv2.resize(template, (100, 100))
        res = cv2.matchTemplate(gray_frame_resized, template, cv2.TM_CCOEFF_NORMED)
        if np.max(res) >= 0.5:
            recognized = True
            student_id = student["id"]
            student_name = student["name"]
            break

    if recognized:
        st.success(f"✅ Recognized {student_name}")
        mark_attendance(
            student_id,
            student_name,
            latitude=latitude,
            longitude=longitude,
            classroom_coords=CLASSROOM_COORDS,
            radius=RADIUS_METERS
        )
        st.write(f"Location recorded: {latitude}, {longitude}")
    else:
        st.warning("❌ Face not recognized. Attendance not marked.")

