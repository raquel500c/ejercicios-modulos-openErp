# -*- coding: utf-8 -*-
# importamos las librerias propias de openerp, con la cual vamos a hacer referencia a las clases maestras
from openerp.osv import osv, fields
from openerp import netsvc
from openerp.tools.translate import _
from datetime import datetime

# Definimos la clase asignaturas


class asignaturas_asignaturas(osv.osv):
    # nombre de la tabla que se creara en la base de datos cuando se instala el modulo
    _name = 'asignaturas.asignaturas'
    # lo siguiente son las columnas de la tabla
    _columns = {
        'asignaturas': fields.char('Asignaturas', size=64),
        'profesor': fields.char('Profesor', size=64),
        'alumno': fields.char('Alumno', size=16),
        'curso': fields.char('Curso', size=16),
        'nota': fields.char('Nota'),
        'n_Eval': fields.char('N_Eval'),
        'fecha_eva': fields.date('Fecha_Eva'),
        'anotaciones': fields.char('Anotaciones', size=64),
    }


asignaturas_asignaturas()
