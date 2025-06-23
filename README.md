# 🎓 Student Registration Web Application

This is a simple *Student Registration System* built using Python and Flask. It allows users to register students, display all student records in a table, and update or delete them as needed. The data is stored in a local SQLite database.

---

## 📌 Features

- ✅ Register new students
- ✅ View all student records
- ✅ Update and delete existing records
- ✅ Simple and clean user interface using HTML and CSS
- ✅ Backend built with Flask
- ✅ Database: SQLite (no setup required)

---

## 💻 Technologies Used

| Technology | Description |
|------------|-------------|
| Python     | Core programming language |
| Flask      | Backend web framework |
| SQLite     | Database to store student records |
| HTML/CSS   | Frontend form and styling |

---

## 🧠 Project Description

This project simulates a basic student registration system for colleges or institutions. Users can:

- Fill in a student registration form with:
  - Full Name
  - Email
  - Phone Number
  - Gender
  - Date of Birth
  - Address
  - Course
- View the list of registered students in a table format
- Edit or delete student records

All records are saved in an SQLite database (students.db), and are accessible via the Flask backend.

---

## 🚀 Getting Started

### 🔧 Prerequisites

Make sure you have Python installed. To check:

```bash
python --version
your_project_folder/
├── app.py                # Flask application code
├── students              # SQLite database file (auto-created)
├── static/
│   └── style.css         # Styling for the form and table
├── templates/
│   ├── form.html         # Registration form + student list
│   └── update.html       # Update form for editing student
├── README.md             # Project documentation
