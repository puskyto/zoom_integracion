# -*- coding: utf-8 -*-

from odoo import models, fields, api, _, tools
from odoo.exceptions import UserError

class ZoomSale(models.Model):
    _inherit = 'sale.order'

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

    def agregar_envio(self):
        return {
            'name': """Agregar Metodo de Envio""",
            'res_model': 'sale.order.zoom',
            'view_mode': 'form',
            'target': 'new',
            'view_id': self.env.ref('zoom_integration.sale_agregar_metodo_envio_view_form').id,
            'views': [
                (self.env.ref('zoom_integration.sale_agregar_metodo_envio_view_form').id, 'form'),
            ],
            'type': 'ir.actions.act_window',
            'context': { }
        }


