# -*- coding: utf-8 -*-
{
    'name': "Grant-Mastery",

    'summary': "Customizations for the Grant-Mastery Addon",

    'description': """
Grant-Mastery All Customizations  
    """,

    'author': "Payne Empowerment",
    'website': "http://www.payneempowerment.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'application': True,

    # any module necessary for this one to work correctly
    'depends': ['base', 'grantmasterycontacts', 'grantmasteryproposals'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
    ],
}

