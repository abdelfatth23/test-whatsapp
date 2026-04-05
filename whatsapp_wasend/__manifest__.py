{
    "name": "Whatsapp Wasend",
    "version": "19.0.1.0.1",
    "author": "Abdelfattah ",
    "license": "AGPL-3",
    "category": "Purchase Management",
    "depends": ["contacts","account"],
    "data": [
        'security/ir.model.access.csv',
        'views/whatsapp_template_view.xml',
        'wizard/whatsapp_wizard_view.xml',

        'views/res_partner_view.xml',
        'views/account_move_view.xml',
    ],
    "installable": True,
    "auto_install": False,
}
