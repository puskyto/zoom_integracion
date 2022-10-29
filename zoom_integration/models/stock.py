# -*- coding: utf-8 -*-

from odoo import models, fields, api, _, tools
from odoo.exceptions import UserError

class Zoompicking(models.Model):
    _inherit = 'stock.picking'
    
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
    status = fields.Char()
    peso = fields.Char()
    n_seguimiento = fields.Char()
    trasportista = fields.Char()
    
    def generar_guia(self):
        return {
            'name': """Generar Guia""",
            'res_model': 'stock.picking.zoom',
            'view_mode': 'form',
            'target': 'new',
            'view_id': self.env.ref('zoom_integration.sale_generar_guia_envio_view_form').id,
            'views': [
                (self.env.ref('zoom_integration.sale_generar_guia_envio_view_form').id, 'form'),
            ],
            'type': 'ir.actions.act_window',
            'context': { }
        }
    
    def cancelar_guia():
        return False