from openerp import models, fields, api

class gerencia(models.Model):
    _name = 'procs.gerencia'

    name = fields.Char(string='Nombre', required=True)
    descripcion = fields.Text()
