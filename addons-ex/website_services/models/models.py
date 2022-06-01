# -*- coding: utf-8 -*-

from inspect import getfile
from odoo import models, fields, api


# class website_services(models.Model):
#     _name = 'website_services.website_services'
#     _description = 'website_services.website_services'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class MTitle(models.Model):
    _name = 'website_services.models.title'
    _description = ''

    name = fields.Char()
    title = fields.Text()

class MText(MTitle):
    _name = 'website_services.models.text'
    _description = 'simple text box with title'

    # name = fields.Char()
    # title = fields.Text()
    content = fields.Text()

def get_iframe(url, props):
    return f"<iframe class=\"ytembed\" src=\"{url}\" {props}></iframe>"

class MYTEmbed(models.Model):
    _name = 'website_services.models.ytembed'
    _description = 'embeded youtube player'

    name = fields.Char()
    url = fields.Char()
    props = fields.Char()
    iframe = fields.Char(readonly=True, compute="compute_iframes")
    
    @api.depends("url", "props")
    def compute_iframes(self):
        for rec in self:
            rec.iframe = get_iframe(self.url, self.props)


class MTech(models.Model):
    _name = 'website_services.models.tech'
    _description = ''

    name = fields.Char()
    img_url = fields.Char()
    img = fields.Char()
    display_name = fields.Char()
    description = fields.Char()

    # @api.depends("img_url")
    # def compute_img_html(self):
    #     for rec in self:
    #         rec.img = self.get_img_html()

    def get_img_html(self):
        return f'<img class="tech-img" src="{self.img_url}"></img>'


class MCatalogItem(MText):
    _name = 'website_services.models.catalog'
    _description = ''
