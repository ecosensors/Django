app.component('station',{
    delimiters: ['[{', '}]'],
    template: `

        <div v-show="map">
         <h4>[{ title }] </h4>
         <button v-on:click="showImage()" v-bind:class="[displayImage ? 'activeButton' : 'notActiveButton']">Show image</button>
         <button v-on:click="hideImage()" v-bind:class="[displayImage ? 'notActiveButton' : 'activeButton']">Hide image</button>
         <button @mouseover="showImage()">On Over Show image</button>
         <button @mouseover="hideImage()">On Over Hide image</button>
         <div v-show="bestseller">Best seller</div>
         <figure v-show="displayImage">
            <img class="img-fluid rounded" v-bind:src="image" v-bind:alt="station_name"/>
            <figcaption>[{ station_name }] [{ station_lat }], [{ station_lng }] alt: [{ station_alt }]</figcaption>
        </figure>
        <ul>
            <li v-for="sonde in sondes">[{ sonde.name }] [{ sonde.unit }]</li>
        </ul>
        </div>

    `,
    props: {
        bestseller: {
            type: Boolean,
        }
    },
    data: function(){
        return {
            station_name : "S_tation 1",
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
                    name : "T_empérature",
                    unit : "°C",
                },
                {
                    id : 2,
                    name : "P_ression",
                    unit : "kPa",
                },
                {
                    id : 3,
                    name : "H_umidité",
                    unit : "%",
                },
            ]
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
})