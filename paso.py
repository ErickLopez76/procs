from openerp import models, fields, api

class paso(models.Model):
    _name = 'procs.paso'

    numero      = fields.Integer(required=True)
    responsable = fields.Char()
    descripcion = fields.Text()
