        
    var map = L.map('map').setView([21.028, 105.804], 13);
        
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    // Parse the CSV file using PapaParse
    Papa.parse('data_bds_total.csv', {
        download: true,
        header: true,
        complete: function(results) {
            results.data.forEach(function(location) {
                var coords = location.coor.split(' ');
                var latitude = parseFloat(coords[0]);
                var longitude = parseFloat(coords[1]);

                var marker = L.marker([latitude, longitude]).addTo(map);
                marker.bindPopup(`<b>${location.title}</b>`);

                // Add click event listener to open the modal with detailed info
                marker.on('click', function() {
                    $('#locationName').text(location.title);
                    $('#locationAddress').text(location.address);
                    $('#locationBedroom').text(location.bedroom);
                    $('#locationBathroom').text(location.bathroom);
                    $('#locationPrice').text(location.price);
                    $('#locationDescription').text(location.description);
                    $('#detailsModal').modal('show');
                });
            });
        }
    });
