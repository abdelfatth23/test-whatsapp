import requests
from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    def action_open_whatsapp_wizard(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'whatsapp.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_res_id': self.id,
                'default_model': 'res.partner',
                'default_partner_id': self.id,
            }
        }

