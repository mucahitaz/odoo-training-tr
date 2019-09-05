from odoo import fields,models

class Role(models.Model):
    _name="role"
    _description = "Roles"

    name = fields.Text(string="Role Name")
    description = fields.Text(string="Role Description")