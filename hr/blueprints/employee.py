from flask import request, jsonify,after_this_request,g
from webargs.flaskparser import use_args
from hr.app.schemas.employeeSchema import employee_details_with_DJ, employee_khan, employee_path, employeeSchema, hybrid, mm, update_employee
from functools import wraps
from flask import Blueprint
from marshmallow import fields,validate
from hr.app.schemas.userSchema import userSchema
from hr.app.db import db
from hr.app.repositories.employeeRepository import employeeRepository
# from marshmallow import fields, Schema, validate
from hr.app.bl.employeeBLC import employeeBLC
from http import HTTPStatus
from flask_jwt_extended import jwt_required,JWTManager,decode_token
from functools import wraps
from hr.tasks import file
from hr.app.models.Path import Path
from hr.signals import user_logged_in
from hr.limiters import limiter
bp = Blueprint("employee", __name__)

# def after_this_request(func):
#     if not hasattr(g, 'call_after_request'):
#         g.call_after_request = []
#     g.call_after_request.append(func)
#     return func

def get_role_from_token():
    header = request.headers.get("Authorization")
    if header is None:
        return None
    raw_token = header.split(" ")[-1]
    decode  =  decode_token(raw_token)
    role = decode.get("role")

    return role
def roles_deco(required_role):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(*args,**kwargs):
            role = get_role_from_token()
            if role in required_role:
                return view_func(*args,**kwargs)
            else:
                return jsonify({"message":"your are not authorization to access this api"}),HTTPStatus.FORBIDDEN
        return wrapper
    return decorator

def higherrole(view_func):
    return roles_deco(required_role=["ceo","director","cio","cto","employee"])(view_func)
def lowrole(view_func):
    return roles_deco(required_role=["employee"])(view_func)



@bp.route("/register",methods=["POST"])
@use_args(userSchema,location="json")
def register(args:dict):
    try:
        user =employeeBLC.adding_user_details(args)
        return jsonify({"message":"you registered successfully"}),HTTPStatus.CREATED
    except Exception as e:
        return jsonify({"message":str(e)}),HTTPStatus.UNPROCESSABLE_ENTITY

@bp.route("/login",methods=["POST"])
@use_args({"email":fields.Email(required=True),
           "password":fields.String(required=True)},location="json")
def login(args):
    try:
        access_token,refresh_token,user =employeeBLC.checking_user(args)
        @after_this_request
        def sig(response):
            user_logged_in.send(None,username=user.username)
            return response
        print("returninnggggggggg")
        return jsonify({"access_token":access_token,"refresh_token":refresh_token}),HTTPStatus.OK
    except Exception as e:
        return jsonify({"message":str(e)}),HTTPStatus.UNPROCESSABLE_ENTITY

@bp.route("/add_employee",methods=["POST"])
@use_args(employeeSchema,location="json")
def add_employee(args:dict):
    try:
        employee = employeeBLC.adding_employee(args)
        schema = employeeSchema()
        res = schema.dump(employee)
        return res,HTTPStatus.OK
    except Exception as e:
        return jsonify({"message":str(e)}),HTTPStatus.UNPROCESSABLE_ENTITY


@bp.route("/get_employee_by_id",methods=["GET"])
@jwt_required()
@higherrole
@limiter.limit("2 per minute")
@use_args({"employee_id":fields.Integer(required=True,validate=validate.Range(min=1,error="employee_id must be a positive integer"))},location="query")
def get_employee_by_id(args):
    # try:
        employee = employeeBLC.getting_employee(args)
        schema = employee_details_with_DJ()
        res = schema.dump(employee)
        file.delay(res)
        return res,HTTPStatus.OK
    # except Exception as e:
    #     return jsonify({"message":str(e)}),HTTPStatus.UNPROCESSABLE_ENTITY


@bp.route("/get_all_employee",methods=["GET"])
@jwt_required()
@use_args({"page":fields.Integer(required=True,validate=validate.Range(min=1,error="page must be a positive integer")),
           "per_page":fields.Integer(required=True,validate=validate.Range(min=1,error="per_page must be a positive integer"))},location="query")
def get_all_employee(args:dict):
    try:
        employess = employeeBLC.getting_all_employee(args)
        get_emp = employess["employees"]
        schema = employee_details_with_DJ(many=True)
        res = schema.dump(get_emp)
        response = {
            'employees': res,
            'page': employess['page'],
            'per_page': employess['per_page'],
            'total': employess['total'],
            'pages': employess['pages'],
            'has_next': employess['has_next'],
            'has_prev': employess['has_prev']
        }
        return response,HTTPStatus.OK
    except Exception as e:
        return jsonify({"error":str(e)}),HTTPStatus.UNPROCESSABLE_ENTITY


@bp.route("/update_employee",methods=["PUT"])
@use_args(update_employee,location="json")
def updateing_employee(args:dict):
    try:
        updating_employee =employeeBLC.updating_employee(args)
        schema = update_employee()
        res = schema.dump(updating_employee)
        return res,HTTPStatus.OK
    except Exception as e:
        return jsonify({"error":str(e)}),HTTPStatus.UNPROCESSABLE_ENTITY

@bp.route("/delete_employee",methods=["DELETE"])
@use_args({"id":fields.Integer(required=True,validate=validate.Range(min=1,error="page must be a positive integer"))},location="query")
def delete_employee(args:dict):
    try:
        employee_deleted = employeeBLC.deleting_employee(args)
        return jsonify({"message":employee_deleted}),HTTPStatus.OK
    except Exception as e:
        return jsonify({"error":str(e)}),HTTPStatus.UNPROCESSABLE_ENTITY
@bp.route("/get_employee_with_path",methods=["GET"])
@use_args({"employee_id":fields.Integer()},location="query")
def getting_employee_with(args):
    with_path  = employeeBLC.get_employee_with_path(args)
    schema = hybrid(many=True)
    # serialized_data = [schema.serialize(item) for item in with_path]
    res = schema.dump(with_path)
    return jsonify(res)