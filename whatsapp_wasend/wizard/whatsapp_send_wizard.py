from odoo import models, fields, api
from jinja2 import Template
import requests


class WhatsAppWizard(models.TransientModel):
    _name = 'whatsapp.wizard'
    _description = 'WhatsApp Wizard'

    model = fields.Char(required=True)
    res_id = fields.Integer(required=True)

    template_id = fields.Many2one('whatsapp.template',domain="[('model_id.model', '=', model)]", required=False)

    message = fields.Text(readonly=False)
    partner_id = fields.Many2one('res.partner', required=True)


    def _get_record(self):
        self.ensure_one()
        return self.env[self.model].browse(self.res_id)


    def _generate_message(self):
        self.ensure_one()

        record = self._get_record()

        template = Template(self.template_id.message)

        return template.render({
            'object': record
        })

    def _get_phone(self, record):
        for rec in self:
            phone = getattr(record, 'phone', False) or getattr(record, 'mobile', False) or rec.patner_id.phone

        if not phone:
            raise Exception("No phone or mobile field found on this record")

        return phone

    @api.onchange('template_id')
    def _onchange_message(self):
        for rec in self:
            if rec.template_id and rec.partner_id:
                rec.message = rec.template_id.generate_message(self.env[self.model].browse(self.res_id)
)

            else:
                rec.message = False

    def action_send(self):
        self.ensure_one()

        webhook_url = "https://autostage.avalon-ai.com/webhook-test/whatsapp-send"

        record = self._get_record()

        if self.template_id:
            message = self._generate_message()
        else:
            message = self.message

        phone = self._get_phone(record)

        payload = {
            "phone": phone,
            "message": message
        }

        try:
            requests.post(webhook_url, json=payload, timeout=10)
        except Exception as e:
            raise Exception(f"WhatsApp sending failed: {str(e)}")

        return True