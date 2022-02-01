# -*- coding: utf-8 -*-
# from odoo import http


# class AbsenceRequest(http.Controller):
#     @http.route('/absence_request/absence_request/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/absence_request/absence_request/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('absence_request.listing', {
#             'root': '/absence_request/absence_request',
#             'objects': http.request.env['absence_request.absence_request'].search([]),
#         })

#     @http.route('/absence_request/absence_request/objects/<model("absence_request.absence_request"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('absence_request.object', {
#             'object': obj
#         })
