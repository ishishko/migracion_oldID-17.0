from odoo import api, fields, models

class ResPartner_old_id (models.Model):
    _inherit='res.partner'
    
    old_id = fields.Integer(string='old_id', default= False )
