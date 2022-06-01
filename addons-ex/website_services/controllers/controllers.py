# -*- coding: utf-8 -*-
from inspect import getfile
from re import search
from urllib import request
from odoo import http
from markupsafe import Markup

# show only the last n items in the database until I figure out how to deduplicate the records
# should match the number of records in timeline.xml
TIMELINE_ITEM_COUNT = 3
# number of records in employees.xml
EMPLOYEE_COUNT = 3

YTEMBED_COUNT = 2
TECH_COUNT = 3
CATALOG_ITEM_COUNT = 2

def get_iframe(url, props):
    return f"<iframe class=\"ytembed\" src=\"{url}\" {props}></iframe>"

class WebsiteAbout(http.Controller):
    @http.route('/services', auth='public', website=True)
    def index(self, **kw):
        text = http.request.env["website_services.models.text"]
        # # ms_id = http.request.env.ref("website_services.missionstatement")
        # timeline = http.request.env["website_services.models.timeline"].search([])[-TIMELINE_ITEM_COUNT:]
        # employees = http.request.env["website_services.models.employee"].search([])[-EMPLOYEE_COUNT:]
        embeds_model = "website_services.models.ytembed"
        embeds = http.request.env[embeds_model].search([])[-YTEMBED_COUNT:]

        techs_model = "website_services.models.tech"
        techs = http.request.env[techs_model].search([])[-TECH_COUNT:]

        for yt in embeds:
            yt.iframe = get_iframe(yt.url, yt.props)
        
        for t in techs:
            t.img = Markup(t.get_img_html())
        
        return http.request.render('website_services.index', {
            "servicesdesc": http.request.env["website_services.models.text"].search([("name", "=", "servicesdesc")], limit=1)[0],
            "yt": embeds,
            "techs": techs,
            "banner": http.request.env["website_services.models.text"].search([("name", "=", "banner")], limit=1)[0],
            "catalogtitle": http.request.env["website_services.models.title"].search([("name", "=", "catalog")], limit=1)[0],
            "catalogitems": http.request.env["website_services.models.catalog"].search([])[-CATALOG_ITEM_COUNT:],
            # "missionstatement": text.search([("name", "=", "ms")], limit=1)[0],
            # "value": text.search([("name", "=", "val")], limit=1)[0],
            # "timeline_events": timeline,
            # "employees": employees,
        })


#     @http.route('/website_services/website_services/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('website_services.listing', {
#             'root': '/website_services/website_services',
#             'objects': http.request.env['website_services.website_services'].search([]),
#         })

#     @http.route('/website_services/website_services/objects/<model("website_services.website_services"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('website_services.object', {
#             'object': obj
#         })
