# from itertools import count
from flask import jsonify
from hr.app.repositories.employeeRepository import employeeRepository
from hr.app.repositories.jobRepository import jobRepository
from hr.app.repositories.departmentRepository import departmentRepository
# from http import HTTPStatus
from hr.app.db import db
# from flask import request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token


class employeeBLC:
    @staticmethod
    def get_session():
        return db.session

    @staticmethod
    def adding_employee(args:dict):
        session = employeeBLC.get_session()
        check_department = departmentRepository.get_department_by_id_from_db(session=session,args=args)
        if check_department:
            check_job = jobRepository.get_job_by_id(session,args)
            if check_job:
                saving_job = employeeRepository.add_employee_in_db(session,args)
                session.commit()
                return saving_job
            else:
                raise Exception(f"job_id {args.get('job_id')} not found")
        else:
            raise Exception(f"department_id {args.get('department_id')} not found")
    @staticmethod
    def getting_employee(args:dict):
        session = employeeBLC.get_session()
        get_employee_details = employeeRepository.get_employee_by_id_for_all_details(session,args)
        if get_employee_details:
            return get_employee_details
        raise Exception(f"the employee_id {args.get('employee_id')} not found")
    

    @staticmethod
    def getting_all_employee(args:dict):
        session = employeeBLC.get_session()
        getting_employees,total = employeeRepository.get_all_employee_from_db(session,args)
        if getting_employees:
            pages = (total + args.get("per_page") - 1) // args.get("per_page")
            has_next = args.get("page") < pages
            has_prev = args.get("page") > 1

            return {
                'employees': getting_employees,
                'page': args.get("page"),
                'per_page': args.get("per_page"),
                'total': total,
                'pages': pages,
                'has_next': has_next,
                'has_prev': has_prev
            }
            # return getting_employees
        raise Exception("there is no job data is saved in db")
    
    @staticmethod
    def updating_employee(args:dict):
        session = employeeBLC.get_session()
        check_employee = employeeRepository.get_employee_by_id(session,args)
        if check_employee:
            check_department = departmentRepository.get_department_by_id_from_db(session=session,args=args)
            if check_department:
                check_job = jobRepository.get_job_by_id(session,args)
                if check_job:
                    upadte_job = employeeRepository.update_employee_in_db(session,check_employee,args)
                    session.commit()
                    return check_employee
                else:
                    raise Exception(f"job_id {args.get('job_id')} not found")
            else:
                raise Exception(f"department_id {args.get('department_id')} not found")
        else:
            raise Exception(f"employee_id {args.get('id')} not found")

    @staticmethod
    def deleting_employee(args:dict):
        session = employeeBLC.get_session()
        check_employee = employeeRepository.get_employee_by_id(session,args)
        if check_employee:
            session.delete(check_employee)
            session.commit()
            return f"the given job_id {args.get('id')} deleted successfully "
        raise Exception(f"the given job_id {args.get('id')} not found ")
    

    @staticmethod
    def adding_user_details(args:dict):
        session = employeeBLC.get_session()
        user = employeeRepository.save_user_details_in_db(session,args)
        session.commit()
        return user
    
    @staticmethod
    def checking_user(args:dict):
        session = employeeBLC.get_session()
        user= employeeRepository.get_user(session,args)
        if user :
            if user.check_password(args.get("password")):
                additional_claims = {"role": user.role}
                access_token = create_access_token(identity=user.username,additional_claims=additional_claims)
                refresh_token = create_refresh_token(identity=user.username,additional_claims=additional_claims)
                return jsonify(access_token=access_token, refresh_token=refresh_token)
            else:
                return jsonify({"error":"password is invalid"})
        else:
            return jsonify({"error":"email is invalid"})
