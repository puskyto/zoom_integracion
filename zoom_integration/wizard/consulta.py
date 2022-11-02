# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.osv import expression
import requests
import json


class ZoomGeneConsul(models.TransientModel):
    _name = 'generar.consulta.zoom'

    Tipo_busqueda = fields.Selection([('1', 'busqueda por N de envio ZOOM'),('2', 'buscar por referencia')])
    Tipo_busqueda_int = fields.Integer()
    codigo = fields.Char()
    codigo_cliente = fields.Char()
    
    mensaje = fields.Char()
    oficina = fields.Char()
    localidad = fields.Char()
    sele_rif_ci_pa = fields.Char()
    rif_ci_pa = fields.Char()
    sele_celular = fields.Char()
    celular = fields.Char()
    telefono = fields.Char()
    costo = fields.Float()

    def consulta(self):
        headers = {"Content-Type": "application/json"}
        url = 'http://sandbox.grupozoom.com/baaszoom/public/canguroazul/getInfoTracking'
        data = {}
        req_values = {'Tipo_busqueda': 1, 
                'codigo': self.codigo,
                'codigo_cliente': self.codigo_cliente}
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
        except Exception as err:
                print(err)
        return self.show_view('Consulta Generada', self._name, 'zoom_integration.view_consulta_compute_wizard', self.id)
        #raise UserError(_("Nothing to print."))
    
    
    
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
    
    def guardar(self):
        return True