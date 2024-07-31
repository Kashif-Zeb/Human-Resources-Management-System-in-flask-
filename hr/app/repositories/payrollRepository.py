# from sqlalchemy import func
from hr.app.models.Payroll import Payroll
from hr.app.models.Job import Job
from hr.app.models.Department import Department
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import joinedload
from flask_sqlalchemy import pagination
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import desc


class IDNotFoundException(Exception):
    def __init__(self, id_type, id_value):
        self.message = f"{id_type} '{id_value}' not found."
        super().__init__(self.message)

class payrollRepository:
    @staticmethod
    def add_payroll_in_db(session:scoped_session,args:dict) -> Payroll:
        try:
            payroll = Payroll(**args)
            session.add(payroll)
            session.flush()
            return payroll
        except SQLAlchemyError:
            session.rollback()
            raise

    @staticmethod
    def get_payroll_by_employee(session:scoped_session,args:dict) -> Payroll:
        try:
            res = session.query(Payroll).filter(Payroll.employee_id==args.get("employee_id")).order_by(desc("payroll_id")).all()
            if not res:
                raise IDNotFoundException("employee_id",args.get("employee_id"))
            return res
        
        except SQLAlchemyError:
             raise 
    

    @staticmethod
    def get_payroll_by_payroll_id(session:scoped_session,args:dict):
        try:
            res = session.query(Payroll).filter(Payroll.payroll_id==args.get("payroll_id")).first()
            if not res:
                raise IDNotFoundException("payroll_id",args.get("payroll_id"))
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
    def update_payroll_in_db(session:scoped_session,check_payroll:Payroll,args:dict):
        try:
            check_payroll.salary = args.get("salary")
            check_payroll.bonus = args.get("bonus")
            check_payroll.deduction = args.get("deduction")
            check_payroll.paydate = args.get("paydate")
            check_payroll.employee_id = args.get("employee_id")
            session.flush()

        except SQLAlchemyError:
            raise