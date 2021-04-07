from flask_restplus import Namespace, Resource, fields
from flask import current_app
from config.database import db
from bson import json_util, objectid
import datetime
import json

api = Namespace('admin', description='Operaciones sobre un administrador')

admin = api.model('admin', {
  '_id': fields.String(required=False, readonly=True),
  'image': fields.String(required=False),
  'name': fields.String(required=True),
  'surname': fields.String(required=True),
  'email': fields.String(required=True),
  'area': fields.String(required=True),
  'estatus': fields.String(required=True),

})


@api.route('')
class Admin(Resource):
  @api.marshal_list_with(admin)
  def get(self):
    '''Listar todos los usuarios'''
    admins = db.db.admins.find()
    response = list(admins)
    return response
  
  @api.response(200, 'Administrador creado correctamente')
  @api.response(400, 'Faltan algunos argumentos')
  @api.response(409, 'El email ya se encuentra registrado')
  @api.response(500, 'Error en el servidor')
  @api.expect( admin )
  def post(self):
    '''Crear un nuevo admin'''
    image = api.payload['image']
    email = api.payload['email']
    name = api.payload['name']
    surname = api.payload['surname']
    area = api.payload['area']
    estatus = api.payload['estatus']

    existing_admin = db.db.admins.find_one({'email' : email})

    if existing_admin:
      api.abort(409, status = "El email del administrador ya se encuentra registrado")
    
    if name:
      idUser = db.db.admins.insert({
          'image': image,
          'name':name,
          'surname': surname,
          'email': email,
          'area': area,
          'estatus': estatus
          })
      if idUser:
        return json.loads(json_util.dumps(idUser))
    else:
      api.abort(500, status = "Ocurrio un error en el proceso")

