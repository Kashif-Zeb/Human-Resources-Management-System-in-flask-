from flask import request, jsonify
from webargs.flaskparser import use_args
from hr.app.schemas.benefitSchema import EmployeeBenefitSchema, benefitSchema, update_benefit_schema
from functools import wraps
from flask import Blueprint
from marshmallow import fields,validate

from hr.app.db import db
from hr.app.repositories.benefitRepository import benefitRepository
# from marshmallow import fields, Schema, validate
from hr.app.bl.benefitBLC import benefitBLC
from http import HTTPStatus
# from flask_jwt_extended import jwt_required

bp = Blueprint("benefit", __name__)


@bp.route("/add_benefit",methods=["POST"])
@use_args(benefitSchema,location="json")
def add_benefit(args:dict):
    try:
        benefit = benefitBLC.adding_benefit(args)
        schema = benefitSchema()
        res = schema.dump(benefit)
        return res,HTTPStatus.OK
    except Exception as e:
        return jsonify({"message":str(e)}),HTTPStatus.UNPROCESSABLE_ENTITY


@bp.route("/get_benefit",methods=["GET"])
@use_args(EmployeeBenefitSchema,location="query")
def get_benefit(args):
    try:
        benefit = benefitBLC.getting_benefit(args)
        if "employee_id" in args:
            schema = benefitSchema(many=True)
            res = schema.dump(benefit)
            return res,HTTPStatus.OK
        elif "benefit_id" in args:
            schema= benefitSchema()
            res = schema.dump(benefit)
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


@bp.route("/update_benefit",methods=["PUT"])
@use_args(update_benefit_schema,location="json")
def update_benefit(args:dict):
    try:
        updating_employee =benefitBLC.updating_benefit(args)
        schema = update_benefit_schema()
        res = schema.dump(updating_employee)
        return res,HTTPStatus.OK
    except Exception as e:
        return jsonify({"error":str(e)}),HTTPStatus.UNPROCESSABLE_ENTITY

@bp.route("/delete_benefit",methods=["DELETE"])
@use_args({"benefit_id":fields.Integer(required=True,validate=validate.Range(min=1,error="page must be a positive integer"))},location="query")
def delete_benefit(args:dict):
    try:
        document_deleted = benefitBLC.deleting_benefit(args)
        return jsonify({"message":document_deleted}),HTTPStatus.OK
    except Exception as e:
        return jsonify({"error":str(e)}),HTTPStatus.UNPROCESSABLE_ENTITY