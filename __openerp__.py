# -*- coding: utf-8 -*-
###############################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2017 Humanytek (<www.humanytek.com>).
#    Manuel Márquez <manuel@humanytek.com>
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
###############################################################################

{
    'name': "product_season",
    'summary': """
        adds a model to define a catalog of seasons with a range of dates.
        """,
    'description': """
        adds a model to define a catalog of seasons with a range of dates.
        Also extends the addon product to add field season in view form of
        products.
    """,
    'author': "Humanytek",
    'website': "http://www.humanytek.com",
    'category': 'Sales',
    'version': '1.0.0',
    'depends': ['product', 'purchase'],
    'data': [
        'views/product_view.xml',
        'views/season_view.xml',
    ],
    'demo': [
    ],
}
