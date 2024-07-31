# from itertools import count
from hr.app.repositories.employeeRepository import employeeRepository
from hr.app.repositories.jobRepository import jobRepository
from hr.app.repositories.departmentRepository import departmentRepository
from hr.app.repositories.attendenceRepository import attendenceRepository
# from http import HTTPStatus
from hr.app.db import db
# from flask import request, jsonify


class attendenceBLC:
    @staticmethod
    def get_session():
        return db.session

    @staticmethod
    def adding_attendence(args:dict):
        session = attendenceBLC.get_session()
        check_employee = employeeRepository.get_employee_by_id2(session=session,args=args)
        if check_employee:
                saving_attendence = attendenceRepository.add_attendence_in_db(session,args)
                session.commit()
                return saving_attendence
        else:
            raise Exception(f"employee_id {args.get('employee_id')} not found")
    @staticmethod
    def getting_attendence(args:dict):
        session = attendenceBLC.get_session()
        get_attendence = attendenceRepository.get_attendence_by_Id(session,args)
        if get_attendence:
            return get_attendence
        raise Exception(f"the employee_id {args.get('employee_id')} not found")
    

    # @staticmethod
    # def getting_all_employee(args:dict):
    #     session = employeeBLC.get_session()
    #     getting_employees,total = employeeRepository.get_all_employee_from_db(session,args)
    #     if getting_employees:
    #         pages = (total + args.get("per_page") - 1) // args.get("per_page")
    #         has_next = args.get("page") < pages
    #         has_prev = args.get("page") > 1

    #         return {
    #             'employees': getting_employees,
    #             'page': args.get("page"),
    #             'per_page': args.get("per_page"),
    #             'total': total,
    #             'pages': pages,
    #             'has_next': has_next,
    #             'has_prev': has_prev
    #         }
    #         # return getting_employees
    #     raise Exception("there is no job data is saved in db")
    
    @staticmethod
    def updating_the_attendence(args:dict):
        session = attendenceBLC.get_session()
        check_employee = employeeRepository.get_employee_by_id2(session,args)
        if check_employee:
            check_attendence = attendenceRepository.get_attendence_by_Id2(session,args)
            if check_attendence:
                upadte_attendence = attendenceRepository.update_attendence_in_db(session,check_attendence,args)
                session.commit()
                return check_attendence
            else:
                raise Exception(f"attendence_id {args.get('attendence_id')} not found")
        else:
            raise Exception(f"employee_id {args.get('employee_id')} not found")

    @staticmethod
    def deleting_the_attendence(args:dict):
        session = attendenceBLC.get_session()
        check_attendence = attendenceRepository.get_attendence_by_Id2(session,args)
        if check_attendence:
            session.delete(check_attendence)
            session.commit()
            return f"the given attendence_id {args.get('attendence_id')} deleted successfully "
        raise Exception(f"the given attendence_id {args.get('attendence_id')} not found ")