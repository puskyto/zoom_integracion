# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.osv import expression
from requests import post
import requests
import json

class ZoomSaleOrder(models.Model):
    _name = 'sale.order.zoom'

    coste = fields.Integer()
    mansaje = fields.Char()

    metodo = fields.Many2one('zoom.gettipotarifa')
    modalidad_tarifa = fields.Many2one('zoom.getmodalidadtarifa')
    ciudad_remitente = fields.Many2one('zoom.getciudadestarifa')
    ciudad_destinatario = fields.Many2one('zoom.getciudadestarifa')
    tipo_envio = fields.Many2one('zoom.gettipoenvio')
    oficina_retirar = fields.Integer()
    
    persona_contacto = fields.Integer()
    sele_rif_ci_pa = fields.Char()
    rif_ci_pa = fields.Char()
    sele_celular = fields.Char()
    celular = fields.Char()
    telefono = fields.Char()
    

    def get_tipo_tarifa(self):
        return 1
    def get_mod_tarifa(self):
        return 1
    def get_ciudades(self):
        return 1
    def get_oficina(self):
        return 1
    def get_paises(self):
        return 1
    def get_tipo_envio(self):
        return 1
    
    def obtener_tarifa(self):
        headers = {"Content-Type": "application/json"}
        url = 'http://sandbox.grupozoom.com/baaszoom/public/canguroazul/CalcularTarifa'
        data = {}
        req_values = {'tipo_tarifa': self.metodo, 
                'modalidad_tarifa': self.modalidad_tarifa,
                'ciudad_remitente': self.ciudad_remitente,
                'ciudad_destinatario': self.ciudad_destinatario,
                'oficina_retirar': self.oficina_retirar,
                'cantidad_piezas': 0,
                'peso': 0, 
                'valor_mercancia': 0,
                'valor_declarado': 0}
        data['data'] = [req_values]
        json_data = req_values
        post_request = None
        #headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        try:
            r = requests.get(url,json=json_data, headers=headers)
            #rs = json.loads(r)
            mensaje = json.loads(r.text)
            #self.codigo = mensaje['mensaje']
            self.mansaje = mensaje['mensaje']
            coste_list = len(mensaje['entidadRespuesta']['total'])
            for i in coste_list:
                self.coste = len(i['total'])
        except Exception as err:
                print(err)
        return self.show_view('Generado', self._name, 'zoom_integration.sale_agregar_metodo_envio_view_form', self.id)        
    
    
    
    
    
    def guardar(self):
        return True
            
            
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