from src.utils import init_attendance_file, mark_attendance, parse_student_filename, clear_attendance

# Step 0: Clear file before test
clear_attendance()

# Step 1: Initialize
init_attendance_file()
print("[TEST] Attendance file initialized.")

# Step 2: Mark Rahul
mark_attendance("101", "Rahul")

# Step 3: Try marking again
mark_attendance("101", "Rahul")

# Step 4: Parse filename
student_id, student_name = parse_student_filename("102_Shreya_5.jpg")
print(f"[TEST] Parsed → ID: {student_id}, Name: {student_name}")

