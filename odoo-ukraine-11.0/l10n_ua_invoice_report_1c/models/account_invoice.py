# -*- coding: utf-8 -*-

from odoo import models, api
from .tools.number_to_text import decimal2text


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    def format_sum_to_text(self, number):
        return decimal2text(number)
