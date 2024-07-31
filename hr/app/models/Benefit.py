from hr.app.db import db


class Benefit(db.Model):
    __tablename__ = "benefit"
    benefit_id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    benefit_type = db.Column(db.String(50),nullable=False)
    description = db.Column(db.String(200),nullable=False)
    start_date = db.Column(db.Date,nullable=False)
    end_date = db.Column(db.Date,nullable=False)
    employee_id = db.Column(db.Integer,db.ForeignKey("employee.id"))

    employees = db.relationship(
        "Employee",
        back_populates="benefits",
    )
