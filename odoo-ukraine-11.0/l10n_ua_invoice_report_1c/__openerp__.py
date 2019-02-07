# -*- coding: utf-8 -*-
{
    'name': 'Счет-фактура для Украины - Invoice Ukrainian',
    'author': 'Hlv Team Ukraine',
    'website': 'https://hlv-ua.pro',
    'category': 'Sales',
    'depends': ['sale'],
    'version': '1.0',
    'license': 'Other proprietary',
    'price': 0,
    'currency': 'UAH',
    'description': """
Друкована форма рахунку-фактури для України
==========================================================
Модуль встановлює форму для друку рахунку-фактури.
""",
    'auto_install': False,
    'demo': [],
    'data': [
            'views/report_invoice.xml',
	    'views/report_invoice2.xml',
	    'views/report_invoice3.xml',
	    'views/report_invoice4.xml',
            'data/invoice_report_action.xml'
        ],
    'installable': True,
    'application': False,
}
