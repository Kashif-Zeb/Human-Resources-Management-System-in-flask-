from flask import request, jsonify
from webargs.flaskparser import use_args
from hr.app.schemas.performanceSchema import EmployeeperformanceSchema, performanceSchema, update_performance_schema
from functools import wraps
from hr.app.schemas.trainingSchema import EmployeetrainingSchema, getting_training_with_employee, trainingSchema, update_training_schema
from flask import Blueprint
from marshmallow import fields,validate

from hr.app.db import db
from hr.app.repositories.performanceRepository import performanceRepository
from hr.app.repositories.trainingRepository import trainingRepository
# from marshmallow import fields, Schema, validate
from hr.app.bl.performanceBLC import performanceBLC
from hr.app.bl.trainingBLC import trainingBLC
from http import HTTPStatus
# from flask_jwt_extended import jwt_required

bp = Blueprint("training", __name__)


@bp.route("/add_training",methods=["POST"])
@use_args(trainingSchema,location="json")
def add_training(args:dict):
    try:
        training = trainingBLC.adding_training(args)
        schema = trainingSchema()
        res = schema.dump(training)
        return res,HTTPStatus.OK
    except Exception as e:
        return jsonify({"message":str(e)}),HTTPStatus.UNPROCESSABLE_ENTITY


@bp.route("/get_training",methods=["GET"])
@use_args(EmployeetrainingSchema,location="query")
def get_training(args):
    try:
        training = trainingBLC.getting_training(args)
        if "employee_id" in args:
            schema = getting_training_with_employee(many=True)
            res = schema.dump(training)
            return res,HTTPStatus.OK
        elif "training_id" in args:
            schema= trainingSchema()
            res = schema.dump(training)
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


@bp.route("/update_training",methods=["PUT"])
@use_args(update_training_schema,location="json")
def update_training(args:dict):
    try:
        updating_training =trainingBLC.updating_training(args)
        schema = update_training_schema()
        res = schema.dump(updating_training)
        return res,HTTPStatus.OK
    except Exception as e:
        return jsonify({"error":str(e)}),HTTPStatus.UNPROCESSABLE_ENTITY

@bp.route("/delete_training",methods=["DELETE"])
@use_args({"training_id":fields.Integer(required=True,validate=validate.Range(min=1,error="training_id must be a positive integer"))},location="query")
def delete_training(args:dict):
    try:
        training_deleted = trainingBLC.deleting_training(args)
        return jsonify({"message":training_deleted}),HTTPStatus.OK
    except Exception as e:
        return jsonify({"error":str(e)}),HTTPStatus.UNPROCESSABLE_ENTITY