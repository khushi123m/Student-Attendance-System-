import cv2
import os

def enroll_student(student_id, student_name):
    # Folder to store student images
    folder = "dataset/"
    os.makedirs(folder, exist_ok=True)  # Create folder if it doesn't exist

    # File name format: ID_Name.jpg
    filename = f"{folder}{student_id}_{student_name}.jpg"

    # Initialize webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("[ERROR] Cannot access webcam.")
        return

    print("[INFO] Press 'c' to capture the photo.")
    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        cv2.imshow("Enrollment - Press 'c' to capture", frame)
        key = cv2.waitKey(1)
        if key & 0xFF == ord('c'):
            cv2.imwrite(filename, frame)
            print(f"[INFO] Enrollment completed! Saved as {filename}")
            break
        elif key & 0xFF == ord('q'):
            print("[INFO] Enrollment canceled.")
            break

    cap.release()
    cv2.destroyAllWindows()

# Example usage
if __name__ == "__main__":
    student_id = input("Enter Student ID: ")
    student_name = input("Enter Student Name: ")
    enroll_student(student_id, student_name)
