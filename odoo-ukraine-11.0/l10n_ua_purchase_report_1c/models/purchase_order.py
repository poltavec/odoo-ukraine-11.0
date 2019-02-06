# -*- coding: utf-8 -*-
from odoo import models, fields, _
from .tools.number_to_text import decimal2text


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    def format_sum_to_text(self, number):
        return decimal2text(number)
