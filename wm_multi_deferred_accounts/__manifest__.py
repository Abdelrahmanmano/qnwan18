# -*- coding: utf-8 -*-
# Part of Waleed Mohsen. See LICENSE file for full copyright and licensing details.

{
    'name': 'Multi Deferred Expense/Revenue Accounts',
    'version': '1.0.1',
    'category': 'Accounting',
    'summary': """Multi Deferred Expense/Revenue accounts
    Deferred Revenue
    Deferred Expense
    multi Deferred accounts
    multi Deferred Expense/Revenue
    multi Deferred accounts Odoo 18
    multi Deferred Expense accounts
    multi Deferred Revenue accounts
    multi Deferred Revenue
    multi Deferred Expense
    """,
    'description': """
    This app allow you to use specific Deferred Expense/Revenue accounts.
    """,
    'license': 'OPL-1',
    'author': 'Waleed Mohsen',
    'support': 'mohsen.waleed@gmail.com',
    'currency': 'USD',
    'price': 38.00,
    'depends': ['account_accountant','account_reports'],
    'data': [
        'views/account_move_views.xml',
        'views/product_views.xml',
    ],
    'images': ['static/description/main_screenshot.png'],
    
    'installable': True,
    'auto_install': False,
}
