from marshmallow import (
    Schema,
    ValidationError,
    fields,
    validate,
    validates,
)
# from hr.app.schemas.BloodDonationSchema import BloodDonationSchema

def no_space_validation(name):
    def validator(value):
        if value.startswith(" "):
            raise ValidationError(f"{name} cannot start with whitespaces")
        if value.endswith(" "):
            raise ValidationError(f"{name} cannot end with whitespaces")
    return validator
class JobSchema(Schema):
    job_id = fields.Integer(dump_only=True)
    name = fields.String(required=True,validate=[validate.Length(min=1,error="job name cannot be left empty"),no_space_validation("name")])
    description = fields.String(validate=no_space_validation("description"))
    salary_range = fields.Dict(
        keys=fields.String(validate=validate.OneOf(["minimum", "maximum"])),
        values=fields.Integer(validate=validate.Range(min=1, error="both maximum and minimum value must be a positive integer")),
        required=True
    )
class JobSchema_for_update(JobSchema):
    job_id = fields.Integer(required=True,validate=validate.Range(min=1,error="job_id must be a positive integer"))


