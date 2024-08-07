# from sqlalchemy import func
from hr.app.models.Employee import Employee
from hr.app.models.Job import Job
from hr.app.models.Department import Department
from hr.app.models.users import Users
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import joinedload
# from flask_sqlalchemy import pagination
# from hr.app.db import db
# from hr.app.models.BloodDonation import BloodDonation
from sqlalchemy.exc import SQLAlchemyError

class employeeRepository:
    @staticmethod
    def add_employee_in_db(session:scoped_session,args:dict) -> Employee:
        try:
            employee = Employee(**args)
            session.add(employee)
            session.flush()
            return employee
        except SQLAlchemyError:
            session.rollback()
            raise

    
    @staticmethod
    def get_employee_by_id_for_all_details(session:scoped_session,args:dict) -> Employee:
        try:
            res =session.query(Employee).\
                filter(Employee.id == args.get("employee_id")).\
                options(joinedload(Employee.jobs), joinedload(Employee.department)).first()
            # res = session.query(Employee).\
            #         join(Job, Employee.job_id == Job.job_id).\
            #         join(Department, Employee.department_id == Department.department_id).\
            #         filter(Employee.id == args.get("employee_id")).\
            #         first()
            return res
        except SQLAlchemyError:
            raise

    
    @staticmethod
    def get_all_employee_from_db(session:scoped_session,args:dict) -> Job:
        try:
            offset = (args.get("page") - 1) * args.get("per_page")
            res = session.query(Employee).\
            options(joinedload(Employee.jobs),joinedload(Employee.department))
            employees = res.offset(offset).limit(args.get("per_page")).all()
        
            # Get total count for pagination metadata
            total = res.count()
            return res,total
        except SQLAlchemyError:
            raise

    @staticmethod
    def get_employee_by_id(session:scoped_session,args:dict):
        try:
            res = session.query(Employee).filter(Employee.id==args.get("id")).first()
            return res
        except SQLAlchemyError:
            raise
    @staticmethod
    def get_employee_by_id2(session:scoped_session,args:dict):
        try:
            res = session.query(Employee).filter(Employee.id==args.get("employee_id")).first()
            return res
        except SQLAlchemyError:
            raise
    @staticmethod
    def update_employee_in_db(session:scoped_session,check_employee:Employee,args:dict):
        try:
            check_employee.name = args.get("name")
            check_employee.email = args.get("email")
            check_employee.address = args.get("address")
            check_employee.job_id = args.get("job_id")
            check_employee.department_id = args.get("department_id")
            check_employee.phone  =args.get("phone")
            session.flush()

        except SQLAlchemyError:
            raise
    

    @staticmethod
    def save_user_details_in_db(session:scoped_session,args:dict):
        try:
            password = args.pop("hash_password")
            user = Users(**args)
            user.set_password(password)
            session.add(user)
            session.flush()
            return user
        except SQLAlchemyError:
            raise
    

    @staticmethod
    def get_user(session:scoped_session,args:dict):
        try:
            res = session.query(Users).filter(Users.email==args.get("email")).first()
            return res
        except SQLAlchemyError:
            raise