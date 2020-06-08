from odoo import models, fields, api, _

class crm_lead(models.Model):
    _inherit = 'crm.lead'
    _description=''

    descripcion_oportunidad=fields.Text(string="Descripcion de la oportunidad")
    usuario=fields.Many2one('res.users','Nombre del usuario actual', default=lambda self: self.env.uid, readonly=True)

    sector=fields.Char(string="Sector de la empresa",related='partner_id.sector')
    product_id=fields.Many2one('product.template',string="Producto")
    marca=fields.Char(related='product_id.marca',readonly=True,string="Marca del producto")
    costo=fields.Float(related='product_id.standard_price', readonly=True, string="Precio del producto")

class product(models.Model):
    _inherit = 'product.template'
    _description=''
    marca=fields.Char(string="Marca del producto")

class partner(models.Model):
    _inherit = 'res.partner'
    _description=''
    sector=fields.Char(string="Sector de la empresa")
