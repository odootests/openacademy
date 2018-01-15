from odoo import models, fields, api
from . import *

class Session(models.Model):
	_name='openacademy.session'
	session_name= fields.Char(required=True)
	start_date = fields.Date()
	duration = fields.Float(digits=(6,2), help="Duration in days")
	seats = fields.Integer(string="Number of seats")
	instructor_id = fields.Many2one('res.partner', string='Course Instructor', domain=['|', ('is_instructor', '=', True), ('category_id.name', 'ilike', "Teacher")])
	course_id = fields.Many2one('openacademy.course', ondelete='cascade', string='Course', required=True)
	attendee_ids = fields.Many2many('res.partner', string="Attendees")
	seats_taken = fields.Float(string="Seats Taken", compute='calc_seats_taken')

	@api.depends('seats', 'attendee_ids')
	def calc_seats_taken(self):
		for rec in self:
			if not rec.seats:
				rec.seats_taken = 0.0
			else:
				rec.seats_taken = 100.0 * len(rec.attendee_ids) / rec.seats