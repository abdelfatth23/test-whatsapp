import requests

def send_to_n8n(self):
    url = "http://localhost:5678/webhook/send-whatsapp"

    for partner in self:
        requests.post(url, json={
            "name": partner.name,
            "phone": partner.phone,
            "message": "أهلاً 👋 رسالة من Odoo"
        })

