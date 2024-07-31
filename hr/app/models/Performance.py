from hr.app.db import db



class Performance(db.Model):
    __tablename__ = "performance"
    performance_id  = db.Column(db.Integer,primary_key=True,autoincrement=True)
    reviewdate = db.Column(db.Date,nullable=False)
    score = db.Column(db.Integer,nullable=False)
    feedback = db.Column(db.String(200),nullable=False)
    employee_id = db.Column(db.Integer,db.ForeignKey("employee.id"))

    employees = db.relationship(
        "Employee",
        back_populates="performances",
    )
