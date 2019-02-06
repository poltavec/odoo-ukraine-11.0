# -*- coding: utf-8 -*-
{
    'name': 'Складские документы для Украины - Stock Picking Report Ukrainian',
    'author': 'Hlv Team Ukraine',
    'website': 'https://hlv-ua.pro',
    'category': 'Stock',
    'depends': ['stock'],
    'version': '1.0',
    'license': 'Other proprietary',
    'price': 0,
    'currency': 'UAH',
    'description': """
Друкована форма накладної на переміщення
=======================================
Модуль встановлює шаблони для друку складських документів
для України. 
Аналог документа в 1С Перемещение. 
""",
    'auto_install': False,
    'demo': [],
    'data': [
            'views/report_stockpicking.xml',
            'data/stock_report.xml'
        ],
    'installable': True,
    'application': False,
}
