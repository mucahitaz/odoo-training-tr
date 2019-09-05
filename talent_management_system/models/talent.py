from odoo import models,fields,api

class Talent(models.Model):
    _name = "talent"
    _description = "Talent management system"

    id = fields.Many2one("hr.employee")
    name = fields.Many2one("hr.employee")
    d_name = fields.Many2one("hr.department")
    email = fields.Char()
    role_name = fields.Char()
    date_started = fields.Date()
    levels = fields.Integer(compute='_compute_experience_days')
    experience = fields.Integer(compute='_compute_experience_days')

    @api.onchange('name')
    def _onchange_email(self):
        self.email = self.name.work_email
        self.d_name = self.name.department_id
        self.role_name = self.name.role_name

    @api.depends('date_started')
    def _compute_experience_days(self):
        if self.date_started:
            self.experience = (fields.Date.today() - self.date_started).days

            if self.experience > 60:
                self.levels = 2
            elif self.experience < 0:
                self.experience = 0
            else:
                self.levels = 1


