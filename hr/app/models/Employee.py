from sqlalchemy import func,event
from hr.app.db import db
from sqlalchemy.ext.hybrid import hybrid_property

from hr.app.models import Document
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
    going_id = db.Column(db.Integer,db.ForeignKey("path.id"))
    comming_id = db.Column(db.Integer,db.ForeignKey("path.id"))
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

    going_path = db.relationship("Path", foreign_keys=[going_id], back_populates="goings")
    coming_path = db.relationship("Path", foreign_keys=[comming_id], back_populates="comings")   

    
    
    
    @hybrid_property
    def document_count(self):
        return len(self.documents)
    
    @document_count.expression
    def document_count(cls):
        return func.count(Document.document_id).label('document_count')
def before_insert(mapper, connection,target):
        print(f"after inserting {target.name}")
        print("mapper",mapper)
        print(connection)
        # You can modify the target object here if needed
        target.name = f"{target.name} C pakistan"
            
event.listen(Employee,"before_insert",before_insert)
# event.listen(MyModel, 'before_insert', before_insert)
# event.listen(MyModel, 'after_insert', after_insert)
# event.listen(MyModel, 'before_update', before_update)
# event.listen(MyModel, 'after_update', after_update)
# event.listen(MyModel, 'before_delete', before_delete)
# event.listen(MyModel, 'after_delete', after_delete)