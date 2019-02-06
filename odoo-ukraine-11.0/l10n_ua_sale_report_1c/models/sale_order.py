# -*- coding: utf-8 -*-
from odoo import models, fields, _
from .tools.number_to_text import decimal2text


class SaleOrder(models.Model):
    _inherit = "sale.order"

    location_signed_in = fields.Char(string=_(u'Місце складання'))

    def format_sum_to_text(self, number):
        return decimal2text(number)
