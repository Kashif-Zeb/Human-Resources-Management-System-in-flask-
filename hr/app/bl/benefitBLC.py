# from itertools import count
from hr.app.repositories.employeeRepository import employeeRepository
from hr.app.repositories.jobRepository import jobRepository
from hr.app.repositories.departmentRepository import departmentRepository
from hr.app.repositories.benefitRepository import benefitRepository
# from http import HTTPStatus
from hr.app.db import db
# from flask import request, jsonify


class benefitBLC:
    @staticmethod
    def get_session():
        return db.session

    @staticmethod
    def adding_benefit(args:dict):
        session = benefitBLC.get_session()
        check_employee = employeeRepository.get_employee_by_id2(session=session,args=args)
        if check_employee:
                save_benefit = benefitRepository.add_benefit_in_db(session,args)
                session.commit()
                return save_benefit
        else:
            raise Exception(f"employee_id {args.get('employee_id')} not found")
    @staticmethod
    def getting_benefit(args:dict):
        session = benefitBLC.get_session()
        if "employee_id" in args:
            get_benefit = benefitRepository.get_benefit_by_employee(session,args)
        elif "benefit_id" in args:
            get_benefit = benefitRepository.get_benefit_by_benefit_id(session,args)
        return get_benefit
    

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
    def updating_benefit(args:dict):
        session = benefitBLC.get_session()
        check_employee = employeeRepository.get_employee_by_id2(session,args)
        if check_employee:
            check_benefit = benefitRepository.get_benefit_by_benefit_id(session,args)
            if check_benefit:
                upadte_benefit = benefitRepository.update_benefit_in_db(session,check_benefit,args)
                session.commit()
                return check_benefit
            else:
                raise Exception(f"document_id {args.get('benefit_id')} not found")
        else:
            raise Exception(f"employee_id {args.get('employee_id')} not found")

    @staticmethod
    def deleting_benefit(args:dict):
        session = benefitBLC.get_session()
        check_benefit = benefitRepository.get_benefit_by_benefit_id(session,args)
        if check_benefit:
            session.delete(check_benefit)
            session.commit()
            return f"the given benefit_id {args.get('benefit_id')} deleted successfully "
        raise Exception(f"the given benefit_id {args.get('benefit_id')} not found ")