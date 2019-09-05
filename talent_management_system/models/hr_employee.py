from odoo import fields,models

class HrEmployee(models.Model):
    _inherit="hr.employee"


    role_name = fields.Selection([
        ('engineer', 'Engineer'),
        ('manager', 'Manager'),
        ('technician', 'Technician')
    ], )