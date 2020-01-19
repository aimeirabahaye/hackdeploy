function initMap(lat, long){
    var container = L.DomUtil.get('mapid'); 
    if(container != null){ container._leaflet_id = null; }

    mymap = L.map('mapid').setView([lat, long], 10);
    L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoiYWltZWlyYWJhIiwiYSI6ImNrNWt6MzBlcjBqZ2QzZG92eGx4MG45ZTYifQ.XW3NLlwzdDfNu2S8cO_vjQ', {
    attribution: '',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    accessToken: 'your.mapbox.access.token'
}).addTo(mymap);
L.marker([lat, long]).addTo(mymap);
}