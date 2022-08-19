/*
* Leaflet
*/

/*
// Project 1
const attribution = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
const map = L.map('map')
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { attribution: attribution }).addTo(map);

const markers = JSON.parse(document.getElementById('markers-data').textContent);
console.log("mmm: ",markers);
let feature = L.geoJSON(markers).bindPopup(function (layer) { return layer.feature.properties.name; }).addTo(map);
console.log("mmm2: ",feature);
map.fitBounds(feature.getBounds(), { padding: [100, 100] });
*/
/*
map.
    locate() // Try to locate the user position
    .on("locationfound", (e) => map.setView(e.latlng, 8))
    .on("locationerror", () => map.setView([46.184610, 6.008253], 13)); // If not found, diplay taht position
*/

// Projet 2
const copy = "© <a href='https://www.openstreetmap.org/copyright'>OpenStreetMap</a> contributors";
const url = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png";
const osm = L.tileLayer(url, { attribution: copy });

latlng = L.latLng(46.184610, 6.008253);
const map = L.map("map", {center: latlng, layers: [osm] });
//console.log("getBounds: ",map.getBounds().toBBoxString())

var markers = L.markerClusterGroup({
    spiderfyOnMaxZoom: false,
    showCoverageOnHover: false
});

render_markers();

async function load_markers() {
    iid = 4;
    //const markers_url = `/api/map/?in_bbox=${map.getBounds().toBBoxString()}`;
    //const markers_url = `/api/map/?in_bbox=${"2"}`;
    //const markers_url = `/api/map/2/`;
    const markers_url = `/api/map/1/`;
    console.log("markers_url: ",markers_url);
    const response = await fetch(markers_url);
    //console.log("response: ",response);
    const geojson = await response.json();
    console.log("geojson: ",geojson);
    return geojson;
}

async function render_markers() {
    const marker_s = await load_markers();

    /*
    * Leaflet.markercluster
    */
    var geoJsonLayer = L.geoJson(marker_s, {
	    onEachFeature: function (feature, layer) {
		    layer.bindPopup(feature.properties.station_longname);
		}
	});

    markers.addLayer(geoJsonLayer);
    map.addLayer(markers);

    /*
    * Get the marker lat/lng to have all stations centralized in the map frame
    */
    var boundsMarkers = []; // Get all lat and lng of markers
    for (var i = 0; i < marker_s['features'].length ; i++){
        lat = marker_s['features'][i].geometry.coordinates[1];
        lng = marker_s['features'][i].geometry.coordinates[0];
        //console.log("lat: ", lat, "lng: ", lng);
        boundsMarkers.push(L.latLng(lat, lng));
    }

    bounds = L.latLngBounds(boundsMarkers);
    map.fitBounds(bounds,{ padding: [10, 10] });

    /*
    // Keep for record
    L.geoJson(marker_s)
    .bindPopup((layer) => layer.feature.properties.station_longname)
    .addTo(map);
    */

}

//map.on("moveend", render_markers);

