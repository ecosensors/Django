//import { latLng } from './leaflet.js';
// import { LMap, LTileLayer, LMarker, LPopup, LTooltip } from "/static/js/leaflet-1-8-0/vue2-leaflet.min.js";

app.component('carte',{
    name: "Example",

    components: {
    /*
        'l-map': window.Vue2Leaflet.LMap,
        
        LMap,
        LTileLayer,
        LMarker,
        LPopup,
        LTooltip,
        */
    },

    delimiters: ['[{', '}]'],
    template: `grrr

          <l-map style="height: 300px" :zoom="zoom" :center="center">
            <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
            <l-marker :lat-lng="markerLatLng"></l-marker>
          </l-map>

    `,

    data: function(){
        return {
            url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
            attribution:'&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors',
            zoom: 15,
            center: [51.505, -0.159],
            markerLatLng: [51.504, -0.159],
        }
    },
    methods: {
    },
})
