from hr.app.db import db


class Attendence(db.Model):
    __tablename__ = "attendence"
    attendence_id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    date = db.Column(db.Date,nullable=False)
    check_in_time = db.Column(db.DateTime,nullable=False)
    check_out_time = db.Column(db.DateTime,nullable=False)
    employee_id = db.Column(db.Integer,db.ForeignKey("employee.id"))

    employees = db.relationship(
        "Employee",
        back_populates="attendences"
    )
