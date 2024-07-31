# from itertools import count
from hr.app.repositories.employeeRepository import employeeRepository
from hr.app.repositories.jobRepository import jobRepository
from hr.app.repositories.departmentRepository import departmentRepository
from hr.app.repositories.performanceRepository import performanceRepository
from hr.app.repositories.trainingRepository import trainingRepository
# from http import HTTPStatus
from hr.app.db import db
# from flask import request, jsonify


class trainingBLC:
    @staticmethod
    def get_session():
        return db.session

    @staticmethod
    def adding_training(args:dict):
        session = trainingBLC.get_session()
        check_employee = employeeRepository.get_employee_by_id2(session=session,args=args)
        if check_employee: 
                save_training = trainingRepository.add_training_in_db(session,args,check_employee)
                session.commit()
                return save_training
        else:
            raise Exception(f"employee_id {args.get('employee_id')} not found")
    @staticmethod
    def getting_training(args:dict):
        session = trainingBLC.get_session()
        if "employee_id" in args:
            get_training = trainingRepository.get_training_by_employee(session,args)
        elif "training_id" in args:
            get_training = trainingRepository.get_training_by_training_id(session,args)
        return get_training
    

    # @staticmethod
    # def getting_all_employee_documents(args:dict):
    #     session = documentBLC.get_session()
    #     getting_documents = documentRepository.get_all_document_from_db_by_eid(session,args)
    #     if getting_documents:
    #             page = args.get('page')
    #             per_page = args.get('per_page')
    #             total = len(getting_documents)
    #             total_pages = (total + per_page - 1) // per_page
                
    #             # Get the items for the current page
    #             start = (page - 1) * per_page
    #             end = start + per_page
    #             items = getting_documents[start:end]
    #             return {
    #                         'page': page,
    #                         'per_page': per_page,
    #                         'total': total,
    #                         'total_pages': total_pages,
    #                         'items': items
    #                     }
    #         # return getting_employees
    #     raise Exception("there is no documents data is saved in db")
    
    @staticmethod
    def updating_training(args:dict):
        session = trainingBLC.get_session()
        
        check_training = trainingRepository.get_training_by_training_id(session,args)
        if check_training:
            upadte_training = trainingRepository.update_training_in_db(session,check_training,args)
            session.commit()
            return check_training
        else:
            raise Exception(f"training_id {args.get('training_id')} not found")

    @staticmethod
    def deleting_training(args:dict):
        session = trainingBLC.get_session()
        check_training = trainingRepository.get_training_by_training_id(session,args)
        if check_training:
            session.delete(check_training)
            session.commit()
            return f"the given training_id {args.get('training_id')} deleted successfully "
        raise Exception(f"the given training_id {args.get('training_id')} not found ")