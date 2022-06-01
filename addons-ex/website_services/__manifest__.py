# -*- coding: utf-8 -*-
{
    'name': "WebsiteService",

    'summary': """
    """,

    'description': """
    """,

    'author': "tiuSolution",
    # 'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Website',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website'],

    # 'css': [
    #     'static/src/template_index.css'
    # ],
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'templates/template_index.xml',
        'data/text.xml',
        'data/embed.xml',
        'data/tech.xml',
        'data/services.xml',
    ]
}
