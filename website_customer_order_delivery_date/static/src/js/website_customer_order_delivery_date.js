odoo.define('website_customer_order_delivery_date.payment', function(require) {
    "use strict";

    var ajax = require('web.ajax');
    var data = { tipo_busqueda: '1',
                codigo: '71090585',
                codigo_cliente: '407940'};



    $(document).ready(function() {
        try {
            $("#delivery_date").datepicker({
                minDate: new Date()
            });
        } catch (e) {}

        $("#delivery_date_icon").click(function(){
            $('#delivery_date').datepicker('show');
        });

        $("button#o_payment_form_pay_2").bind("click", function(ev) {

            //data.push({ tipo_busqueda: '1',
              //          codigo: '71090585',
                 //       codigo_cliente: '407940'});


                var request = new XMLHttpRequest()

                 request.open('GET', 'http://sandbox.grupozoom.com/baaszoom/public/canguroazul/CalcularTarifa?tipo_tarifa=1&modalidad_tarifa=2&ciudad_remitente=1&ciudad_destinatario=19&oficina_retirar=46&cantidad_piezas=5&peso=10&valor_mercancia=1000&valor_declarado=0', true)
                 request.send()
                 
                 request.onload = function() {
                   // Begin accessing JSON data here
                   var data = JSON.parse(this.response)
                 
                   if (request.status >= 200 && request.status < 400) {
                  
                   } else {   console.log('error')  }
                 }
                 


                $(".mypanel").html(function getRandom() {
                    return Math.random();
                  })
            
            
            
            //var customer_order_delivery_date = $('#delivery_date').val();
           // var customer_order_delivery_comment = $('#delivery_comment').val();
           // ajax.jsonRpc('/shop/customer_order_delivery', 'call', {
           //     'delivery_date': customer_order_delivery_date,
           //     'delivery_comment': customer_order_delivery_comment
           // });
        });
    });

});