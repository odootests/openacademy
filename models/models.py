# -9*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):
	_name='openacademy.course'
	course_name = fields.Char(string="Title", required=True)
	description = fields.Text()
	responsible_id = fields.Many2one('res.users', ondelete='set null', string="Course Taker", index=True)
	session_ids = fields.One2many('openacademy.sessoin', 'course_id', string='Sessions')

class Session(models.Model):
	_name='openacademy.session'
	session_name= fields.Char(required=True)
	start_date = fields.Date()
	duration = fields.Float(digits=(6,2), help="Duration in days")
	seats = fields.Integer(string="Number of seats")
	instructor_id = fields.Many2one('res.partner', string='Course Instructor')
	course_id=fields.Many2one('openacademy.course', ondelete='cascade', string='Course', required=True)

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