# 📸 Face Recognition Attendance Prototype
## 🚀 Overview

This project is a **Face Recognition based Attendance System** built using Streamlit, OpenCV, and NumPy.
It allows automatic student attendance marking by recognizing faces from a pre-registered dataset.

## ✨ Features

- 📷 Capture and recognize student faces in real time

- 📂 Dataset-based student enrollment

- 🗺️ Location-based attendance (using GPS coordinates + geopy)

- ✅ Attendance marked automatically and stored in a log file

- 🖥️ Simple and interactive Streamlit UI

🛠️ Tech Stack
## 🛠️ Tech Stack  

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)](https://www.python.org/)  
[![Streamlit](https://img.shields.io/badge/Streamlit-Web%20Interface-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)  
[![OpenCV](https://img.shields.io/badge/OpenCV-Face%20Recognition-5C3EE8?logo=opencv&logoColor=white)](https://opencv.org/)  
[![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?logo=numpy&logoColor=white)](https://numpy.org/)  
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Handling-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)  
[![Geopy](https://img.shields.io/badge/Geopy-Geospatial%20Analysis-5A2D81?logo=python&logoColor=white)](https://geopy.readthedocs.io/)  


## 📂 Project Structure
```
Attendance-Prototype/
│── dataset/
│── pages/
│   ├── enroll_student.py
    ├── home.py
    ├── recognize_attendance.py
    ├── veiw_attendance.py
    ├── veiw_student.py                # Stored images of registered students
│── src/
    ├── __init__.py    
    ├── utils.py                      # Helper functions (loading, marking attendance)
    ├── recognise.py
    ├── enrollment.py
│── test/
    ├── __init__.py    
    ├── test_utils.py 
│── run_admin_panel.py
    # Main Streamlit application
│── requirements.txt          # Python dependencies
│── attendance.csv   
│── README.md                 # Project documentation
```

## ⚙️ Installation

Clone the repository:
```

git clone https://github.com/yourusername/attendance-prototype.git
cd attendance-prototype
```


Create a virtual environment and activate it:
```
python -m venv venv
source venv/bin/activate    # On macOS/Linux
venv\Scripts\activate       # On Windows
```

Install dependencies:
```
pip install -r requirements.txt
```
## ▶️ Usage

Start the Streamlit app:
```
streamlit run run_admin_panel.py
```

### Upload/register student images into the dataset/ folder.

### Open the app in your browser → Capture live camera → Attendance gets marked.

## 📊 Attendance Logging

### Attendance records are stored with:

- Name/ID

- Date & Time

- Location validation

#### You can later export logs to CSV/Excel for reporting.

## 👨‍💻 Authors

### Rahul Manchanda  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/rahul-manchanda-3959b120a/)  
[![GitHub](https://img.shields.io/badge/GitHub-Portfolio-181717?logo=github&logoColor=white)](https://github.com/rahul15-manch)  
📧 [rahulmanchanda015@gmail.com](mailto:rahulmanchanda015@gmail.com)

---

### Khushi Munjal  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/khushi-m-491188364/)  
[![GitHub](https://img.shields.io/badge/GitHub-Portfolio-181717?logo=github&logoColor=white)](https://github.com/khushi123m)  
📧 [khushimunjal0660@gmail.com](mailto:khushimunjal0660@gmail.com)
