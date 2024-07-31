from marshmallow import (
    Schema,
    ValidationError,
    fields,
    validate,
    validates,
    post_dump,
    validates_schema
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
class performanceSchema(Schema):
    performance_id = fields.Integer(dump_only=True)
    score = fields.Integer(required=True,validate=validate.Range(min=0,error="score must be a positive integer"))
    feedback = fields.String(required=True,validate=validate.Length(min=1,error="feedback cannot be left empty"))
    reviewdate = fields.Date(required=True,format="%Y-%m-%d")
    employee_id = fields.Integer(required=True,validate=validate.Range(min=1,error="employee_id must be a positive integer"))

class update_performance_schema(performanceSchema):
    performance_id = fields.Integer(required=True,validate=validate.Range(min=1,error="id must be a positive integer"))


class EmployeeperformanceSchema(Schema):
    employee_id = fields.Integer(required=False,validate=validate.Range(min=1,error="employee_id must be a positive integer"))
    performance_id = fields.Integer(required=False,validate=validate.Range(min=1,error="performance_id must be a positive integer"))
    page = fields.Integer()
    per_page = fields.Integer()
    @validates_schema
    def validate_only_one_id(self, data, **kwargs):
        if 'employee_id' not in data and 'performance_id' not in data:
            raise ValidationError('Either employee_id or performance_id must be provided.')
        if 'employee_id' in data and 'performance_id' in data:
            raise ValidationError('Only one of employee_id or performance_id must be provided, not both.')

# class employee_details_with_DJ(employeeSchema):
#     jobs = fields.Nested(JobSchema, exclude=("job_id",))
#     department = fields.Nested(DepartmentSchema, exclude=("department_id",))

#     @post_dump
#     def remove_id(self,data,**kwargs):
#         data.pop("job_id",None)
#         data.pop("department_id",None)
#         return data

