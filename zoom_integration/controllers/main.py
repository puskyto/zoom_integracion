# -*- coding: utf-8 -*-
# Part of AppJetty. See LICENSE file for full copyright and licensing details.

from datetime import datetime
from odoo import fields, http, SUPERUSER_ID, tools, _
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale


class WebsiteSaleDeliveryZoom(WebsiteSale):

    """Add Customer Order Delivery functions to the website_sale controller."""

    @http.route(['/shop/customer_order_delivery'], type='json', auth="public", methods=['POST'], website=True)
    def customer_order_delivery(self, **post):
        """ Json method that used to add a
        delivery date and/or comment when the user clicks on 'pay now' button.
        """
        if post.get('ciudad_remitente') or post.get('ciudad_destinatario') or post.get('tipo_envio') or post.get('oficina_retirar') or post.get('cantidad_piezas') or post.get('peso') or post.get('persona_contacto') or post.get('rif_ci_pa') or post.get('celular') or post.get('telefono'):
            order = request.website.sale_get_order().sudo()
            redirection = self.checkout_redirection(order)
            if redirection:
                return redirection

            if order and order.id:
                values = {}
                if post.get('ciudad_remitente'):
                    values.update(
                        {'delivery_ciudad_remitente': post.get('ciudad_remitente')})
                else:
                    values.update(
                        {'delivery_ciudad_remitente': 'No Comment'})
                    
                order.write(values)
        return True
    
class Zoom(http.Controller):
    @http.route(['/shop/payment'], type='http', auth="public", website=True)
    def zoom(self, **kw):
        print("ejecucion..................................................")
        busq = request.env['zoom.getciudadestarifa'].sudo().search()
        for r in busq:
            zoom_ciudad = r
        return http.request.render('website_sale.payment',{'zoom_ciudad':zoom_ciudad})
