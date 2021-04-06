from flask_restplus import Api

from .admin import api as ns_admin

api = api(
  title='Prueba de back AppLab',
  version='0.1.0',
  description='Preuba de API de AppLab <style>.models {display: none !important}</style>',
  contact="Eduardo Acosta Martinez",
  contact_email="fx2013630461@gmail.com",
  RESTPLUS_MASK_SWAGGER=False
)

api.add_namespace(ns_admin)