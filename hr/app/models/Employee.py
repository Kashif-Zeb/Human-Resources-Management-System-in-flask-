from hr.app.db import db

employee_training = db.Table(
    "employee_training",
    db.Column("e_id",db.Integer,db.ForeignKey("employee.id",ondelete='CASCADE'),primary_key=True),
    db.Column("t_id",db.Integer,db.ForeignKey("training.training_id",ondelete='CASCADE'),primary_key=True)
)


class Employee(db.Model):
    __tablename__ = "employee"
    id  = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(50),nullable=False)
    address  = db.Column(db.String(200),nullable=True)
    phone = db.Column(db.String(20),nullable=True,unique=True)
    email = db.Column(db.String(50),nullable=True,unique=True)
    job_id =db.Column(db.Integer,db.ForeignKey("job.job_id"))
    department_id = db.Column(db.ForeignKey("department.department_id"))

    department = db.relationship(
        "Department",
        back_populates="employees",
    )
    jobs = db.relationship("Job",back_populates="employees")

    payrolls = db.relationship(
        "Payroll",
        back_populates="employees",cascade ="all"
    )

    performances = db.relationship(
        "Performance",
        back_populates="employees",cascade ="all"
    )


    benefits = db.relationship(
        "Benefit",
        back_populates="employees",cascade = "all"
    )

    documents = db.relationship(
        "Document",
        back_populates="employees",cascade = "all"
    )

    attendences = db.relationship(
        "Attendence",
        back_populates="employees",cascade = "all"
    )

    trainings = db.relationship(
        "Training", secondary = employee_training,
        back_populates="employees",
    )