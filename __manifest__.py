# -*- coding: utf-8 -*-
{
    'name': "OpenAcademy",
    'summary': "Summary",
    'description': "Description",
    'author': "Haha",
    'website': "http://www.the_name_of_your_website.com",
    'category': 'Module Development',
    'version': '0.1',
    'depends': ['base', 'report', 'board'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/openacademy_course.xml',
        'views/openacademy_session.xml',
        'views/partner.xml',
        'views/openacademy_session_workflow.xml',
        'views/reports.xml',
        'views/session_board.xml'
    ],
    'installable': True,
    'application': True
}