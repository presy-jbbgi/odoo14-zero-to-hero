# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class AbsenceRequest(models.Model):
    _name = 'absence.request'
    _description = 'The employees request for absence'

    name = fields.Char(string="Name", default="Absence Request", required=True)
    user_id = fields.Many2one('res.users', string='User')
    date_from = fields.Date(string='From',default=0 )
    date_to = fields.Date(string='To', default=0)
    days_absent = fields.Float("Absent days",default=0, compute='_get_days')
    absence_reason = fields.Text(string='Reason')
    proof = fields.Binary('Proof')

    state = fields.Selection([('draft', 'Draft'), ('confirmed', 'Confirmed'), ('rejected', 'Rejected')], 'State',
                             default='draft',
                             readonly=True)

    @api.constrains('date_from', 'date_to')
    def check_date(self):
        if self.date_from > self.date_to:
            raise ValidationError('[Date From] should be less than [Date To]')

    @api.depends('date_from', 'date_to')
    def _get_days(self):

        for req in self:
            req.days_absent = (req.date_to - req.date_from).days

    def to_confirm(self):
        # self.state = 'confirmed'
        self.write({'state': 'confirmed'})

    def to_reject(self):
        # self.state = 'confirmed'
        self.write({'state': 'rejected'})

    def to_draft(self):
        # self.state = 'confirmed'
        self.write({'state': 'draft'})
