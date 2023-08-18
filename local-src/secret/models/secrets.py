# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools


class Goal(models.Model):
    _name = 'secret.secret'
    _description = 'Secrets'

    name = fields.Char(
        string="Nom court",
        compute="_name_short")
    secret = fields.Text(
        string="Secret"
    )
    ipaddress = fields.Char(
        string="Adresse ip"
    )


    @api.depends('secret')
    def _name_short(self):
        for record in self:
            if record.secret:
                record.name = record.secret[:50] + '...'
            else:
                record.name = False