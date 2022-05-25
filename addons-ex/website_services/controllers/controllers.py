# -*- coding: utf-8 -*-
from odoo import http

# show only the last n items in the database until I figure out how to deduplicate the records
# should match the number of records in timeline.xml
TIMELINE_ITEM_COUNT = 3
# number of records in employees.xml
EMPLOYEE_COUNT = 3

class WebsiteAbout(http.Controller):
    @http.route('/services', auth='public', website=True)
    def index(self, **kw):
        # text = http.request.env["website_about.models.text"]
        # # ms_id = http.request.env.ref("website_about.missionstatement")
        # timeline = http.request.env["website_about.models.timeline"].search([])[-TIMELINE_ITEM_COUNT:]
        # employees = http.request.env["website_about.models.employee"].search([])[-EMPLOYEE_COUNT:]
        
        return http.request.render('website_services.index', {
            # "missionstatement": text.search([("name", "=", "ms")], limit=1)[0],
            # "value": text.search([("name", "=", "val")], limit=1)[0],
            # "timeline_events": timeline,
            # "employees": employees,
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
