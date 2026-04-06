from flask import Flask, render_template, request, redirect, session
from database import db
from models.user import User
from models.job import Job
from models.application import Application
from sqlalchemy import func
import datetime

app = Flask(__name__)
app.secret_key = "secretkey"

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///skillconnect.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Create Tables
with app.app_context():
    db.create_all()

# Home
@app.route('/')
def home():
    return redirect('/login')

# ---------------- SIGNUP ----------------
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        city = request.form['city']
        role = request.form['role']

        new_user = User(name=name, email=email, password=password, city=city, role=role)
        db.session.add(new_user)
        db.session.commit()

        return redirect('/login')

    return render_template('signup.html')

# ---------------- LOGIN ----------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email, password=password).first()

        if user:
            session['user_id'] = user.user_id
            session['role'] = user.role
            return redirect('/dashboard')
        else:
            return "Invalid Credentials"

    return render_template('login.html')

# ---------------- DASHBOARD ----------------
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/login')
    user_jobs_count = db.session.query(func.count(Job.job_id)).filter_by(posted_by=session['user_id']).scalar() or 0
    total_jobs = db.session.query(func.count(Job.job_id)).scalar() or 0
    return render_template('dashboard.html', user_jobs_count=user_jobs_count, total_jobs=total_jobs)

# ---------------- POST JOB ----------------
@app.route('/post_job', methods=['GET', 'POST'])
def post_job():
    if request.method == 'POST':
        title = request.form['title']
        company = request.form['company']
        location = request.form['location']
        salary = request.form['salary']
        category = request.form['category']
        posted_by = session['user_id']

        new_job = Job(title=title, company=company, location=location,
                      salary=salary, category=category, posted_by=posted_by)

        db.session.add(new_job)
        db.session.commit()

        return redirect('/dashboard')

    return render_template('post_job.html')

# ---------------- VIEW JOBS ----------------
@app.route('/jobs')
def view_jobs():
    jobs = Job.query.all()
    return render_template('jobs.html', jobs=jobs)

# ---------------- APPLY JOB ----------------
@app.route('/apply/<int:job_id>')
def apply_job(job_id):
    user_id = session['user_id']

    application = Application(
        user_id=user_id,
        job_id=job_id,
        status="Applied",
        applied_date=datetime.date.today()
    )

    db.session.add(application)
    db.session.commit()

    return redirect('/jobs')

# ---------------- ANALYTICS ----------------
@app.route('/analytics')
def analytics():
    job_applications = [[row.job_id, row[1]] for row in db.session.query(
        Application.job_id,
        func.count(Application.application_id)
    ).group_by(Application.job_id).all()]

    users_city = [[row.city, row[1]] for row in db.session.query(
        User.city,
        func.count(User.user_id)
    ).group_by(User.city).all()]

    jobs_category = [[row.category, row[1]] for row in db.session.query(
        Job.category,
        func.count(Job.job_id)
    ).group_by(Job.category).all()]

    return render_template(
        'analytics.html',
        job_applications=job_applications,
        users_city=users_city,
        jobs_category=jobs_category
    )

# ---------------- LOGOUT ----------------
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

# Run App
if __name__ == '__main__':
    app.run(debug=True)
