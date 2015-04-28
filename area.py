from openerp import models, fields, api

class area(models.Model):
    _name = 'procs.area'

    name = fields.Char(string='Nombre', required=True)
    descripcion = fields.Text()
    procs       = fields.One2many('procs.proc', 'area')
