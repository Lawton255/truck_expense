from odoo import models, fields, api

class TruckExpense(models.Model):
    _name = 'all.expense'
    _inherit = ['fleet.vehicle', 'truck.trip']
    _rec_name = 'exp_trip_no'
    _order  =   'exp_trip_no desc'


    @api.depends('exp_amount', 'qty')
    def _compute_total_expense(self):
        for record in self:
                record['exp_total'] = record.exp_amount * record.qty

    @api.model
    def default_get(self, default_fields):
        res = super(TruckExpense, self).default_get(default_fields)
        res.update({
            'date': fields.Date.context_today(self)})
        return res

    exp_trip_no = fields.Many2one('truck.trip' , string="Trip number" , required=True)
    exp_truck  =  fields.Many2one('fleet.vehicle', string='Truck', required=True)
    expense_type = fields.Selection([
                ('trip', 'Trip'), 
                ('workshop', 'Workshop'), 
                ('driver', 'Driver')])
    exp_product  = fields.Many2one('exp.product')
    exp_amount  = fields.Float(string="Price")
    qty         = fields.Float(string="Quantity" , default='1.0')
    exp_total   = fields.Float(string="Total", compute="_compute_total_expense")
    date        = fields.Date(string="Date")
    employee    = fields.Many2one('res.partner', string="Responsible", required=True)


