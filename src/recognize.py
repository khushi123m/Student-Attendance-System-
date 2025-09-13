import sys
import os
import cv2
import numpy as np
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.utils import mark_attendance

DATA_DIR = "dataset/"

def load_dataset():
    students = []
    for file in os.listdir(DATA_DIR):
        if file.endswith(".jpg"):
            try:
                student_id, student_name = file.replace(".jpg", "").split("_")
                students.append({"id": student_id, "name": student_name, "file": os.path.join(DATA_DIR, file)})
            except ValueError:
                print(f"[WARN] Skipping file with unexpected format: {file}")
    return students

def train_recognizer(students):
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    faces = []
    labels = []
    label_map = {}  # Maps numeric label to student info

    for idx, student in enumerate(students):
        img = cv2.imread(student["file"], cv2.IMREAD_GRAYSCALE)
        if img is None:
            print(f"[WARN] Could not read image: {student['file']}")
            continue
        img = cv2.resize(img, (200, 200))
        faces.append(img)
        labels.append(idx)
        label_map[idx] = student

    if faces and labels:
        recognizer.train(faces, np.array(labels))
    return recognizer, label_map

def recognize_face():
    students = load_dataset()
    if not students:
        print("[ERROR] No students found in dataset.")
        return

    recognizer, label_map = train_recognizer(students)
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("[ERROR] Cannot access webcam.")
        return

    print("[INFO] Press 'c' to recognize student, 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        cv2.imshow("Face Recognition", frame)
        key = cv2.waitKey(1)

        if key & 0xFF == ord('c'):  # Capture frame for recognition
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray_resized = cv2.resize(gray, (200, 200))

            label, confidence = recognizer.predict(gray_resized)
            student = label_map.get(label, None)

            if student and confidence < 70:  # Lower confidence is better
                cv2.putText(frame, f"Recognized: {student['name']}", (50, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                mark_attendance(student["id"], student["name"])
            else:
                cv2.putText(frame, "Unknown", (50, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            cv2.imshow("Face Recognition", frame)
            cv2.waitKey(2000)  # Show result for 2 seconds

        elif key & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    recognize_face()
