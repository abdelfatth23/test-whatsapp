from odoo import fields,models,api



class AccountMove(models.Model):
    _inherit = 'account.move'

    phone = fields.Char(related='partner_id.phone')

    def action_open_whatsapp_wizard(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'whatsapp.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_res_id': self.id,
                'default_model': 'account.move',
                'default_partner_id': self.partner_id.id,
            }
        }
