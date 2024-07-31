# from itertools import count
from hr.app.repositories.employeeRepository import employeeRepository
from hr.app.repositories.jobRepository import jobRepository
from hr.app.repositories.departmentRepository import departmentRepository
from hr.app.repositories.payrollRepository import payrollRepository
# from http import HTTPStatus
from hr.app.db import db
# from flask import request, jsonify


class payrollBLC:
    @staticmethod
    def get_session():
        return db.session

    @staticmethod
    def adding_payroll(args:dict):
        session = payrollBLC.get_session()
        check_employee = employeeRepository.get_employee_by_id2(session=session,args=args)
        if check_employee:
                save_payroll = payrollRepository.add_payroll_in_db(session,args)
                session.commit()
                return save_payroll
        else:
            raise Exception(f"employee_id {args.get('employee_id')} not found")
    @staticmethod
    def getting_payroll(args:dict):
        session = payrollBLC.get_session()
        if "employee_id" in args:
            get_payroll = payrollRepository.get_payroll_by_employee(session,args)
        elif "payroll_id" in args:
            get_payroll = payrollRepository.get_payroll_by_payroll_id(session,args)
        return get_payroll
    

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
    def updating_payroll(args:dict):
        session = payrollBLC.get_session()
        check_employee = employeeRepository.get_employee_by_id2(session,args)
        if check_employee:
            check_payroll = payrollRepository.get_payroll_by_payroll_id(session,args)
            if check_payroll:
                upadte_payroll = payrollRepository.update_payroll_in_db(session,check_payroll,args)
                session.commit()
                return check_payroll
            else:
                raise Exception(f"payroll_id {args.get('payroll_id')} not found")
        else:
            raise Exception(f"employee_id {args.get('employee_id')} not found")

    @staticmethod
    def deleting_payroll(args:dict):
        session = payrollBLC.get_session()
        check_payroll = payrollRepository.get_payroll_by_payroll_id(session,args)
        if check_payroll:
            session.delete(check_payroll)
            session.commit()
            return f"the given payroll_id {args.get('payroll_id')} deleted successfully "
        raise Exception(f"the given payroll_id {args.get('payroll_id')} not found ")