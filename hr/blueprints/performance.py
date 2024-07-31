from flask import request, jsonify
from webargs.flaskparser import use_args
from hr.app.schemas.performanceSchema import EmployeeperformanceSchema, performanceSchema, update_performance_schema
from functools import wraps
from flask import Blueprint
from marshmallow import fields,validate

from hr.app.db import db
from hr.app.repositories.performanceRepository import performanceRepository
# from marshmallow import fields, Schema, validate
from hr.app.bl.performanceBLC import performanceBLC
from http import HTTPStatus
# from flask_jwt_extended import jwt_required

bp = Blueprint("performance", __name__)


@bp.route("/add_performance",methods=["POST"])
@use_args(performanceSchema,location="json")
def add_performance(args:dict):
    try:
        performance = performanceBLC.adding_performance(args)
        schema = performanceSchema()
        res = schema.dump(performance)
        return res,HTTPStatus.OK
    except Exception as e:
        return jsonify({"message":str(e)}),HTTPStatus.UNPROCESSABLE_ENTITY


@bp.route("/get_performance",methods=["GET"])
@use_args(EmployeeperformanceSchema,location="query")
def get_performance(args):
    try:
        performance = performanceBLC.getting_performance(args)
        if "employee_id" in args:
            schema = performanceSchema(many=True)
            res = schema.dump(performance)
            return res,HTTPStatus.OK
        elif "performance_id" in args:
            schema= performanceSchema()
            res = schema.dump(performance)
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


@bp.route("/update_performance",methods=["PUT"])
@use_args(update_performance_schema,location="json")
def update_performance(args:dict):
    try:
        updating_performance =performanceBLC.updating_performance(args)
        schema = update_performance_schema()
        res = schema.dump(updating_performance)
        return res,HTTPStatus.OK
    except Exception as e:
        return jsonify({"error":str(e)}),HTTPStatus.UNPROCESSABLE_ENTITY

@bp.route("/delete_performance",methods=["DELETE"])
@use_args({"performance_id":fields.Integer(required=True,validate=validate.Range(min=1,error="page must be a positive integer"))},location="query")
def delete_benefit(args:dict):
    try:
        performance_deleted = performanceBLC.deleting_performance(args)
        return jsonify({"message":performance_deleted}),HTTPStatus.OK
    except Exception as e:
        return jsonify({"error":str(e)}),HTTPStatus.UNPROCESSABLE_ENTITY