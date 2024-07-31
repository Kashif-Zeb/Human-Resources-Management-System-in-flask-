# from sqlalchemy import func
from hr.app.models.Attendence import Attendence
from hr.app.models.Job import Job
from hr.app.models.Department import Department
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import joinedload
from flask_sqlalchemy import pagination
# from hr.app.db import db
# from hr.app.models.BloodDonation import BloodDonation
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import desc

class attendenceRepository:
    @staticmethod
    def add_attendence_in_db(session:scoped_session,args:dict) -> Attendence:
        try:
            attendence = Attendence(**args)
            session.add(attendence)
            session.flush()
            return attendence
        except SQLAlchemyError:
            session.rollback()
            raise

    @staticmethod
    def get_attendence_by_Id(session:scoped_session,args:dict) -> Attendence:
        try:
            res = session.query(Attendence).filter(Attendence.employee_id==args.get("employee_id")).order_by(desc(Attendence.date)).all()
            return res
        except SQLAlchemyError:
            raise
    
    @staticmethod
    def get_attendence_by_Id2(session:scoped_session,args:dict) -> Attendence:
        try:
            res = session.query(Attendence).filter(Attendence.attendence_id==args.get("attendence_id")).first()
            return res
        except SQLAlchemyError:
            raise
    # @staticmethod
    # def get_employee_by_id_for_all_details(session:scoped_session,args:dict) -> Employee:
    #     try:
    #         res =session.query(Employee).\
    #             filter(Employee.id == args.get("employee_id")).\
    #             options(joinedload(Employee.jobs), joinedload(Employee.department)).first()
    #         # res = session.query(Employee).\
    #         #         join(Job, Employee.job_id == Job.job_id).\
    #         #         join(Department, Employee.department_id == Department.department_id).\
    #         #         filter(Employee.id == args.get("employee_id")).\
    #         #         first()
    #         return res
    #     except SQLAlchemyError:
    #         raise

    
    # @staticmethod
    # def get_all_employee_from_db(session:scoped_session,args:dict) -> Job:
    #     try:
    #         offset = (args.get("page") - 1) * args.get("per_page")
    #         res = session.query(Employee).\
    #         options(joinedload(Employee.jobs),joinedload(Employee.department))
    #         employees = res.offset(offset).limit(args.get("per_page")).all()
        
    #         # Get total count for pagination metadata
    #         total = res.count()
    #         return res,total
    #     except SQLAlchemyError:
    #         raise

    # @staticmethod
    # def get_employee_by_id(session:scoped_session,args:dict):
    #     try:
    #         res = session.query(Employee).filter(Employee.id==args.get("id")).first()
    #         return res
    #     except SQLAlchemyError:
    #         raise
    @staticmethod
    def update_attendence_in_db(session:scoped_session,check_attendence:Attendence,args:dict):
        try:
            check_attendence.date = args.get("date")
            check_attendence.check_in_time = args.get("check_in_time")
            check_attendence.check_out_time = args.get("check_out_time")
            check_attendence.employee_id = args.get("employee_id")
            session.flush()

        except SQLAlchemyError:
            raise