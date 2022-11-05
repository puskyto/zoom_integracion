# -*- coding: utf-8 -*-

import code
from odoo import models, fields, api, _, tools
from odoo.exceptions import UserError

#class ZoomConfig(models.Model):
 #   _inherit = 'delivery.carrier'

  #  clave = fields.Char()
   # codigo_cliente = fields.Char()
    
   # def actualizar_estados():
        
    #    return access_zoom_config,zoom.config,model_zoom_config,sales_team.group_sale_salesman,1,1,1,0
    
class getTipoTarifa(models.Model):
    _name = 'zoom.gettipotarifa'
    
    name = fields.Char()
    code = fields.Char()
    
class getModalidadTarifa(models.Model):
    _name = 'zoom.getmodalidadtarifa'
    
    name = fields.Char()
    code = fields.Char()
    
class getCiudadesTarifa(models.Model):
    _name = 'zoom.getciudadestarifa'
    
    name = fields.Char()
    code = fields.Char()
    nombre_estado = fields.Char()
    
class getOficina(models.Model):
    _name = 'zoom.oficinas'
    
    name = fields.Char()
    code = fields.Char()
    code_estado = fields.Char()
    
    
class getTipoEnvio(models.Model):
    _name = 'zoom.gettipoenvio'
    
    name = fields.Char()
    code = fields.Char()
    a_m = fields.Many2one('sale.order.zoom')