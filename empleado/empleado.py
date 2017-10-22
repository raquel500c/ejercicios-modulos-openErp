# #-*- coding: utf-8 -*-
#importamos las librerias propias de openerp, con la cual vamos a hacer referencia a las clases maestras
from openerp.osv import osv,fields
from openerp import netsvc
from openerp.tools.translate import _
from datetime import datetime


class empleado_empleado(osv.osv):
_name = 'empleado.empleado'

_columns = {
    'id_Empleado': fields.integer('Id_Empleado', size = 7, required = True),
	'fecha_ingreso': fields.date('Fecha_Ingreso'),
	'nombre': fields.char('Nombre', size = 30, required = True),
	'apellidos': fields.char('Apellidos', size = 50, required = True),
	'dirección': fields.char('Dirección', size = 50, required = True),
	'dni': fields.char('DNI', size = 9, required = True),
	'telefono': fields.char('tfno', size = 12, required = True),
	'email': fields.char('Email', size = 50, required = True),
	'categoria':  fields.selection([('adm','Administrativos'),('tec','Técnicos de Mantenimiento'),('prog','Programadores')],'Categoría', required = True),
	'salario': fields.float('Salario €',size = 10, help = "Euros", required = True),
	'fecha_valoración': fields.date('Fecha_Valoración'),
	'valoracion':  fields.selection([('mal','Mala'),('reg','Regular'),('bue','Buena')],'Valoración', required = True),
	'observaciones': fields.char('Observaciones', size = 100, required = True),
}

empleado_empleado()
