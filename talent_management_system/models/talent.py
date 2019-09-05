from odoo import models,fields,api

class Talent(models.Model):
    _name = "talent"
    _description = "Talent management system"

    id = fields.Many2one("hr.employee")
    name = fields.Many2one("hr.employee")
    d_name = fields.Many2one("hr.department")
    email = fields.Char()
    role_name = fields.Many2one("role")

    @api.onchange('name')
    def _onchange_email(self):
        self.email = self.name.work_email
        self.d_name = self.name.department_id