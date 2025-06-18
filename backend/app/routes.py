from flask import Blueprint, request, jsonify
from app.models import Contacto
from app.schemas import ContactoSchema

routes = Blueprint("routes", __name__)

contactos = []  
contador_id = 1  

@routes.route("/contactos", methods=["POST"])
def crear_contacto():
    global contador_id
    data = request.get_json()
    schema = ContactoSchema()
    errors = schema.validate(data)
    if errors:
        return jsonify(errors), 400

    nuevo = Contacto(
        id=contador_id,
        nombre=data["nombre"],
        apellido=data["apellido"],
        correo=data["correo"],
        razon=data["razon"],
        mensaje=data["mensaje"]
    )
    contactos.append(nuevo)
    contador_id += 1

    print(f"Contacto recibido: {vars(nuevo)}")
    return schema.dump(nuevo), 201

@routes.route("/contactos", methods=["GET"])
def obtener_contactos():
    schema = ContactoSchema(many=True)
    return schema.dump(contactos), 200

@routes.route("/contactos/<int:id>", methods=["GET"])
def obtener_contacto_por_id(id):
    schema = ContactoSchema()
    contacto = next((c for c in contactos if c.id == id), None)
    if contacto:
        return schema.dump(contacto), 200
    return jsonify({"error": "Contacto no encontrado"}), 404
