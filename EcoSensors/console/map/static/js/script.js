$(document).ready(function(){
    var mychart=null;
    /*
    * Chartjs
    */
    var chart = $("#charts");
    if(chart.length > 0){
        show_graph(chart);
    }

})

function show_graph(chart){
        console.log("DEBUG: show_graph")
        var sensors=[];
        var idsensors=[];

        if(chart.length > 0){
            /*
            * Show all sensors measure for a station
            * See: station.html template
            * See: station view
             */
            if(chart.attr('data-chart')=="station")
            {
                console.log("VIEW: station");
                $('#charts .container').each(function(){
                    l_abels=[];
                    d_ata=[];
                    unit="";
                    sensor_id_class = 'sensor-' + $(this).attr('data-idsensor');

                    // Collect sensor datas/values
                    $('.' + sensor_id_class + ' .data').each(function(){
                        //console.log("\tx: ",$(this).data('x'));
                        l_abels.push($(this).data('x'));
                        //console.log("\ty: ",$(this).data('y'));
                        d_ata.push(parseFloat($(this).data('y').replaceAll(',', '.')).toFixed(2));
                    });

                    // Collect sensors features
                    var features = $('.' + sensor_id_class + ' .features');
                    unit = features.data('unit');

                    datasets = [{
                        label : features.data('sensor_longname'),
                        data : d_ata,
                        borderColor: "rgba(" + features.data('bordercolor') + ",1)",
                        backgroundColor: "rgba(" + features.data('backgroundcolor') + ",1)",
                        type: features.data('chart_style'),
                        borderWidth: features.data('chart_borderwidth'),
                        showLine: features.data('showline'),
                        pointHoverRadius: features.data('chart_pointhoverradius'),
                        pointRadius: features.data('chart_pointradius'),
                        fill: features.data('chart_fill'),
                    }]
                    datas = {
                      labels: l_abels,
                      datasets : datasets,
                    };

                    $('#' + sensor_id_class).remove();
                    $('div.' + sensor_id_class +' div.container-sensor').append('<canvas class="canvas" id="' + sensor_id_class + '"></canvas>');

                    var ctx = document.getElementById(sensor_id_class).getContext('2d');
                    var conf = config(datas, unit);
                    mychart = new Chart(ctx, conf);

                })
            }
            else
            {
                console.log("VIEW: We are not in the station view");
            }

            /*
            * Show a sensor measure for a station
            * See: sensor.html template
            * See: sensor view
            */
            if(chart.attr('data-chart')=="sensor")
            {
                console.log("VIEW: sensor");
                l_abels=[];
                d_ata=[];
                unit="";

                // Collect sensor datas/values
                    $('#charts .sensor .data').each(function(){
                        //console.log("\tx: ",$(this).data('x'));
                        l_abels.push($(this).data('x'));
                        //console.log("\ty: ",$(this).data('y'));
                        d_ata.push(parseFloat($(this).data('y').replaceAll(',', '.')).toFixed(2));
                    });

                    // Collect sensors features
                    var features = $('.sensor .features');
                    unit = features.data('unit');

                    datasets = [{
                        label : features.data('sensor_longname'),
                        data : d_ata,
                        borderColor: "rgba(" + features.data('bordercolor') + ",1)",
                        backgroundColor: "rgba(" + features.data('backgroundcolor') + ",1)",
                        type: features.data('chart_style'),
                        borderWidth: features.data('chart_borderwidth'),
                        showLine: features.data('showline'),
                        pointHoverRadius: features.data('chart_pointhoverradius'),
                        pointRadius: features.data('chart_pointradius'),
                        fill: features.data('chart_fill'),
                    }]
                    datas = {
                      labels: l_abels,
                      datasets : datasets,
                    };

                    console.log("datas:", datas)

                    $('#sensor').remove();
                    $('div.sensor div.container-sensor').append('<canvas class="canvas" id="sensor"></canvas>');

                    var ctx = document.getElementById('sensor').getContext('2d');
                    var conf = config(datas, unit);
                    mychart = new Chart(ctx, conf);

            }
            else
            {
                console.log("VIEW: We are not in the sensor view");
            }
        }
        else
        {
            console.log("DEBUG: Not charts for this page ");
        }

    }


    function config(datas, unit){
        return {
            type: 'line',
            data: datas,

            options: {
                type: 'line',
                responsive: true,
                plugins: {
                    title: {
                        display: false,
                        text: 'Chart.js Line Chart'
                    },
                },
                interaction: {
                    mode: 'index',
                    intersect: false
                },
                scales: {
                    x: {
                        type: 'time',
                        time: {
                          unit: 'day'
                        },
                        title: {
                            display: true,
                            text: 'Heure'
                        },
                        display: true,
                    },
                    y: {

                        display: true,
                        title: {
                            display: true,
                            text: unit
                        }
                    }
                }
            },
        };
    }