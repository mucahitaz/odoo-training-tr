from odoo import models,fields,api

class Talent(models.Model):
    _name = "talent"
    _description = "Talent management system"

    id = fields.Many2one("hr.employee")
    name = fields.Many2one("hr.employee")
    d_name = fields.Many2one("hr.department")
    email = fields.Many2one("hr.employee")