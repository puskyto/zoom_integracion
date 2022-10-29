# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.osv import expression


class ZoomStockPicking(models.TransientModel):
    _name = 'stock.picking.zoom'

    metodo = fields.Char()
    
    ciudad = fields.Char()
    oficina = fields.Char()
    localidad = fields.Char()
    sele_rif_ci_pa = fields.Char()
    rif_ci_pa = fields.Char()
    sele_celular = fields.Char()
    celular = fields.Char()
    telefono = fields.Char()
    costo = fields.Float()

    def generar_guia():
        return 1