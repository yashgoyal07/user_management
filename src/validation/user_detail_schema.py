from marshmallow import Schema, fields, ValidationError, \
    validate, post_load
import json
from datetime import datetime


def validate_mobile(n):
    if len(n) > 20:
        raise ValidationError('length of mobile number must be less than 20')
    if not n.isdigit():
        raise ValidationError('mobile number must be numeric')


def validate_date(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
    except Exception:
        raise ValidationError('date must be valid')


class AddressSchema(Schema):
    name = fields.Str(validate=validate.Length(min=1))
    country_code = fields.Str(validate=validate.Length(min=1))
    mobile_number = fields.Str(validate=validate_mobile)
    email = fields.Email()
    address_line_1 = fields.Str(required=True, validate=validate.Length(min=1))
    address_line_2 = fields.Str(validate=validate.Length(min=1))
    landmark = fields.Str(validate=validate.Length(min=1))
    city = fields.Str(required=True, validate=validate.Length(min=1))
    district = fields.Str(required=True, validate=validate.Length(min=1))
    state = fields.Str(required=True, validate=validate.Length(min=1))
    country = fields.Str(required=True, validate=validate.Length(min=1))
    pincode = fields.Str(required=True, validate=validate.Length(min=1))


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


class UserGetDataSchema(Schema):
    user_id = fields.Str(required=True, validate=validate.Length(max=100))
    columns = fields.List(fields.Str(), missing=[])

    class Meta:
        unknown = 'EXCLUDE'
