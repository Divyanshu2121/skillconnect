from database import db

class Job(db.Model):
    __tablename__ = 'jobs'

    job_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    company = db.Column(db.String(100))
    location = db.Column(db.String(50))
    salary = db.Column(db.Integer)
    posted_by = db.Column(db.Integer)
    category = db.Column(db.String(50))