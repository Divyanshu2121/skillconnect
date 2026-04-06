# SkillConnect – Job Portal with Analytics (SDG1)

## 📌 Project Overview

SkillConnect is a web-based job portal application developed using Flask and SQL. The platform allows employers to post jobs and workers to apply for jobs. The system also includes an analytics dashboard to analyze job applications, user distribution, and job trends. This project supports **SDG1 – No Poverty** by helping connect job seekers with employment opportunities.

---

## 🚀 Features

* User Signup and Login
* Employer Job Posting
* View Available Jobs
* Apply for Jobs
* Dashboard Navigation
* Analytics Dashboard
* Applications Tracking
* Logout System
* Database Integration

---

## 📊 Analytics Dashboard

The system provides analytics using SQL queries and charts:

* Applications per Job
* Users per City
* Jobs per Category

Charts are displayed using **Chart.js**.

---

## 🧰 Tech Stack

* Python
* Flask
* SQLAlchemy
* SQLite
* HTML
* CSS
* Chart.js
* GitHub

---

## 🗄 Database Tables

The project uses the following tables:

* Users
* Jobs
* Applications

### Database Schema

**Users**

* user_id
* name
* email
* password
* role
* city

**Jobs**

* job_id
* title
* company
* location
* salary
* category
* posted_by

**Applications**

* application_id
* user_id
* job_id
* status
* applied_date

---

## 🏗 Project Structure

```
skillconnect-job-portal/
│
├── app.py
├── database.py
├── skillconnect.db
├── models/
├── templates/
├── static/
├── screenshots/
├── README.md
```

---

## ▶️ How to Run the Project

1. Install required libraries:

```
pip install flask flask_sqlalchemy
```

2. Run the application:

```
python app.py
```

3. Open browser:

```
http://127.0.0.1:5000/login
```

---

## 📷 Screenshots

Add screenshots of:

* Signup Page
* Login Page
* Dashboard
* Post Job Page
* Jobs Page
* Analytics Dashboard

(Store them in the **screenshots** folder)

---

## 🎯 Project Outcome

This project demonstrates:

* Backend Development using Flask
* Database Design and SQL Queries
* CRUD Operations
* Analytics Dashboard
* Data Visualization
* Full Stack Web Development Basics

---

## 🌍 SDG Goal

This project supports **United Nations Sustainable Development Goal 1 (No Poverty)** by providing a platform that connects job seekers with employers and helps increase employment opportunities.

---

## 👨‍💻 Author

**Divyanshu Sharma**
