from openerp import models, fields, api

class proc(models.Model):
    _name = 'procs.proc'

    name        = fields.Char(string='Nombre', required=True)
    descripcion = fields.Text()
    area        = fields.Many2one('procs.area')
    gerencia    = fields.Many2one('procs.gerencia')
    unidad      = fields.Many2one('procs.unidad')
    depto       = fields.Many2one('procs.depto')
    proceso     = fields.Many2one('procs.proceso')
    fecha       = fields.Char()
    pasos       = fields.Many2many('procs.paso')

    @api.onchange('area')
    def _onchange_area(self):
        if not self.name:
            self.name = self.area.name

#    @api.onchange('gerencia')
#    def _onchange_gerencia(self):
#        if not self.name:
#            self.name = self.gerencia.name
