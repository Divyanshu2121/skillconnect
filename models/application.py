from database import db

class Application(db.Model):
    __tablename__ = 'applications'

    application_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    job_id = db.Column(db.Integer)
    status = db.Column(db.String(20))
    applied_date = db.Column(db.Date)