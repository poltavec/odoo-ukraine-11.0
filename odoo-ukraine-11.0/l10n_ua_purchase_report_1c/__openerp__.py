# -*- coding: utf-8 -*-
{
    'name': 'Приходная накладная для Украины - purchase Order Report Ukrainian ',
    'author': 'Hlv Team Ukraine',
    'website': 'https://hlv-ua.pro',
    'category': 'purchases',
    'depends': ['purchase'],
    'version': '1.0',
    'license': 'Other proprietary',
    'price': 0,
    'currency': 'UAH',
    'description': """
Друкована форма замовлень закупівлі та приходної накладної
==========================================================
Модуль встановлює форму для друку замовлень постачальнику
та приходної накладної
""",
    'auto_install': False,
    'demo': [],
    'data': [
            'views/report_purchaseorder.xml',
            'views/report_purchasequotation.xml',
            'data/purchase_report.xml'
        ],
    'installable': True,
    'application': False,
}
