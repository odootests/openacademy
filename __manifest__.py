# -*- coding: utf-8 -*-
{
    'name': "openacademy",
    'summary': "Summary",
    'description': "Description",
    'author': "Haha",
    'website': "http://www.yourcompany.com",
    'category': 'Module Development',
    'version': '0.1',
    'depends': ['base', 'report'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/openacademy_course.xml',
        'views/openacademy_session.xml',
        'views/partner.xml',
        'views/openacademy_session_workflow.xml',
        'views/reports.xml'
    ],
    'installable': True,
    'application': True
}