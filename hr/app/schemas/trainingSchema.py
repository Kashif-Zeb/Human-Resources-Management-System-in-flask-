from marshmallow import (
    Schema,
    ValidationError,
    fields,
    validate,
    validates,
    post_dump,
    validates_schema
)
from hr.app.schemas.employeeSchema import employeeSchema
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
class trainingSchema(Schema):
    training_id = fields.Integer(dump_only=True)
    training_name = fields.String(required=True,validate=validate.Length(min=1,error="training_name must be a positive integer"))
    status = fields.String(required=True,validate=validate.OneOf(["passed","failed","pending"]))
    date = fields.Date(required=True,format="%Y-%m-%d")
    description = fields.String(required=True,validate=validate.Length(min=1,error="description cannot be left empty"))
    employee_id = fields.Integer(required=True,validate=validate.Range(min=1,error="employee_id must be a positive integer"))

class update_training_schema(trainingSchema):
    training_id = fields.Integer(required=True,validate=validate.Range(min=1,error="id must be a positive integer"))
    class Meta:
        exclude = ("employee_id",)
class getting_training_with_employee(employeeSchema):
    trainings = fields.Nested(trainingSchema,many=True,exclude=("employee_id",))


class EmployeetrainingSchema(Schema):
    employee_id = fields.Integer(required=False,validate=validate.Range(min=1,error="employee_id must be a positive integer"))
    training_id = fields.Integer(required=False,validate=validate.Range(min=1,error="training_id must be a positive integer"))

    @validates_schema
    def validate_only_one_id(self, data, **kwargs):
        if 'employee_id' not in data and 'training_id' not in data:
            raise ValidationError('Either employee_id or training_id must be provided.')
        if 'employee_id' in data and 'training_id' in data:
            raise ValidationError('Only one of employee_id or training_id must be provided, not both.')

# class employee_details_with_DJ(employeeSchema):
#     jobs = fields.Nested(JobSchema, exclude=("job_id",))
#     department = fields.Nested(DepartmentSchema, exclude=("department_id",))

#     @post_dump
#     def remove_id(self,data,**kwargs):
#         data.pop("job_id",None)
#         data.pop("department_id",None)
#         return data

