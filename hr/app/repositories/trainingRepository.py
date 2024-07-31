# from sqlalchemy import func
from hr.app.models.Training import Training
from hr.app.models.Job import Job
from hr.app.models.Employee import Employee
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import joinedload
from flask_sqlalchemy import pagination
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import desc


class IDNotFoundException(Exception):
    def __init__(self, id_type, id_value):
        self.message = f"{id_type} '{id_value}' not found."
        super().__init__(self.message)

class trainingRepository:
    @staticmethod
    def add_training_in_db(session:scoped_session,args:dict,check_employee:Employee) -> Training:
        try:
            args.pop("employee_id")
            training = Training(**args)
            training.employees.append(check_employee)
            session.add(training)
            session.flush()
            return training
        except SQLAlchemyError:
            session.rollback()
            raise

    @staticmethod
    def get_training_by_employee(session:scoped_session,args:dict) -> Training:
        try:
            res = session.query(Employee).filter(Employee.id==args.get("employee_id")).options(joinedload(Employee.trainings)).all()
            if not res:
                raise IDNotFoundException("employee_id",args.get("employee_id"))
            return res
        
        except SQLAlchemyError:
             raise 
    

    @staticmethod
    def get_training_by_training_id(session:scoped_session,args:dict):
        try:
            res = session.query(Training).filter(Training.training_id==args.get("training_id")).first()
            if not res:
                raise IDNotFoundException("training_id",args.get("training_id"))
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
    def update_training_in_db(session:scoped_session,check_training:Training,args:dict):
        try:
            check_training.date = args.get("date")
            check_training.description = args.get("description")
            check_training.status = args.get("status")
            check_training.training_name = args.get("training_name")
            session.flush()

        except SQLAlchemyError:
            raise