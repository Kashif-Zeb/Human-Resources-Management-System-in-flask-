from flask import request, jsonify
from webargs.flaskparser import use_args
from hr.app.schemas.documentSchema import documentSchema, update_document_schema
from functools import wraps
from flask import Blueprint
from marshmallow import fields,validate

from hr.app.db import db
from hr.app.repositories.documentRepository import documentRepository
# from marshmallow import fields, Schema, validate
from hr.app.bl.documentBLC import documentBLC
from http import HTTPStatus
# from flask_jwt_extended import jwt_required

bp = Blueprint("document", __name__)


@bp.route("/add_document",methods=["POST"])
@use_args(documentSchema,location="json")
def add_document(args:dict):
    try:
        document = documentBLC.adding_document(args)
        schema = documentSchema()
        res = schema.dump(document)
        return res,HTTPStatus.OK
    except Exception as e:
        return jsonify({"message":str(e)}),HTTPStatus.UNPROCESSABLE_ENTITY


@bp.route("/get_document_by_id",methods=["GET"])
@use_args({"document_id":fields.Integer(required=True,validate=validate.Range(min=1,error="document_id must be a positive integer"))},location="query")
def get_document_by_id(args):
    try:
        employee = documentBLC.getting_document(args)
        schema = documentSchema()
        res = schema.dump(employee)
        return res,HTTPStatus.OK
    except Exception as e:
        return jsonify({"message":str(e)}),HTTPStatus.UNPROCESSABLE_ENTITY


@bp.route("/get_all_employee_documents",methods=["GET"])
@use_args({"employee_id":fields.Integer(required=True,validate=validate.Range(min=1,error="employee_id must be a positive integer")),
    "page":fields.Integer(required=True,validate=validate.Range(min=1,error="page must be a positive integer")),
           "per_page":fields.Integer(required=True,validate=validate.Range(min=1,error="per_page must be a positive integer"))},location="query")
def get_all_employee_documents(args:dict):
    try:
        employess = documentBLC.getting_all_employee_documents(args)
        get_emp = employess["items"]
        schema = documentSchema(many=True)
        res = schema.dump(get_emp)
        response = {
            'documents': res,
            'page': employess['page'],
            'per_page': employess['per_page'],
            'total_pages': employess['total_pages'],
            'total': employess['total'],
        }
        return response,HTTPStatus.OK
    except Exception as e:
        return jsonify({"error":str(e)}),HTTPStatus.UNPROCESSABLE_ENTITY


@bp.route("/update_document",methods=["PUT"])
@use_args(update_document_schema,location="json")
def updateing_employee(args:dict):
    try:
        updating_employee =documentBLC.updating_document(args)
        schema = update_document_schema()
        res = schema.dump(updating_employee)
        return res,HTTPStatus.OK
    except Exception as e:
        return jsonify({"error":str(e)}),HTTPStatus.UNPROCESSABLE_ENTITY

@bp.route("/delete_document",methods=["DELETE"])
@use_args({"document_id":fields.Integer(required=True,validate=validate.Range(min=1,error="page must be a positive integer"))},location="query")
def delete_employee(args:dict):
    try:
        document_deleted = documentBLC.deleting_document(args)
        return jsonify({"message":document_deleted}),HTTPStatus.OK
    except Exception as e:
        return jsonify({"error":str(e)}),HTTPStatus.UNPROCESSABLE_ENTITY