from odoo import models, fields, api, exceptions
from datetime import timedelta

class Session(models.Model):
	_name='openacademy.session'
	session_name= fields.Char(required=True)
	start_date = fields.Date()
	duration = fields.Float(digits=(6,2), help="Duration in days")
	seats = fields.Integer(string="Number of seats")
	active = fields.Boolean(default=True)
	color = fields.Integer()
	instructor_id = fields.Many2one('res.partner', string='Course Instructor', domain=['|', ('is_instructor', '=', True), ('category_id.name', 'ilike', "Teacher")])
	course_id = fields.Many2one('openacademy.course', ondelete='cascade', string='Course', required=True)
	attendee_ids = fields.Many2many('res.partner', string="Attendees")
	seats_taken = fields.Float(string="Seats Taken", compute='calc_seats_taken')
	end_date = fields.Date(string="End Date", store=True, compute='get_end_date', inverse='set_end_date')

	hours = fields.Float(string="Duration in hours", compute='calc_hours', inverse='set_hours')
	
	attendees_count = fields.Integer(string='Attendees Count', compute='calc_attendees', store=True)

	@api.depends('attendee_ids')
	def calc_attendees(self):
		for rec in self:
			rec.attendees_count = len(rec.attendee_ids)

	@api.depends('start_date', 'duration')
	def get_end_date(self):
		for rec in self:
			if not(rec.start_date and rec.duration):
				rec.end_date = rec.start_date
				continue
			start = fields.Datetime.from_string(rec.start_date)
			duration = timedelta(days=rec.duration, seconds=-1)
			rec.end_date = start + duration

	def set_end_date(self):
		for rec in self:
			if not (rec.start_date and rec.end_date):
				continue
			start_date = fields.Datetime.from_string(rec.start_date)
			end_date = fields.Datetime.from_string(rec.end_date)
			rec.duration = (end_date - start_date).days +1

	@api.depends('seats', 'attendee_ids')
	def calc_seats_taken(self):
		for rec in self:
			if not rec.seats:
				rec.seats_taken = 0.0
			else:
				rec.seats_taken = 100.0 * len(rec.attendee_ids) / rec.seats

	@api.onchange('seats', 'attendee_ids')
	def verify_valid_seats(self):
		if self.seats <0:
			return {
				'warning': { 
					'title': "Incorrect amount for seats",
					'message': "No. of seats can't be negative"
				},
			}
		if self.seats < len(self.attendee_ids):
			return {
				'warning': {
					'title': "Too many Attendees",
					'message': "More Attendees than seats"
				}
			}
			
	@api.constrains('instructor_id', 'attendee_ids')
	def check_instructor_not_in_attendees(self):
		for rec in self:
			if rec.instructor_id and rec.instructor_id in rec.attendee_ids:
				raise exceptions.ValidationError("The Instructor cannot be an attendee")

	@api.depends('duration')
	def calc_hours(self):
		for rec in self:
			rec.hours = rec.duration * 24

	def set_hours(self):
		for rec in self:
			rec.duration = rec.hours / 24