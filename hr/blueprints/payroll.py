from flask import request, jsonify
from webargs.flaskparser import use_args
from hr.app.schemas.payrollSchema import EmployeepayrollSchema, payrollSchema, update_payroll_schema
from functools import wraps
from flask import Blueprint
from marshmallow import fields,validate

from hr.app.db import db
from hr.app.repositories.payrollRepository import payrollRepository
# from marshmallow import fields, Schema, validate
from hr.app.bl.payrollBLC import payrollBLC
from http import HTTPStatus
# from flask_jwt_extended import jwt_required

bp = Blueprint("payroll", __name__)


@bp.route("/add_payroll",methods=["POST"])
@use_args(payrollSchema,location="json")
def add_payroll(args:dict):
    try:
        payroll = payrollBLC.adding_payroll(args)
        schema = payrollSchema()
        res = schema.dump(payroll)
        return res,HTTPStatus.OK
    except Exception as e:
        return jsonify({"message":str(e)}),HTTPStatus.UNPROCESSABLE_ENTITY


@bp.route("/get_payroll",methods=["GET"])
@use_args(EmployeepayrollSchema,location="query")
def get_payroll(args):
    try:
        payroll = payrollBLC.getting_payroll(args)
        if "employee_id" in args:
            schema = payrollSchema(many=True)
            res = schema.dump(payroll)
            return res,HTTPStatus.OK
        elif "payroll_id" in args:
            schema= payrollSchema()
            res = schema.dump(payroll)
            return res,HTTPStatus.OK
    except Exception as e:
        return jsonify({"message":str(e)}),HTTPStatus.UNPROCESSABLE_ENTITY


# @bp.route("/get_all_employee_documents",methods=["GET"])
# @use_args({"employee_id":fields.Integer(required=True,validate=validate.Range(min=1,error="employee_id must be a positive integer")),
#     "page":fields.Integer(required=True,validate=validate.Range(min=1,error="page must be a positive integer")),
#            "per_page":fields.Integer(required=True,validate=validate.Range(min=1,error="per_page must be a positive integer"))},location="query")
# def get_all_employee_documents(args:dict):
#     try:
#         employess = documentBLC.getting_all_employee_documents(args)
#         get_emp = employess["items"]
#         schema = documentSchema(many=True)
#         res = schema.dump(get_emp)
#         response = {
#             'documents': res,
#             'page': employess['page'],
#             'per_page': employess['per_page'],
#             'total_pages': employess['total_pages'],
#             'total': employess['total'],
#         }
#         return response,HTTPStatus.OK
#     except Exception as e:
#         return jsonify({"error":str(e)}),HTTPStatus.UNPROCESSABLE_ENTITY


@bp.route("/update_payroll",methods=["PUT"])
@use_args(update_payroll_schema,location="json")
def update_payroll(args:dict):
    try:
        updating_payroll =payrollBLC.updating_payroll(args)
        schema = update_payroll_schema()
        res = schema.dump(updating_payroll)
        return res,HTTPStatus.OK
    except Exception as e:
        return jsonify({"error":str(e)}),HTTPStatus.UNPROCESSABLE_ENTITY

@bp.route("/delete_payroll",methods=["DELETE"])
@use_args({"payroll_id":fields.Integer(required=True,validate=validate.Range(min=1,error="page must be a positive integer"))},location="query")
def delete_benefit(args:dict):
    try:
        payroll_deleted = payrollBLC.deleting_payroll(args)
        return jsonify({"message":payroll_deleted}),HTTPStatus.OK
    except Exception as e:
        return jsonify({"error":str(e)}),HTTPStatus.UNPROCESSABLE_ENTITY