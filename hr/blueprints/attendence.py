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
from hr.app.repositories.attendenceRepository import attendenceRepository
from marshmallow import fields, Schema, validate
from hr.app.bl.attendenceBLC import attendenceBLC
from http import HTTPStatus
# from flask_jwt_extended import jwt_required
from hr.app.schemas.attendenceSchema import attendenceSchema, update_attendence_schema
bp = Blueprint("attendence", __name__)

@bp.route("/add_attendence",methods=["POST"])
@use_args(attendenceSchema,location="json")
def add_job(args:dict):
    try:
        attendence = attendenceBLC.adding_attendence(args)
        schema = attendenceSchema()
        result = schema.dump(attendence)
        return result,HTTPStatus.CREATED
    except Exception as e:
        return jsonify(str(e)),HTTPStatus.UNPROCESSABLE_ENTITY

@bp.route("/get_attendence_by_id",methods=["GET"])
@use_args({"employee_id":fields.Integer(required=True,validate=validate.Range(min=1,error="employee_id must be a positive integer"))},location="query")
def get_job_by_id(args:dict):
    try:
        attendence = attendenceBLC.getting_attendence(args)
        schema = attendenceSchema(many=True)
        result = schema.dump(attendence)
        return result,HTTPStatus.OK
    except Exception as e:
        return jsonify(str(e)),HTTPStatus.UNPROCESSABLE_ENTITY
    

# @bp.route("/get_all_job",methods=["GET"])
# def get_all_job():
#     try:
#         departments = jobBLC.getting_all_jobs()
#         schema  = JobSchema(many=True)
#         result = schema.dump(departments)
#         return result,HTTPStatus.OK
#     except Exception as e:
#         return jsonify(str(e)),HTTPStatus.UNPROCESSABLE_ENTITY
    


@bp.route("/update_attendece",methods=["PUT"])
@use_args(update_attendence_schema,location="json")
def update_department(args:dict):
    try:
        updated = attendenceBLC.updating_the_attendence(args)
        schema = update_attendence_schema()
        result = schema.dump(updated)
        return result,HTTPStatus.OK
    except Exception as e:
        return jsonify(str(e)),HTTPStatus.UNPROCESSABLE_ENTITY
    
@bp.route("/delete_attendence",methods=["DELETE"])
@use_args({"attendence_id":fields.Integer(required=True,validate=validate.Range(min=1,error="attendence_id must be a positive integer"))},location="query")
def delete_department(args:dict):
    try:
        result = attendenceBLC.deleting_the_attendence(args)
        return jsonify(result),HTTPStatus.OK
    except Exception as e:
            return jsonify(str(e)),HTTPStatus.UNPROCESSABLE_ENTITY