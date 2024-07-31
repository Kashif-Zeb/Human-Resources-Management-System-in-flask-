from flask import request, jsonify
from webargs.flaskparser import use_args
# from hr.app.schemas.StaffSchema import (
#     Login,
#     StaffSchema,
#     update_schema_staff,
#     RegisterationSchema,
# )
from functools import wraps
from flask import Blueprint

from hr.app.db import db
from hr.app.repositories.departmentRepository import departmentRepository
from marshmallow import fields, Schema, validate
from hr.app.bl.departmentBLC import departmentBLC
from http import HTTPStatus
# from flask_jwt_extended import jwt_required
from hr.app.schemas.departmentSchema import DepartmentSchema, DepartmentSchema_for_update
bp = Blueprint("department", __name__)

@bp.route("/add_department",methods=["POST"])
@use_args(DepartmentSchema,location="json")
def add_department(args:dict):
    try:
        department = departmentBLC.adding_department(args)
        schema = DepartmentSchema()
        result = schema.dump(department)
        return result,HTTPStatus.OK
    except Exception as e:
        return jsonify(str(e)),HTTPStatus.UNPROCESSABLE_ENTITY

@bp.route("/get_department_by_id",methods=["GET"])
@use_args({"department_id":fields.Integer(required=True,validate=validate.Range(min=1,error="department_id must be a positive integer"))},location="query")
def get_department_by_id(args:dict):
    try:
        department = departmentBLC.getting_department_by_id(args)
        schema = DepartmentSchema()
        result = schema.dump(department)
        return result,HTTPStatus.OK
    except Exception as e:
        return jsonify(str(e)),HTTPStatus.UNPROCESSABLE_ENTITY
    

@bp.route("/get_all_department",methods=["GET"])
def get_all_department():
    try:
        departments = departmentBLC.getting_all_department()
        schema  = DepartmentSchema(many=True)
        result = schema.dump(departments)
        return result,HTTPStatus.OK
    except Exception as e:
        return jsonify(str(e)),HTTPStatus.UNPROCESSABLE_ENTITY
    


@bp.route("/update_department",methods=["PUT"])
@use_args(DepartmentSchema_for_update,location="json")
def update_department(args:dict):
    try:
        updated = departmentBLC.updating_the_department(args)
        schema = DepartmentSchema()
        result = schema.dump(updated)
        return result,HTTPStatus.OK
    except Exception as e:
        return jsonify(str(e)),HTTPStatus.UNPROCESSABLE_ENTITY
    
@bp.route("/delete_department",methods=["DELETE"])
@use_args({"department_id":fields.Integer(required=True,validate=validate.Range(min=1,error="department_id must be a positive integer"))},location="query")
def delete_department(args:dict):
    try:
        result = departmentBLC.deleting_the_department(args)
        return jsonify(result),HTTPStatus.OK
    except Exception as e:
            return jsonify(str(e)),HTTPStatus.UNPROCESSABLE_ENTITY