# from sqlalchemy import func
from hr.app.models.Benefit import Benefit
from hr.app.models.Job import Job
from hr.app.models.Department import Department
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import joinedload
# from flask_sqlalchemy import pagination
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import desc


class IDNotFoundException(Exception):
    def __init__(self, id_type, id_value):
        self.message = f"{id_type} '{id_value}' not found."
        super().__init__(self.message)

class benefitRepository:
    @staticmethod
    def add_benefit_in_db(session:scoped_session,args:dict) -> Benefit:
        try:
            benefit = Benefit(**args)
            session.add(benefit)
            session.flush()
            return benefit
        except SQLAlchemyError:
            session.rollback()
            raise

    @staticmethod
    def get_benefit_by_employee(session:scoped_session,args:dict) -> Benefit:
        try:
            res = session.query(Benefit).filter(Benefit.employee_id==args.get("employee_id")).order_by(desc("benefit_id")).all()
            if not res:
                raise IDNotFoundException("employee_id",args.get("employee_id"))
            return res
        
        except SQLAlchemyError:
             raise 
    

    @staticmethod
    def get_benefit_by_benefit_id(session:scoped_session,args:dict):
        try:
            res = session.query(Benefit).filter(Benefit.benefit_id==args.get("benefit_id")).first()
            if not res:
                raise IDNotFoundException("benefit_id",args.get("benefit_id"))
            return res
        except SQLAlchemyError:
            raise

    # # @staticmethod
    # # def get_attendence_by_Id2(session:scoped_session,args:dict) -> Attendence:
    # #     try:
    # #         res = session.query(Attendence).filter(Attendence.attendence_id==args.get("attendence_id")).first()
    # #         return res
    # #     except SQLAlchemyError:
    # #         raise
    # # # @staticmethod
    # # # def get_employee_by_id_for_all_details(session:scoped_session,args:dict) -> Employee:
    # # #     try:
    # # #         res =session.query(Employee).\
    # # #             filter(Employee.id == args.get("employee_id")).\
    # # #             options(joinedload(Employee.jobs), joinedload(Employee.department)).first()
    # # #         # res = session.query(Employee).\
    # # #         #         join(Job, Employee.job_id == Job.job_id).\
    # # #         #         join(Department, Employee.department_id == Department.department_id).\
    # # #         #         filter(Employee.id == args.get("employee_id")).\
    # # #         #         first()
    # # #         return res
    # # #     except SQLAlchemyError:
    # # #         raise

    
    # @staticmethod
    # def get_all_document_from_db_by_eid(session:scoped_session,args:dict) -> Document:
    #     try:
    #         res = session.query(Document).filter(Document.employee_id==args.get("employee_id")).all()
    #         return res
    #     except SQLAlchemyError:
    #         raise

    # # # @staticmethod
    # # # def get_employee_by_id(session:scoped_session,args:dict):
    # # #     try:
    # # #         res = session.query(Employee).filter(Employee.id==args.get("id")).first()
    # # #         return res
    # # #     except SQLAlchemyError:
    # # #         raise
    @staticmethod
    def update_benefit_in_db(session:scoped_session,check_benefit:Benefit,args:dict):
        try:
            check_benefit.benefit_type = args.get("benefit_type")
            check_benefit.description = args.get("description")
            check_benefit.start_date = args.get("start_date")
            check_benefit.end_date = args.get("end_date")
            check_benefit.employee_id = args.get("employee_id")
            session.flush()

        except SQLAlchemyError:
            raise