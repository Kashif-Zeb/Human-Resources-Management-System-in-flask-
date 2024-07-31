# from itertools import count
from hr.app.repositories.employeeRepository import employeeRepository
from hr.app.repositories.jobRepository import jobRepository
from hr.app.repositories.departmentRepository import departmentRepository
from hr.app.repositories.documentRepository import documentRepository
# from http import HTTPStatus
from hr.app.db import db
# from flask import request, jsonify


class documentBLC:
    @staticmethod
    def get_session():
        return db.session

    @staticmethod
    def adding_document(args:dict):
        session = documentBLC.get_session()
        check_employee = employeeRepository.get_employee_by_id2(session=session,args=args)
        if check_employee:
                save_document = documentRepository.add_document_in_db(session,args)
                session.commit()
                return save_document
        else:
            raise Exception(f"employee_id {args.get('employee_id')} not found")
    @staticmethod
    def getting_document(args:dict):
        session = documentBLC.get_session()
        get_document = documentRepository.get_document_by_Id(session,args)
        if get_document:
            return get_document
        raise Exception(f"the document_id {args.get('document_id')} not found")
    

    @staticmethod
    def getting_all_employee_documents(args:dict):
        session = documentBLC.get_session()
        getting_documents = documentRepository.get_all_document_from_db_by_eid(session,args)
        if getting_documents:
                page = args.get('page')
                per_page = args.get('per_page')
                total = len(getting_documents)
                total_pages = (total + per_page - 1) // per_page
                
                # Get the items for the current page
                start = (page - 1) * per_page
                end = start + per_page
                items = getting_documents[start:end]
                return {
                            'page': page,
                            'per_page': per_page,
                            'total': total,
                            'total_pages': total_pages,
                            'items': items
                        }
            # return getting_employees
        raise Exception("there is no documents data is saved in db")
    
    @staticmethod
    def updating_document(args:dict):
        session = documentBLC.get_session()
        check_employee = employeeRepository.get_employee_by_id2(session,args)
        if check_employee:
            check_document = documentRepository.get_document_by_Id(session,args)
            if check_document:
                upadte_attendence = documentRepository.update_document_in_db(session,check_document,args)
                session.commit()
                return check_document
            else:
                raise Exception(f"document_id {args.get('document_id')} not found")
        else:
            raise Exception(f"employee_id {args.get('employee_id')} not found")

    @staticmethod
    def deleting_document(args:dict):
        session = documentBLC.get_session()
        check_document = documentRepository.get_document_by_Id(session,args)
        if check_document:
            session.delete(check_document)
            session.commit()
            return f"the given document_id {args.get('document_id')} deleted successfully "
        raise Exception(f"the given document_id {args.get('document_id')} not found ")