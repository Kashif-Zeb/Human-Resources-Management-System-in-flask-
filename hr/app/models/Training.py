from hr.app.db import db

from .Employee import employee_training

class Training(db.Model):
    __tablename__ = "training"
    training_id =db.Column(db.Integer,primary_key=True,autoincrement=True)
    training_name =  db.Column(db.String(50),nullable=False)
    date  = db.Column(db.Date,nullable=False)
    status =  db.Column(db.String(50),nullable=False)
    description = db.Column(db.String(200),nullable=False)
    employees = db.relationship("Employee",secondary = employee_training,back_populates="trainings")
