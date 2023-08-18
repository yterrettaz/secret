# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Secrets',
    'summary': '',
    'version': '16.0.0',
    'category': '',
    'website': '',
    'author': '',
    'license': '',
    'application': True,
    'installable': True,
    'external_dependencies': {
        'python': [],
        'bin': [],
    },
    'depends': [
        'base',
    ],
    'data': [
        'views/menu.xml',
        'views/secret.xml',
        'templates/home.xml',
        # Security
        'security/ir.model.access.csv', 
    ],
    'demo': [
    ],
    'qweb': [
        
    ]
}
