# -*- coding: utf-8 -*-
{
    'name': "grantmasterycontacts",
    'version': '0.1',
    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
    Grant-Mastery Contacts Customizations""",

    'author': "Payne Empowerment",
    'website': "http://www.payneempowerment.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Customization',
    

    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts', 'hr'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/res_partner_view.xml',

    ],
      'application': True,
}

