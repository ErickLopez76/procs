from openerp import models, fields, api

class proceso(models.Model):
    _name = 'procs.proceso'

    name = fields.Char(string='Nombre', required=True)
    descripcion = fields.Text()
