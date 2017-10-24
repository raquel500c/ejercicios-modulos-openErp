# #-*- coding: utf-8 -*-
# importamos las librerias propias de openerp, con la cual vamos a hacer referencia a las clases maestras
from openerp.osv import osv, fields
from openerp import netsvc
from openerp.tools.translate import _
from datetime import datetime


class compras_compras(osv.osv):
    _name = 'compras.compras'

    _columns = {
        'n_pedido': fields.integer('Num_pedido', size=6, required=True),
        'fecha_p': fields.date('Fecha_Pedido'),
        'producto': fields.char('Producto', size=30, required=True),
        'categoria':  fields.selection([('mor', 'Material de Oficina Regular'), ('moe', 'Material de Oficina Excepcional')], 'Categoría', required=True),
        'ud': fields.integer('Unidades', size=6, required=True),
        'pvp': fields.float('PVP €', size=10, help="Euros", required=True),
        'total': fields.float('Total €', size=10, help="A manubrio", required=True),
        'observaciones': fields.char('Comentarios', size=100, required=True),
    }


compras_compras()
