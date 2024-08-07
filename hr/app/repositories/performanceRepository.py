# from sqlalchemy import func
from hr.app.models.Performance import Performance
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

class performanceRepository:
    @staticmethod
    def add_performance_in_db(session:scoped_session,args:dict) -> Performance:
        try:
            performance = Performance(**args)
            session.add(performance)
            session.flush()
            return performance
        except SQLAlchemyError:
            session.rollback()
            raise

    @staticmethod
    def get_performance_by_employee(session:scoped_session,args:dict) -> Performance:
        try:
            res = session.query(Performance).filter(Performance.employee_id==args.get("employee_id")).order_by(desc("performance_id")).paginate(page=args.get("page"),per_page=args.get("per_page"))
            if not res:
                raise IDNotFoundException("employee_id",args.get("employee_id"))
            return res
        
        except SQLAlchemyError:
             raise 
    

    @staticmethod
    def get_performance_by_performance_id(session:scoped_session,args:dict):
        try:
            res = session.query(Performance).filter(Performance.performance_id==args.get("performance_id")).first()
            if not res:
                raise IDNotFoundException("performance_id",args.get("performance_id"))
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
    def update_performance_in_db(session:scoped_session,check_performance:Performance,args:dict):
        try:
            check_performance.score = args.get("score")
            check_performance.feedback = args.get("feedback")
            check_performance.reviewdate = args.get("reviewdate")
            check_performance.employee_id = args.get("employee_id")
            session.flush()

        except SQLAlchemyError:
            raise