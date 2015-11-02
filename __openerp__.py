# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    'name': 'Shuttl Website Module',
    'version': '1.1',
    'category': 'Report',
    'sequence': 19,
    'summary': 'website module',
    'description': """
Shuttl Website MOdule
========================
    """,
    'author': 'J&G Infosystems',
    'website': 'https://www.jginfosystems.com',
    'images': [],
    'depends': ['base','website','shuttl_erp'
                ],
    'data': [
             'data/data.xml',
             'views/template.xml',
    ],
#     'qweb' : [
#         "static/src/xml/*.xml",
#     ],    
    'test': [
    ],
    'demo': [
    ],
    'installable': True,
    'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
