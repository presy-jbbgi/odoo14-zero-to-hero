# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AbsenceRequest(models.Model):
    _name = 'absence.request'
    _description = 'The employees request for absence'

    name = fields.Char(string="Name", required=True)
    user_id = fields.Many2one('res.users', string='user')
    date_from = fields.Date(string='From')
    date_to = fields.Date(string='To')
    absence_reason = fields.Text(string='Reason')
    state = fields.Selection([('draft', 'Draft'), ('confirmed', 'Confirmed'), ('rejected', 'Rejected')], 'State',
                             readonly=True)

    def to_confirm(self):
        # self.state = 'confirmed'
        self.write({'state': 'confirmed'})

    def to_reject(self):
        # self.state = 'confirmed'
        self.write({'state': 'rejected'})
