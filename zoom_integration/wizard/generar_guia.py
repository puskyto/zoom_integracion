# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.osv import expression
import requests
import json


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

    def generar_guia(self):
        headers = {"Content-Type": "application/json"}
        url = 'sandbox.grupozoom.com/baaszoom/public/guiaelectronica/generarPdfGuiaEWs'
        data = {}
        req_values = {'codcliente': "405954", 
                'clave': "456789",
                'codguia': 1000156017,}
        data['data'] = [req_values]
        json_data = req_values
        post_request = None
        #headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        
        r = requests.get(url,json=json_data, headers=headers)
        #rs = json.loads(r)
        mensaje = json.loads(r.text)
        #self.codigo = mensaje['mensaje']
        self.mansaje = mensaje["codrespuesta"]
        string = mensaje['entidadRespuesta']['guiaPDF']
        
        return 