from marshmallow import Schema, fields

class ContactoSchema(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True)
    apellido = fields.Str(required=True)
    correo = fields.Email(required=True)
    razon = fields.Str(required=True)
    mensaje = fields.Str(required=True)
