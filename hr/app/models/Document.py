from hr.app.db import db


    
class Document(db.Model):
    __tablename__ = "document"
    document_id  = db.Column(db.Integer,primary_key=True,autoincrement=True)
    document_type = db.Column(db.String(50),nullable=False)
    file_path = db.Column(db.String(200),nullable=False)
    employee_id = db.Column(db.Integer,db.ForeignKey("employee.id"))
    employees = db.relationship(
        "Employee",
        back_populates="documents",
    )
