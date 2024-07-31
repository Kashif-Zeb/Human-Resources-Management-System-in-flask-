from hr.app.db import db
from sqlalchemy.dialects.mysql import JSON


class Job(db.Model):
    __tablename__ = "job"
    job_id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(50),nullable=False)
    description = db.Column(db.String(50),nullable=False)
    salary_range = db.Column(JSON,nullable=False)

    employees = db.relationship(
            "Employee",
            back_populates="jobs",
        )
