from odoo import models, fields

class ExpProduct(models.Model):
    _name = 'exp.product'

    name = fields.Char(string="Product expense")