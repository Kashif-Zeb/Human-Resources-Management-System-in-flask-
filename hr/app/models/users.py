from hr.app.db import db
from sqlalchemy import Integer ,String,Column
from werkzeug.security import generate_password_hash,check_password_hash
class Users(db.Model):
    __tablename__="users"
    user_id = Column(Integer,primary_key=True,autoincrement=True)
    username = Column(String(50),nullable=False,unique=True)
    email = Column(String(200),nullable=False,unique=True)
    hash_password = Column(String(200),nullable=False)
    role = Column(String(50),nullable=False)
    def set_password(self, password):
        self.hash_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hash_password, password)