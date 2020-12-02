# -*- coding: utf-8 -*-
from odoo import http

# class TruckExpense(http.Controller):
#     @http.route('/truck_expense/truck_expense/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/truck_expense/truck_expense/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('truck_expense.listing', {
#             'root': '/truck_expense/truck_expense',
#             'objects': http.request.env['truck_expense.truck_expense'].search([]),
#         })

#     @http.route('/truck_expense/truck_expense/objects/<model("truck_expense.truck_expense"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('truck_expense.object', {
#             'object': obj
#         })