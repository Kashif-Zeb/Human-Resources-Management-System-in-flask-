# from itertools import count
from hr.app.repositories.employeeRepository import employeeRepository
from hr.app.repositories.jobRepository import jobRepository
from hr.app.repositories.departmentRepository import departmentRepository
from hr.app.repositories.performanceRepository import performanceRepository
# from http import HTTPStatus
from hr.app.db import db
# from flask import request, jsonify


class performanceBLC:
    @staticmethod
    def get_session():
        return db.session

    @staticmethod
    def adding_performance(args:dict):
        session = performanceBLC.get_session()
        check_employee = employeeRepository.get_employee_by_id2(session=session,args=args)
        if check_employee:
                save_performance = performanceRepository.add_performance_in_db(session,args)
                session.commit()
                return save_performance
        else:
            raise Exception(f"employee_id {args.get('employee_id')} not found")
    @staticmethod
    def getting_performance(args:dict):
        session = performanceBLC.get_session()
        if "employee_id" in args:
            get_performance = performanceRepository.get_performance_by_employee(session,args)
        elif "performance_id" in args:
            get_performance = performanceRepository.get_performance_by_performance_id(session,args)
        return get_performance
    

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
    def updating_performance(args:dict):
        session = performanceBLC.get_session()
        check_employee = employeeRepository.get_employee_by_id2(session,args)
        if check_employee:
            check_performance = performanceRepository.get_performance_by_performance_id(session,args)
            if check_performance:
                upadte_performance = performanceRepository.update_performance_in_db(session,check_performance,args)
                session.commit()
                return check_performance
            else:
                raise Exception(f"performance_id {args.get('performance_id')} not found")
        else:
            raise Exception(f"employee_id {args.get('employee_id')} not found")

    @staticmethod
    def deleting_performance(args:dict):
        session = performanceBLC.get_session()
        check_performance = performanceRepository.get_performance_by_performance_id(session,args)
        if check_performance:
            session.delete(check_performance)
            session.commit()
            return f"the given performance_id {args.get('performance_id')} deleted successfully "
        raise Exception(f"the given performance_id {args.get('performance_id')} not found ")