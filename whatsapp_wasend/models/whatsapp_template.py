from odoo import models, fields
from jinja2 import Template




class WhatsAppTemplate(models.Model):
    _name = 'whatsapp.template'
    _description = 'WhatsApp Template'

    name = fields.Char(string="Template Name", required=True)
    model_id = fields.Many2one('ir.model', string="Applies To")
    message = fields.Text(string="Message", required=True)
    active = fields.Boolean(default=True)


    def generate_message(self, record):
        self.ensure_one()
        template = Template(self.message)
        return template.render({
            'object': record
        })