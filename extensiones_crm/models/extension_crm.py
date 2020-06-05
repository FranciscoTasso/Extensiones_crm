from odoo import models, fields, api, _

class crm_lead(models.Model):
    _inherit = 'crm.lead'
    _description=''

    descripcion_oportunidad=fields.Text(string="Descripcion de la oportunidad")
    usuario=fields.Many2one('res.users','Nombre del usuario actual', default=lambda self: self.env.uid, readonly=True)
