# -*- coding: utf-8 -*-
from odoo import http


class WebsiteAbout(http.Controller):
    @http.route('/about', auth='public', website=True)
    def index(self, **kw):
        text = http.request.env["website_about.models.text"]
        return http.request.render('website_about.index', {
            "ms_title": "aaaaaaaaa",
        })

#     @http.route('/website_about/website_about/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('website_about.listing', {
#             'root': '/website_about/website_about',
#             'objects': http.request.env['website_about.website_about'].search([]),
#         })

#     @http.route('/website_about/website_about/objects/<model("website_about.website_about"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('website_about.object', {
#             'object': obj
#         })
