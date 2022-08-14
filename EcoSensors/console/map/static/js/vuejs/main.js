/*
* Vue JS
*/
const app = Vue.createApp({
    delimiters: ['[{', '}]'],
    data: function(){
        return {
            bestSellerProduct : true,
            /*
            station_name : "Station 1",
            station_lat: 46.187164,
            station_lng: 5.997526,
            station_alt: 560,
            //image : "../static/images/stations/station-1.jpg",
            image : "https://bud.eco-sensors.ch/img/stations/station-21.jpg",
            displayImage : true,
            map : true,
            sondes : [
                {
                    id : 1,
                    name : "Température",
                    unit : "°C",
                },
                {
                    id : 2,
                    name : "Pression",
                    unit : "kPa",
                },
                {
                    id : 3,
                    name : "Humidité",
                    unit : "%",
                },
            ]
            */
        }
    },

    methods: {
        showImage(){
            this.displayImage=true;
        },
        hideImage(){
            this.displayImage=false;
        },
    },

    computed : {
        title(){
            return this.station_name;
        },
    }

});