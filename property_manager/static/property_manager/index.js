console.log("Maps Script Started");


var map = L.map('map').setView([16.775485625052898, 96.16007953078017], 15);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

var cur_markers = [];
property_list.forEach(element => {
    element.marker = L.marker([element["lat"], element["long"]]).addTo(map)
    element.marker.bindPopup(`Price: ${element["price"]}<br>Type: ${element["type_name"]}`); 
    
});


geoJson = L.geoJson(ygn_townships, {style: {dashArray: '10', fillOpacity: 0, onEachFeature:onEachFeature}}).addTo(map);
var popup = L.popup();
function highlightFeature(e) {
    var layer = e.target;

    layer.setStyle({
        weight: 5,
        color: '#005',
        dashArray: '',
        fillOpacity: 0.7
    });

    layer.bringToFront();
}
function resetHighlight(e) {
    var layer = e.target;
    layer.setStyle({
        weight: 0,
        dashArray: '5',
        fillOpacity: 0
    })
}

function zoomToFeature(e) {
    map.fitBounds(e.target.getBounds());
    e.target.bindPopup(e.target.feature.properties.name).openPopup();
}

function onEachFeature(feature, layer) {
    layer.on({
        mouseover: highlightFeature,
        mouseout: resetHighlight,
        click: zoomToFeature
    });
}
geoJson = L.geoJson(ygn_townships, {style: {dashArray: '10', fillOpacity: 0}, onEachFeature:onEachFeature}).addTo(map);

document.getElementById("type").addEventListener("change", e=>{
    console.log(e.target.value);
    markers.data.map(ele=>{
        if(e.target.value=="all"){
            map.addLayer(ele.marker);
        }
        else if(ele.type!=e.target.value){
            map.removeLayer(ele.marker);
        }
        else{
            map.addLayer(ele.marker);
        }
    })
});