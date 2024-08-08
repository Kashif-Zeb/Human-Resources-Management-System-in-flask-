from hr.app.db import db

class Path(db.Model):
    __tablename__="path"
    id = db.Column(db.Integer,primary_key=True)
    path_name = db.Column(db.String(25),nullable=False)

    goings = db.relationship("Employee", foreign_keys="Employee.going_id", back_populates="going_path")
    comings = db.relationship("Employee", foreign_keys="Employee.comming_id", back_populates="coming_path")