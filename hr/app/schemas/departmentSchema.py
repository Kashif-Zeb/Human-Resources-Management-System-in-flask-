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
class DepartmentSchema(Schema):
    department_id = fields.Integer(dump_only=True)
    name = fields.String(required=True,validate=[validate.Length(min=1,error="department name cannot be left empty"),no_space_validation("name")])


class DepartmentSchema_for_update(DepartmentSchema):
    department_id = fields.Integer(required=True)

# class BloodBankSchema(Schema):
#     BloodBankID = fields.Integer(dump_only=True)
#     BloodBankName = fields.String(
#         validate=validate.Length(min=2, max=50),
#         required=True,
#     )
#     Location = fields.String(
#         validate=validate.Length(min=2, max=50),
#         required=True,
#     )
#     Email = fields.Email(required=True)
#     ContactNumber = fields.String(validate=validate.Length(11))

#     @validates("ContactNumber")
#     def validate_phone_number(self, value):
#         if not value.isdigit() or len(value) != 11:
#             raise ValidationError(
#                 "Phone number must contain 10 digits and no other characters."
#             )


# class BB_BD(BloodBankSchema):
#     blooddonations = fields.Nested(
#         BloodDonationSchema, many=True, include=("BloodType")
#     )


# class update_bloodbank(BloodBankSchema):
#     BloodBankID = fields.Integer(required=True)


# class nested_to_Available_blood(Schema):
#     Type = fields.String()
#     TotalAvailable = fields.Integer()


# class Available_blood(BloodBankSchema):
#     BloodType = fields.Nested(nested_to_Available_blood, many=True)
