# from sqlalchemy import func
from hr.app.models.Job import Job
from sqlalchemy.orm import scoped_session
# from hr.app.db import db
# from hr.app.models.BloodDonation import BloodDonation
from sqlalchemy.exc import SQLAlchemyError

class jobRepository:
    @staticmethod
    def add_job_in_db(session:scoped_session,args:dict) -> Job:
        try:
            job = Job(**args)
            session.add(job)
            session.flush()
            return job
        except SQLAlchemyError:
            session.rollback()
            raise

    
    @staticmethod
    def get_job_by_id(session:scoped_session,args:dict) -> Job:
        try:
            res = session.query(Job).filter(Job.job_id==args.get("job_id")).first()
            return res
        except SQLAlchemyError:
            raise

    
    @staticmethod
    def get_all_job_from_db(session:scoped_session) -> Job:
        try:
            res = session.query(Job).all()
            return res
        except SQLAlchemyError:
            raise

    

    @staticmethod
    def update_the_job_in_db(session:scoped_session,args:dict,check_job:Job):
        try:
            check_job.name = args.get("name")
            check_job.description = args.get("description")
            check_job.salary_range = args.get("salary_range")
            session.flush()

        except SQLAlchemyError:
            raise