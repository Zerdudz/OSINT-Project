var map = L.map('map').setView([46.603354, 1.888334], 6); // Centre la carte sur la France

var oms = new OverlappingMarkerSpiderfier(map, {
    keepSpiderfied: true,
    nearbyDistance: 50
});

oms.addListener('mouseover', function(marker) {
    popup.setContent(marker.desc);
    popup.setLatLng(marker.getLatLng());
    map.openPopup(popup);
});

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
}).addTo(map);

var markers = [];

document.getElementById('search-form-strava').addEventListener('submit', function(e) {
    e.preventDefault();

    var query = document.getElementById('query-input-country-strava').value;

    // Afficher le spinner et l'overlay
    document.getElementById('loading-spinner').style.display = 'block';
    document.getElementById('overlay').style.display = 'block';

    fetch('/search_strava', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: 'query=' + encodeURIComponent(query)
        })
        .then(response => response.json())
        .then(data => {
            // Placer les points sur la carte pour chaque annonce
            var stravaIcon = L.icon({
                iconUrl: 'static/img/strava_pin.png',
                iconSize: [45, 45],
                iconAnchor: [22.5, 45],
                popupAnchor: [0, -45]
            });
            data.items.forEach(item => {
                var marker = L.marker([item.coordinates.lat, item.coordinates.lng], {
                        icon: stravaIcon
                    }).addTo(map)
                    .bindPopup(`<a href="${item.url}" target="_blank"><b>${item.nom}</b><br><img src="${item.image_url}" width="200"><br>${item.location}<br></a>`);
                oms.addMarker(marker);



                marker.on('mouseover', function(e) {
                    this.openPopup();
                });


                markers.push(marker); // ajoute le marqueur à la liste
            });

            // Cacher le spinner et l'overlay
            document.getElementById('loading-spinner').style.display = 'none';
            document.getElementById('overlay').style.display = 'none';
        });
});


document.getElementById('search-form-paruvendu').addEventListener('submit', function(e) {
    e.preventDefault();

    var query = document.getElementById('query-input-marque-paru').value;

    // Afficher le spinner et l'overlay
    document.getElementById('loading-spinner').style.display = 'block';
    document.getElementById('overlay').style.display = 'block';

    fetch('/search_paruvendu', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: 'query=' + encodeURIComponent(query)
        })
        .then(response => response.json())
        .then(data => {
            // Placer les points sur la carte pour chaque annonce
            var paruvendu_Icon = L.icon({
                iconUrl: 'static/img/paruvendu_pin.png',
                iconSize: [45, 45],
                iconAnchor: [22.5, 45],
                popupAnchor: [0, -45]
            });
            data.items.forEach(item => {
                var marker = L.marker([item.coordinates.lat, item.coordinates.lng], {
                        icon: paruvendu_Icon
                    }).addTo(map)
                    .bindPopup(`<a href="${item.url}" target="_blank"><b>${item.titre}</b><br><img src="${item.image_url}" width="200"><br>${item.location}<br></a>`);
                oms.addMarker(marker);
                marker.on('mouseover', function(e) {
                    this.openPopup();
                });

                markers.push(marker); // ajoute le marqueur à la liste
            });

            // Cacher le spinner et l'overlay
            document.getElementById('loading-spinner').style.display = 'none';
            document.getElementById('overlay').style.display = 'none';
        });
});


document.getElementById('search-form-finishers').addEventListener('submit', function(e) {
    e.preventDefault();

    var query = document.getElementById('query-input-pays-finishers').value;

    // Afficher le spinner et l'overlay
    document.getElementById('loading-spinner').style.display = 'block';
    document.getElementById('overlay').style.display = 'block';

    fetch('/search_finishers', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: 'query=' + encodeURIComponent(query)
        })
        .then(response => response.json())
        .then(data => {
            // Placer les points sur la carte pour chaque annonce
            var finishers_Icon = L.icon({
                iconUrl: 'static/img/finishers_pin.png',
                iconSize: [45, 45],
                iconAnchor: [22.5, 45],
                popupAnchor: [0, -45]
            });
            data.items.forEach(item => {
                var marker = L.marker([item.coordinates.lat, item.coordinates.lng], {
                        icon: finishers_Icon
                    }).addTo(map)
                    .bindPopup(`<a href="${item.url}" target="_blank"><b>${item.nom}</b><br><img src="${item.image_url}" width="200"><br>${item.location}<br>${item.date}<br></a>`);
                oms.addMarker(marker);
                marker.on('mouseover', function(e) {
                    this.openPopup();
                });

                markers.push(marker); // ajoute le marqueur à la liste
            });

            // Cacher le spinner et l'overlay
            document.getElementById('loading-spinner').style.display = 'none';
            document.getElementById('overlay').style.display = 'none';
        });
});