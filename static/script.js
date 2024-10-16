// Initialize the map centered at Hanoi's coordinates
var map = L.map('map').setView([21.0285, 105.8542], 13);

// Add OpenStreetMap tiles
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// Define the markers data passed from Flask
var markers = {{ markers|tojson }};

// Loop through the markers and add them to the map
markers.forEach(function(marker) {
    var leafletMarker = L.marker([marker.latitude, marker.longitude]).addTo(map);
    leafletMarker.bindPopup(
        "<b>" + marker.title + "</b><br>" +
        "Area: " + marker.area + " m²<br>" +
        "Bedrooms: " + marker.bedroom + "<br>" +
        "Bathrooms: " + marker.bathroom + "<br>" +
        "Price: " + marker.price + "<br>" +
        "Description: " + marker.description
    );
});