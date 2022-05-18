# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class website_about(models.Model):
#     _name = 'website_about.website_about'
#     _description = 'website_about.website_about'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class MText(models.Model):
    _name = 'website_about.models.text'
    _description = 'simple text box with title'

    title = fields.Char()
    content = fields.Char(required=True)