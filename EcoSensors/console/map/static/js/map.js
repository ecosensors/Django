/*
* Leaflet
*/


/*
const attribution = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
const map = L.map('map')
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { attribution: attribution }).addTo(map);
map.fitWorld();
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


// Projet 2
const copy = "© <a href='https://www.openstreetmap.org/copyright'>OpenStreetMap</a> contributors";
const url = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png";
const osm = L.tileLayer(url, { attribution: copy });
const map = L.map("map", { layers: [osm] });
map.
    locate() // Try to locate the user position
    .on("locationfound", (e) => map.setView(e.latlng, 8))
    .on("locationerror", () => map.setView([46.184610, 6.008253], 13)); // If not found, diplay taht position


async function load_markers() {
    const markers_url = `/api/map/?in_bbox=${map.getBounds().toBBoxString()}`;
    console.log("markers_url: ",markers_url);
    const response = await fetch(markers_url);
    console.log("response: ",response);
    const geojson = await response.json();
    console.log("geojson: ",geojson);
    return geojson;
}

async function render_markers() {
    const markers = await load_markers();
    console.log("Markers:",markers);
    L.geoJSON(markers).addTo(map);
    //.bindPopup((layer) => layer.feature.properties.name)

}

map.on("moveend", render_markers);



/*
if($("#map").length > 0)
{
    // Initiate the map
    var map = L.map('map').setView([46.184610, 6.008253], 13);
    // Add a layer with the openstreetmap
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '© OpenStreetMap'
    }).addTo(map);


    // Add a marker
    var allMarkers=[];
    // Faire une loop pour optenir les latlong des stations selon le field
    // allMarkers.push(L.latLng(data.properties[i]['la'], data.properties[i]['lo']));
    // fermer la loop

    var marker = L.marker([46.186090, 5.997505]).addTo(map);

}
*/