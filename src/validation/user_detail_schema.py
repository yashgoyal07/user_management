from marshmallow import Schema, fields, ValidationError, \
    validate,validates_schema,post_load
import json


def validate_mobile(n):
    if len(n) > 20:
        raise ValidationError('length of mobile number must be less than 20')
    if not n.isdigit():
        raise ValidationError('mobile number must be numeric')


def validate_date(n):
    date_list = list(map(int, n.split('-')))
    if not 1000 <= date_list[0] <= 9999:
        raise ValidationError('Date must be between range 1000-01-01 to 9999-12-31')
    if not 1 <= date_list[1] <= 12:
        raise ValidationError('Date must be between range 1000-01-01 to 9999-12-31')
    if not 1 <= date_list[2] <= 31:
        raise ValidationError('Date must be between range 1000-01-01 to 9999-12-31')


class AddressSchema(Schema):
    name = fields.Str(validate=validate.Length(max=100))
    country_code = fields.Str(validate=validate.Length(max=20))
    mobile_number = fields.Str(validate=validate_mobile)
    email = fields.Email()
    address_line_1 = fields.Str(required=True, validate=validate.Length(max=200))
    address_line_2 = fields.Str(validate=validate.Length(max=200))
    landmark = fields.Str(validate=validate.Length(max=200))
    city = fields.Str(required=True, validate=validate.Length(max=100))
    district = fields.Str(required=True, validate=validate.Length(max=100))
    state = fields.Str(required=True, validate=validate.Length(max=100))
    country = fields.Str(required=True, validate=validate.Length(max=100))
    pincode = fields.Str(required=True, validate=validate.Length(max=20))


class PaymentInfoSchema(Schema):
    method = fields.Str(validate=validate.Length(max=100))
    vendor = fields.Str(validate=validate.Length(max=100))


class UserDetailSchema(Schema):
    user_id = fields.Str(required=True, validate=validate.Length(max=100))
    name = fields.Str(validate=validate.Length(max=100), missing=None)
    email = fields.Email(required=True)
    sex = fields.Str(validate=validate.OneOf(["male", "female", "other"]), missing=None)
    dob = fields.Str(validate=validate_date, missing=None)
    country_code = fields.Str(validate=validate.Length(max=20), missing=None)
    mobile = fields.Str(validate=validate_mobile, missing=None)
    billing_address = fields.Nested(AddressSchema, missing={})
    delivery_address = fields.Nested(AddressSchema, missing={})
    payment_info = fields.Nested(PaymentInfoSchema, missing={})
    latest_order_id = fields.Str(validate=validate.Length(max=100), missing=None)
    tags = fields.List(fields.Str(), missing=[])

    @post_load
    def dict_to_json(self, data, **kwargs):
        for column in ['tags', 'billing_address', 'delivery_address', 'payment_info', 'latest_order_id']:
            data[column] = json.dumps(data[column])
        return data

    class Meta:
        unknown = 'EXCLUDE'


