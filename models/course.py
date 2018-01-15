# -9*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class Course(models.Model):
	_name='openacademy.course'
	course_name = fields.Char(string="Title", required=True)
	description = fields.Text()
	responsible_id = fields.Many2one('res.users', ondelete='set null', string="Course Taker", index=True)
	session_ids = fields.One2many('openacademy.session', 'course_id', string='Sessions')
	
	def __str__(self):
		return self.course_name

	_sql_constraints = [
    	(
    		'name_description_check', 
    		'CHECK(course_name != description)',
    		'The Course Title and description must be different'
    	),
    	(
    		'check_name_unique', 
    		'UNIQUE(course_name)' , 
    		"The Course title must be unique"
    	),
    ]
# class openacademy(models.Model):
#     _name = 'openacademy.openacademy'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100