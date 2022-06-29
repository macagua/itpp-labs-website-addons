# Copyright 2016 Ilyas <https://github.com/ilyasProgrammer>
# Copyright 2016 Ildar Nasyrov <https://www.it-projects.info/team/iledarn>
# Copyright 2016 Dinar Gabbasov <https://www.it-projects.info/team/GabbasovDinar>
# Copyright 2016-2017 Ivan Yelizariev <https://it-projects.info/team/yelizariev>
# Copyright 2017 Kolushov Alexandr <https://it-projects.info/team/KolushovAlexandr>
# Copyright 2021-2022  Leonardo Caballero <https://github.com/macagua>
# License MIT (https://opensource.org/licenses/MIT).

from odoo import _, api, fields, models


class WebsiteConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    nobill_noship = fields.Boolean(string="Pickup and pay at store")
    bill_noship = fields.Boolean(string="Pickup at store but pay now")
    bill_ship = fields.Boolean(string="Pay now and get delivery")
    nobill_ship = fields.Boolean(string="Pay on delivery")
    bill_ship_option = fields.Selection(
        [
            ("nobill_noship", "Pickup and pay at store"),
            ("bill_noship", "Pickup at store but pay now"),
            ("bill_ship", "Pay now and get delivery"),
            ("nobill_ship", "Pay on delivery"),
        ],
        string="Selected by default",
        default="nobill_noship",
    )

    @api.model
    def get_values(self):
        res = super(WebsiteConfigSettings, self).get_values()
        config_parameters = self.env["ir.config_parameter"].sudo()
        res.update(
            nobill_noship=config_parameters.get_param(
                "website_sale_checkout_store.nobill_noship", default=False
            ),
            bill_noship=config_parameters.get_param(
                "website_sale_checkout_store.bill_noship", default=False
            ),
            bill_ship=config_parameters.get_param(
                "website_sale_checkout_store.bill_ship", default=False
            ),
            nobill_ship=config_parameters.get_param(
                "website_sale_checkout_store.nobill_ship", default=False
            ),
            bill_ship_option=config_parameters.get_param(
                "website_sale_checkout_store.bill_ship_option", default="nobill_noship"
            ),
        )
        return res

    def set_values(self):
        super(WebsiteConfigSettings, self).set_values()
        config_parameters = self.env["ir.config_parameter"].sudo()
        for record in self:
            config_parameters.set_param(
                "website_sale_checkout_store.nobill_noship", record.nobill_noship or ""
            )
            config_parameters.set_param(
                "website_sale_checkout_store.bill_noship", record.bill_noship or ""
            )
            config_parameters.set_param(
                "website_sale_checkout_store.bill_ship", record.bill_ship or ""
            )
            config_parameters.set_param(
                "website_sale_checkout_store.nobill_ship", record.nobill_ship or ""
            )
            config_parameters.set_param(
                "website_sale_checkout_store.bill_ship_option",
                record.bill_ship_option or "",
            )
