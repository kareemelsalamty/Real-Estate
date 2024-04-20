# -*- coding: utf-8 -*-
{
    'name': "app_one",
    'description': "" ,
    'author': "Kareem Elsalamty",
    'website': "",
    'category': '',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/base_menu.xml',
        'views/property_view.xml',
        'views/owner_view.xml',
        'views/tag_view.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml', ],
    'application' :True ,
    'auto_install': False,
}
