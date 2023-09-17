from marshmallow import Schema,fields

class UserSchema(Schema):
    id = fields.Integer()
    '''用户ID'''
    name =fields.String(required=True)
    '''用户姓名'''
    email = fields.Email(required=True)
    '''电子邮箱'''
    password= fields.String(load_only=True)