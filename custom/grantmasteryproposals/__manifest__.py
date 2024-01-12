# -*- coding: utf-8 -*-
{
    'name': 'Grant-Mastery CRM',

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
    Grant-Mastery CRM Customizations
    """,

    'author': "Payne Empowerment",
    'website': "http://www.payneempowerment.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'crm',],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',

        'views/crm_lead_form_views.xml',
        'views/crm_lead_tree_opportunity_views.xml',
        'views/menu_crm_root.xml',
    ],
}