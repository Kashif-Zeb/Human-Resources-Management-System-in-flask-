from hr.app.db import db



class Payroll(db.Model):
    __tablename__ = "payroll"
    payroll_id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    salary=db.Column(db.Integer,nullable=False)
    bonus=db.Column(db.Integer,nullable=False)
    deduction = db.Column(db.Integer,nullable=False)
    paydate = db.Column(db.Date,nullable=False)
    employee_id = db.Column(db.Integer,db.ForeignKey("employee.id"))

    employees = db.relationship(
        "Employee",
        back_populates="payrolls",
    )
