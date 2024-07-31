# from sqlalchemy import func
from hr.app.models.Document import Document
from hr.app.models.Job import Job
from hr.app.models.Department import Department
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import joinedload
from flask_sqlalchemy import pagination
# from hr.app.db import db
# from hr.app.models.BloodDonation import BloodDonation
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import desc

class documentRepository:
    @staticmethod
    def add_document_in_db(session:scoped_session,args:dict) -> Document:
        try:
            document = Document(**args)
            session.add(document)
            session.flush()
            return document
        except SQLAlchemyError:
            session.rollback()
            raise

    @staticmethod
    def get_document_by_Id(session:scoped_session,args:dict) -> Document:
        try:
            res = session.query(Document).filter(Document.document_id==args.get("document_id")).first()
            return res
        except SQLAlchemyError:
            raise
    
    # @staticmethod
    # def get_attendence_by_Id2(session:scoped_session,args:dict) -> Attendence:
    #     try:
    #         res = session.query(Attendence).filter(Attendence.attendence_id==args.get("attendence_id")).first()
    #         return res
    #     except SQLAlchemyError:
    #         raise
    # # @staticmethod
    # # def get_employee_by_id_for_all_details(session:scoped_session,args:dict) -> Employee:
    # #     try:
    # #         res =session.query(Employee).\
    # #             filter(Employee.id == args.get("employee_id")).\
    # #             options(joinedload(Employee.jobs), joinedload(Employee.department)).first()
    # #         # res = session.query(Employee).\
    # #         #         join(Job, Employee.job_id == Job.job_id).\
    # #         #         join(Department, Employee.department_id == Department.department_id).\
    # #         #         filter(Employee.id == args.get("employee_id")).\
    # #         #         first()
    # #         return res
    # #     except SQLAlchemyError:
    # #         raise

    
    @staticmethod
    def get_all_document_from_db_by_eid(session:scoped_session,args:dict) -> Document:
        try:
            res = session.query(Document).filter(Document.employee_id==args.get("employee_id")).all()
            return res
        except SQLAlchemyError:
            raise

    # # @staticmethod
    # # def get_employee_by_id(session:scoped_session,args:dict):
    # #     try:
    # #         res = session.query(Employee).filter(Employee.id==args.get("id")).first()
    # #         return res
    # #     except SQLAlchemyError:
    # #         raise
    @staticmethod
    def update_document_in_db(session:scoped_session,check_document:Document,args:dict):
        try:
            check_document.file_path = args.get("file_path")
            check_document.document_type = args.get("document_type")
            check_document.employee_id = args.get("employee_id")
            session.flush()

        except SQLAlchemyError:
            raise