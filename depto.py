from openerp import models, fields, api

class depto(models.Model):
    _name = 'procs.depto'

    name = fields.Char(string='Nombre', required=True)
    descripcion = fields.Text()
