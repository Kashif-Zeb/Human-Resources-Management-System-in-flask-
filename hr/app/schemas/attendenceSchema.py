from marshmallow import (
    Schema,
    ValidationError,
    fields,
    validate,
    validates,
    post_dump
)
from hr.app.schemas.jobSchema import JobSchema
from hr.app.schemas.departmentSchema import DepartmentSchema

def no_space_validation(name):
    def validator(value):
        if value.startswith(" "):
            raise ValidationError(f"{name} cannot start with whitespaces")
        if value.endswith(" "):
            raise ValidationError(f"{name} cannot end with whitespaces")
    return validator

def phone(key):
    def validator(value:str):
        if not value.isdigit():
            raise ValidationError(f"{key} must be a positive integer")
    return validator
def check_not_float(key):
    def validator(value):
        if not isinstance(value,int):
            raise ValidationError(f"{key} must be a integer")
    return validator
class attendenceSchema(Schema):
    attendence_id = fields.Integer(dump_only=True)
    date = fields.Date(required=True,format="%Y-%m-%d")
    check_in_time = fields.DateTime(required=True,format="%Y-%m-%d %H:%M:%S")
    check_out_time = fields.DateTime(required=True,format="%Y-%m-%d %H:%M:%S")
    employee_id = fields.Integer(required=True,validate=validate.Range(min=1,error="department_id must be a positive integer"))

class update_attendence_schema(attendenceSchema):
    attendence_id = fields.Integer(required=True,validate=validate.Range(min=1,error="id must be a positive integer"))

# class employee_details_with_DJ(employeeSchema):
#     jobs = fields.Nested(JobSchema, exclude=("job_id",))
#     department = fields.Nested(DepartmentSchema, exclude=("department_id",))

#     @post_dump
#     def remove_id(self,data,**kwargs):
#         data.pop("job_id",None)
#         data.pop("department_id",None)
#         return data

