from marshmallow import Schema, fields, ValidationError, pre_load


# Custom validator
def must_not_be_blank(data):
    if not data:
        raise ValidationError('Data not provided.')


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    email = fields.Str(required=True, validate=must_not_be_blank)
    password = fields.Str(required=True, validate=must_not_be_blank)
    registered_on = fields.DateTime(dump_only=True)
    admin = fields.Str(dump_only=True)
