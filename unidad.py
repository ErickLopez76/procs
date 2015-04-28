from openerp import models, fields, api

class unidad(models.Model):
    _name = 'procs.unidad'

    name = fields.Char(string='Nombre', required=True)
    descripcion = fields.Text()
