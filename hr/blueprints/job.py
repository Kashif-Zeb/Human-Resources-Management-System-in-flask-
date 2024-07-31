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
from hr.app.repositories.jobRepository import jobRepository
from marshmallow import fields, Schema, validate
from hr.app.bl.jobBLC import jobBLC
from http import HTTPStatus
# from flask_jwt_extended import jwt_required
from hr.app.schemas.jobSchema import JobSchema, JobSchema_for_update
bp = Blueprint("job", __name__)

@bp.route("/add_job",methods=["POST"])
@use_args(JobSchema,location="json")
def add_job(args:dict):
    try:
        job = jobBLC.adding_job(args)
        schema = JobSchema()
        result = schema.dump(job)
        return result,HTTPStatus.OK
    except Exception as e:
        return jsonify(str(e)),HTTPStatus.UNPROCESSABLE_ENTITY

@bp.route("/get_job_by_id",methods=["GET"])
@use_args({"job_id":fields.Integer(required=True,validate=validate.Range(min=1,error="job_id must be a positive integer"))},location="query")
def get_job_by_id(args:dict):
    try:
        job = jobBLC.getting_department_by_id(args)
        schema = JobSchema()
        result = schema.dump(job)
        return result,HTTPStatus.OK
    except Exception as e:
        return jsonify(str(e)),HTTPStatus.UNPROCESSABLE_ENTITY
    

@bp.route("/get_all_job",methods=["GET"])
def get_all_job():
    try:
        departments = jobBLC.getting_all_jobs()
        schema  = JobSchema(many=True)
        result = schema.dump(departments)
        return result,HTTPStatus.OK
    except Exception as e:
        return jsonify(str(e)),HTTPStatus.UNPROCESSABLE_ENTITY
    


@bp.route("/update_job",methods=["PUT"])
@use_args(JobSchema_for_update,location="json")
def update_department(args:dict):
    try:
        updated = jobBLC.updating_the_job(args)
        schema = JobSchema_for_update()
        result = schema.dump(updated)
        return result,HTTPStatus.OK
    except Exception as e:
        return jsonify(str(e)),HTTPStatus.UNPROCESSABLE_ENTITY
    
@bp.route("/delete_job",methods=["DELETE"])
@use_args({"job_id":fields.Integer(required=True,validate=validate.Range(min=1,error="job_id must be a positive integer"))},location="query")
def delete_department(args:dict):
    try:
        result = jobBLC.deleting_the_job(args)
        return jsonify(result),HTTPStatus.OK
    except Exception as e:
            return jsonify(str(e)),HTTPStatus.UNPROCESSABLE_ENTITY