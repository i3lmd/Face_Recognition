# 🧠 Face Recognition Attendance System with Python & OpenCV

Welcome to the **Face Recognition Attendance System**, an intelligent desktop application built with Python that leverages real-time facial recognition to mark and record attendance — no manual input required!

> 🚀 _“Bringing automation to the classroom and workplace with AI-driven face recognition.”_

---

## ✨ Key Features

✅ **Real-Time Face Detection & Recognition** using `OpenCV`  
✅ **Add New Faces on the Fly** with `add_faces.py`  
✅ **Attendance Logging** with timestamps stored in CSV format  
✅ **Simple GUI Integration** using `Tkinter`  
✅ **Auto-Creation of Face Data** using a camera feed  
✅ **Visual Feedback with Background UI**  
✅ **Test Mode** (`test.py`) for rapid model validation  
✅ **Clean Project Structure** and modular code  
✅ **Easy to Extend** for schools, companies, or events

---

## 📸 How It Works

1. **Run `add_faces.py`**  
   ➤ Capture and save new face images under a name of your choice.

2. **Run `app.py`**  
   ➤ Starts the recognition interface using your webcam.  
   ➤ logs attendance when a known face is detected after pressing "O".

3. **View Attendance**  
   ➤ CSV logs with timestamped entries can be found in the `Attendance/` folder.

4. **Run `test.py`**  
   ➤ A quick way to test face recognition separately without logging.

---

## 📁 Project Structure

| File/Folder       | Description                                      |
|-------------------|--------------------------------------------------|
| `Attendance/`     | Stores CSV files with logged attendance records  |
| `Data/`           | Contains stored face images for recognition      |
| `Background.png`  | Background image used in the application UI      |
| `add_faces.py`    | Script to add new faces to the dataset           |
| `app.py`          | Main application for real-time recognition       |
| `test.py`         | Script to test face recognition functionality    |


---

## 🔧 Tech Stack

- **Python 3**
- **OpenCV** – Real-time computer vision
- **Tkinter** – GUI elements
- **NumPy** – Matrix operations
- **OS / CSV Modules** – File handling
- **PIL (Pillow)** – Image management

---

## 🖥️ Setup Instructions

### Prerequisites

- Python 3.x
- Webcam (built-in or external)

### Installation

```bash
git clone https://github.com/i3lmd/Face_Recognition.git
cd Face_Recognition_Attendance
pip install -r requirements.txt
