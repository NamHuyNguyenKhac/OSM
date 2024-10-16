$(document).ready(function() {

    var map = L.map('map').setView([21.028, 105.804], 15);
        
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

        // Fetch CSV data and render it in the table
        $.getJSON('/get_csv_data', function(data) {
            var tableBody = $('#csvDataBody');
            data.forEach(function(row) {
                var rowHtml = '<tr>' +
                    '<td>' + row.name + '</td>' +
                    '<td>' + row.coordinates + '</td>' +
                    '<td>' + row.address + '</td>' +
                    '<td>' + row.bedroom + '</td>' +
                    '<td>' + row.bathroom + '</td>' +
                    '<td>' + row.price + '</td>' +
                    '<td>' + row.description + '</td>' +
                '</tr>';
                tableBody.append(rowHtml);
            });
        });
    });