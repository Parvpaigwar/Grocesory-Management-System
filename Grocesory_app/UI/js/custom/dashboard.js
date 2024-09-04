$(function () {
    const orderListApiUrl = 'http://127.0.0.1:5000/getallorders'; // Ensure this URL is correct

    // Json data by api call for order table
    $.get(orderListApiUrl, function (response) {
        console.log("API Response:", response); // Debug the response
        if (response) {
            var table = '';
            var totalCost = 0;
            $.each(response, function (index, order) {
                console.log("Order:", order); // Debug each order
                totalCost += parseFloat(order.total);
                table += '<tr>' +
                    '<td>' + order.datetime + '</td>' +
                    '<td>' + order.order_id + '</td>' +
                    '<td>' + order.customer_name + '</td>' +
                    '<td>' + order.total.toFixed(2) + ' Rs</td></tr>';
            });
            table += '<tr><td colspan="3" style="text-align: end"><b>Total</b></td><td><b>' + totalCost.toFixed(2) + ' Rs</b></td></tr>';
            $("table").find('tbody').empty().html(table);
        }
    }).fail(function (jqXHR, textStatus, errorThrown) {
        console.error("API Request Failed:", textStatus, errorThrown); // Handle errors
    });
});
