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
		
	@api.multi
	def copy(self, default=None):
		default = dict(default or {})
		copy_count = self.search_count([('course_name', '=ilike', u"Copy of {}".format(self.course_name))])
		if not copy_count:
			new_course_name = u"Copy of {}".format(self.course_name)
		else: 
			new_course_name = u"Copy of {} {}".format(self.course_name, copy_count)

		default['course_name'] = new_course_name
		return super(Course, self).copy(default)


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