# -*- coding: utf-8 -*-

import code
from odoo import models, fields, api, _, tools
from odoo.exceptions import UserError

class ZoomConfig(models.Model):
    _name = 'zoom.config'

    name = fields.Char()
    proveedor = fields.Char()
    n_integracion = fields.Char()
    envio = fields.Char()
    facturacion = fields.Char()
    margen = fields.Char()
    gratis = fields.Char()

    usuario = fields.Char()
    passw = fields.Char()
    token = fields.Char()
    tipo_servicio = fields.Char()
    peso = fields.Char()
    tamano = fields.Char()
    
    
    
class getTipoTarifa(models.Model):
    _name = 'zoom.gettipotarifa'
    
    codigo = fields.Char()
    name = fields.Char()
    a_m = fields.Many2one('sale.order.zoom')
    
class getModalidadTarifa(models.Model):
    _name = 'zoom.getmodalidadtarifa'
    
    codigo = fields.Char()
    name = fields.Char()
    a_m = fields.Many2one('sale.order.zoom')
    
class getCiudadesTarifa(models.Model):
    _name = 'zoom.getciudadestarifa'
    
    code = fields.Char()
    name = fields.Char()
    nombre_estado = fields.Char()
    a_m = fields.Many2one('sale.order.zoom')
    
#class getPaises(models.Model):
 #   _name = 'zoom.config.getPaises'
    
class getTipoEnvio(models.Model):
    _name = 'zoom.gettipoenvio'
    
    codigo = fields.Char()
    name = fields.Char()
    a_m = fields.Many2one('sale.order.zoom')