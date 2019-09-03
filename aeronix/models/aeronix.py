from odoo import models,fields

class Aeronix(models.Model):
    _name= 'aeronix'
    _description= 'aeronix info'

    name = fields.Many2one("res.partner")

    id_status = fields.Selection([
        ('passport', 'Passport'),
        ('id', 'ID Card'),
        ('driving', 'Driving License')
        ],)

    id_number = fields.Integer(string='Id Number', required= 'True')
