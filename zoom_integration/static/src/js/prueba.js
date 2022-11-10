odoo.define('zoom_integration.payment', function(require) {
    "use strict";

    var ajax = require('web.ajax');

    $.ajax({
        url: 'http://test.etravelsmart.com/etsAPI/api/getStations',
        dataType: 'json',
        username: '*****',
        password: '****'
      }).done(function(result) {
        // etc
      }).fail(function(jqXHR, textStatus, errorThrown) {
        console.error(textStatus, errorThrown)
      })

});