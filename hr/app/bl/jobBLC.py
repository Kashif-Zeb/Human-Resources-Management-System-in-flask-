# from itertools import count
from hr.app.repositories.jobRepository import jobRepository
# from http import HTTPStatus
from hr.app.db import db
# from flask import request, jsonify


class jobBLC:
    @staticmethod
    def get_session():
        return db.session

    @staticmethod
    def adding_job(args:dict):
        session = jobBLC.get_session()
        saving_job = jobRepository.add_job_in_db(session,args)
        session.commit()
        return saving_job
    
    @staticmethod
    def getting_department_by_id(args:dict):
        session = jobBLC.get_session()
        get_job = jobRepository.get_job_by_id(session,args)
        if get_job:
            return get_job
        raise Exception(f"the job_id {args.get('job_id')} not found")
    

    @staticmethod
    def getting_all_jobs():
        session = jobBLC.get_session()
        getting_job = jobRepository.get_all_job_from_db(session)
        if getting_job:
            return getting_job
        raise Exception("there is no job data is saved in db")
    
    @staticmethod
    def updating_the_job(args:dict):
        session = jobBLC.get_session()
        check_job = jobRepository.get_job_by_id(session,args)
        if check_job:
            jobRepository.update_the_job_in_db(session,args,check_job)
            session.commit()
            return check_job
        raise Exception(f"the given job_id {args.get('job_id')} not found ")
    

    @staticmethod
    def deleting_the_job(args:dict):
        session = jobBLC.get_session()
        check_job = jobRepository.get_job_by_id(session,args)
        if check_job:
            session.delete(check_job)
            session.commit()
            return f"the given job_id {args.get('job_id')} deleted successfully "
        raise Exception(f"the given job_id {args.get('job_id')} not found ")