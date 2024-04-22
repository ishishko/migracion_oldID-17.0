from odoo import api, fields, models

class ResPartner (models.Model):
    _inherit='res.partner'
    
    old_id = fields.Integer(string='old_id')