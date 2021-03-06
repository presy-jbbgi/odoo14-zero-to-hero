# -*- coding: utf-8 -*-
{
    'name': "Employees' Request for Absence",

    'summary': """
        Employees can create their request for their possible absence """,

    'description': """
        Employees can create their request for their possible absence
    """,

    'author': "Presy Lord",
    'website': "-",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'HR',
    'version': '14.0',

    # any module necessary for this one to work correctly
    'depends': ['base', ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/absence_request_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
