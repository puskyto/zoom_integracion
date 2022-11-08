odoo.define('zoom_integration.payment', function(require) {
    "use strict";

    var ajax = require('web.ajax');

    $(document).ready(function() {
        $("button#o_payment_form_pay").bind("click", function(ev) {

            var delivery_ciudad_remitente = $('#ciudad_remitente').val();
            var delivery_ciudad_destinatario = $('#ciudad_destinatario').val();
            var delivery_tipo_envio = $('#tipo_envio').val();
            var delivery_oficina_retirar = $('#oficina_retirar').val();
            var delivery_cantidad_piezas = $('#cantidad_piezas').val();
            var delivery_peso = $('#peso').val();
            
            var delivery_persona_contacto = $('#persona_contacto').val();
            var delivery_rif_ci_pa = $('#rif_ci_pa').val();
            var delivery_celular = $('#celular').val();
            var delivery_telefono = $('#telefono').val();
            ajax.jsonRpc('/shop/delivery', 'call', {
                'ciudad_remitente': delivery_ciudad_remitente,
                'ciudad_destinatario': delivery_ciudad_destinatario,
                'tipo_envio': delivery_tipo_envio,
                'oficina_retirar': delivery_oficina_retirar,
                'cantidad_piezas': delivery_cantidad_piezas,
                'peso': delivery_peso,
                'persona_contacto': delivery_persona_contacto,
                'rif_ci_pa': delivery_rif_ci_pa,
                'celular': delivery_celular,
                'telefono': delivery_telefono,
            });
        });
    });

});