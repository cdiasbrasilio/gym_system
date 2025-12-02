# Gym Management System 🏋️‍♂️

This is a **work-in-progress** project for managing a fitness academy, built with **Flask (Python)** on the backend, **PostgreSQL** as the database, and **HTML/CSS/JS** on the frontend.  
The goal is to create a complete system for students, instructors, and administrators, including login, role-based dashboards, training management, and group classes.

---

## ✅ Features already implemented

- **Login system** with distinct roles:
  - Student
  - Instructor
  - Admin
- **Session persistence** using `localStorage` in the browser.
- **Student dashboard**:
  - View personal data.
- **Instructor dashboard**:
  - List students.
  - Register new students.
- **Admin dashboard**:
  - List instructors.
  - Register new instructors.
- **Logout** available on all dashboards, clearing session data.
- **Access protection**: each page can only be accessed by the correct role.

---

## 🚀 Upcoming features (in development)

- **Individual training management**:
  - Instructors create training plans.
  - Students view assigned trainings.
- **Group classes**:
  - Admin creates and removes classes.
  - Instructors adjust schedules and capacity.
  - Students enroll in classes based on availability.
  - Enrollment limits and participant lists.
- **Calendar integration**:
  - Students see confirmed classes in a personal schedule.
  - Instructors view their teaching schedule.
- **Security improvements**:
  - Password hashing with `bcrypt`.
  - Stronger backend permission control.
- **Interface enhancements**:
  - Fixed navbar/menu with navigation and logout.
  - Responsive design (Bootstrap).
- **Statistics and reports**:
  - Progress charts for students.
  - Dashboard for admins.

---

## 🛠️ Tech stack

- **Backend**: Python + Flask  
- **Database**: PostgreSQL  
- **Frontend**: HTML, CSS, JavaScript  
- **Version control**: Git + GitHub

> ⚠️ The database schema (`schema.sql`) will be added at the final stage of development, once all features are consolidated. This ensures the script reflects the complete and stable structure of the project.


---

## 📌 Project status

This project is **in progress** and will be expanded with new features.  
The current focus is consolidating the login and role-based dashboards, followed by training and group class management.

---

## 🤝 Contributions

This is a personal project under development.  
Suggestions and improvements are welcome via c.diasbrasilio@outlook.com


