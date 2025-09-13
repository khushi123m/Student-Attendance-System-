import os
import pandas as pd
from datetime import datetime
from math import radians, cos, sin, asin, sqrt

ATTENDANCE_FILE = "attendance.csv"
DATA_DIR = "dataset/"  # Folder where student images are stored

# -------------------- Helper: Distance Calculation -------------------- #
def haversine(lat1, lon1, lat2, lon2):
    """Calculate distance in meters between two GPS points."""
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    km = 6371 * c
    return km * 1000

# -------------------- Attendance Management -------------------- #
def init_attendance_file():
    """Create attendance.csv if it doesn't exist or is empty."""
    if not os.path.exists(ATTENDANCE_FILE) or os.stat(ATTENDANCE_FILE).st_size == 0:
        df = pd.DataFrame(columns=["ID", "Name", "Time", "Latitude", "Longitude"])
        df.to_csv(ATTENDANCE_FILE, index=False)

def mark_attendance(student_id: str, student_name: str,
                    latitude=None, longitude=None,
                    classroom_coords=None, radius=None):
    init_attendance_file()
    df = pd.read_csv(ATTENDANCE_FILE)
    df["ID"] = df["ID"].astype(str)
    today = datetime.now().strftime("%Y-%m-%d")

    # Already marked check
    if not df.empty and any((df["ID"] == str(student_id)) & (df["Time"].str.startswith(today))):
        print(f"[INFO] {student_name} is already marked present today.")
        return

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_entry = pd.DataFrame([[str(student_id), student_name, now, latitude, longitude]],
                             columns=["ID", "Name", "Time", "Latitude", "Longitude"])
    df = pd.concat([df, new_entry], ignore_index=True)
    df.to_csv(ATTENDANCE_FILE, index=False)
    print(f"[INFO] Attendance marked for {student_name} at ({latitude}, {longitude})")


def clear_attendance():
    """Clear all attendance records."""
    df = pd.DataFrame(columns=["ID", "Name", "Time", "Latitude", "Longitude"])
    df.to_csv(ATTENDANCE_FILE, index=False)
    print("[INFO] Attendance file cleared")

def read_attendance_file():
    """Return attendance DataFrame."""
    init_attendance_file()
    return pd.read_csv(ATTENDANCE_FILE)

# -------------------- Student Dataset Management -------------------- #
def parse_student_filename(filename: str):
    """Extract student_id and name from saved image filename."""
    parts = filename.split("_")
    if len(parts) >= 2:
        return parts[0], parts[1]
    return None, None

def load_students():
    """Load all student images from dataset folder."""
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    students = []
    for file in os.listdir(DATA_DIR):
        if file.endswith(".jpg"):
            student_id, student_name = parse_student_filename(file)
            if student_id and student_name:
                students.append({"id": student_id, "name": student_name, "file": os.path.join(DATA_DIR, file)})
            else:
                print(f"[WARN] Skipping file with unexpected format: {file}")
    return students
