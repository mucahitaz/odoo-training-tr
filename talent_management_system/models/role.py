from odoo import fields,models

class Role(models.Model):
    _name="role"
    _description = "Roles"

    name = fields.Selection([
        ('engineer', 'Engineer'),
        ('manager', 'Manager'),
        ('technician', 'Technician')
    ], )