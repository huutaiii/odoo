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

    name = fields.Char()
    title = fields.Text()
    content = fields.Text()

class MTimeline(models.Model):
    _name = 'website_about.models.timeline'
    _description = 'timeline events'

    date = fields.Char()
    content = fields.Text()

class MEmployee(models.Model):
    _name = 'website_about.models.employee'
    _description = ''

    name = fields.Char()
    position = fields.Char()
    description = fields.Text()
    img_url = fields.Char()
    img_tag = fields.Char(compute="get_img_tag")

    @api.depends("img_url")
    def get_img_tag(self):
        for record in self:
            record.img_tag = f'<img src="{record.img_url}" class="img-fluid rounded-circle mx-auto anim-gs" loading="lazy"/>'