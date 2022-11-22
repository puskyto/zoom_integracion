# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError
from odoo.osv import expression
from requests import post
import requests
import json

class ZoomSaleOrder(models.TransientModel):
    _inherit = 'choose.delivery.carrier'

    coste = fields.Char()
    mansaje = fields.Char()

    metodo = fields.Many2one('zoom.gettipotarifa')
    modalidad_tarifa = fields.Many2one('zoom.getmodalidadtarifa')
    ciudad_remitente = fields.Many2one('zoom.getciudadestarifa')
    ciudad_destinatario = fields.Many2one('zoom.getciudadestarifa')
    tipo_envio = fields.Many2one('zoom.gettipoenvio')
    oficina_retirar = fields.Many2one('zoom.oficinas')
    cantidad_piezas = fields.Char()
    peso = fields.Char()
    
    
    persona_contacto = fields.Integer()
    sele_rif_ci_pa = fields.Char()
    rif_ci_pa = fields.Char()
    sele_celular = fields.Char()
    celular = fields.Char()
    telefono = fields.Char()
    

  
    
    
    #@api.onchange('ciudad_destinatario')
    #def get_oficina(self):
        
      #  for r in self:
        #    variable = r.env['zoom.oficinas'].search([['code_estado', '=', self.ciudad_destinatario.code]])
        #    r.oficina_retirar = variable.name
    
    
    def obtener_tarifa(self):
        headers = {"Content-Type": "application/json"}
        url = 'http://sandbox.grupozoom.com/baaszoom/public/canguroazul/CalcularTarifa'
        data = {}
        req_values = {'tipo_tarifa': 1, 
                    'modalidad_tarifa': 2,
                    'ciudad_remitente': 1,
                    'ciudad_destinatario': 19,
                    'oficina_retirar': 46,
                    'cantidad_piezas': 1,
                    'peso': 1, 
                    'valor_mercancia': 0,
                    'valor_declarado': 0}
        data['data'] = [req_values]
        json_data = req_values
        post_request = None
        
        #headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        #try:
        coste = 0.0
        r = requests.get(url,json=json_data, headers=headers)
        #rs = json.loads(r)
        mensaje = json.loads(r.text)
        #self.codigo = mensaje['mensaje']
        self.mansaje = mensaje['mensaje']
        #prueba = json.loads(r)
        #self.coste = prueba['entidadRespuesta']['total']
        print(len(mensaje['entidadRespuesta']))
        coste = mensaje['entidadRespuesta']['total']
        self.display_price = float(coste.replace(',',''))
        self.delivery_price = float(coste.replace(',',''))
        self.order_id.write({
            'metodo': "Zoom Nacional",
            'ciudad': self.ciudad_destinatario.name,
            'oficina': self.oficina_retirar.name,
            'localidad': self.ciudad_remitente.name,
            'rif_ci_pa': self.rif_ci_pa,
            'celular': self.celular,
            'telefono': self.telefono,
            'costo': float(coste.replace(',','')),
        })
        
        #enviar data a formulario
            
        #except Exception as err:
        #    print(err)
        return self.show_view('Generado', self._name, 'delivery.choose_delivery_carrier_view_form', self.id)        
            
    def show_view(self, name, model, id_xml, res_id=None, view_mode='tree,form', nodestroy=True, target='new'):
        context = self._context
        mod_obj = self.env['ir.model.data']
        view_obj = self.env['ir.ui.view']
        module = ""
        view_id = self.env.ref(id_xml).id
        if view_id:
            view = view_obj.browse(view_id)
            view_mode = view.type
        ctx = context.copy()
        ctx.update({'active_model': model})
        res = {'name': name,
                'view_mode': view_mode,
                'view_id': view_id,
                'res_model': model,
                'res_id': res_id,
                'nodestroy': nodestroy,
                'target': target,
                'type': 'ir.actions.act_window',
                'context': ctx,
                }
        return res