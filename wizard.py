from odoo import models, fields, api

class Wizard(models.TransientModel):
	_name='openacademy.wizard'
	attendee_ids = fields.Many2many('res.partner', string='Attendees')

	def default_session(self):
		return self.env['openacademy.session'].browse(self._context.get('active_id'))

	session_id = fields.Many2one('openacademy.session', string="Session", required=True, default=default_session)

	@api.multi
	def subscribe(self):
		self.session_id.attendee_ids |= self.attendee_ids
		return {}

	def _default_sessions(self):
		return self.env['openacademy.session'].browse(self._context.get('active_ids'))

	session_ids = fields.Many2many('openacademy.session',
		string="Sessions", required=True, default=_default_sessions)
