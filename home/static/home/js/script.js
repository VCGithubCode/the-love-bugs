document.addEventListener('DOMContentLoaded', function () {
  var map = L.map('map').setView([51.505, -0.09], 13);
  // Add a tile layer to add to our map
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '© OpenStreetMap contributors'
  }).addTo(map);
  function addMarkers(locationOne, locationTwo, meetingDate) {
    // Clear existing markers and lines first
    map.eachLayer(function (layer) {
      if (layer instanceof L.Marker || layer instanceof L.Polyline) {
        map.removeLayer(layer);
      }
    });
   // Define a new Leaflet icon with the image of the on-fire heart emoji
  var heartIcon = L.icon({
      iconUrl: 'https://cdn.vectorstock.com/i/1000x1000/21/36/red-world-heart-vector-18152136.webp', // Replace with the path to your image
      iconSize: [32, 32], // Set the size of the icon
      iconAnchor: [16, 32], // Set the anchor point of the icon to be its bottom center
      popupAnchor: [0, -32], // Set the popup to open above the icon
  });
  // Use this icon when creating markers
  var marker1 = L.marker(locationOne, {icon: heartIcon}).addTo(map).bindPopup('My Location');
  var marker2 = L.marker(locationTwo, {icon: heartIcon}).addTo(map).bindPopup("Partner's Location");
    // Create a line between the two markers
    var latlngs = [locationOne, locationTwo];
    var polyline = L.polyline(latlngs, {color: 'blue'}).addTo(map);
    // Display meeting date when hovering over the line
    polyline.bindPopup("Meeting Date: " + meetingDate);
  }
  // Global variable for the countdown interval
  let countdownInterval;
  document.getElementById('locationsForm').addEventListener('submit', function(event) {
    event.preventDefault();
    // Assume these functions return the coordinates for the addresses
    var locOneCoords = getCoordinatesForAddress(document.getElementById('location_one').value);
    var locTwoCoords = getCoordinatesForAddress(document.getElementById('location_two').value);
    // Retrieve and format the meeting date
    var meetingDate = new Date(document.getElementById('datetime_field').value);
    var meetingDateString = meetingDate.toDateString() + ' ' + meetingDate.toLocaleTimeString();
    // Compare meetingDate with today's date
    var today = new Date();
    var isFutureMeeting = meetingDate > today;
    addMarkers(locOneCoords, locTwoCoords, isFutureMeeting ? meetingDateString : "Meeting date is in the past!");
    // Update the countdown immediately and set an interval to update it every second
    calculateCountdown(meetingDate);
    clearInterval(countdownInterval); // Clear any existing interval
    countdownInterval = setInterval(function() {
      calculateCountdown(meetingDate);
    }, 1000);
  });
  async function getCoordinatesForAddress(address) {
    const mapboxAccessToken = 'pk.eyJ1IjoidmNvbmxpbmVlZHVjYXRpb24iLCJhIjoiY2xzcWgwOWM4MDM3bDJzczB4cHc3OWc4MCJ9.0hoLrOXYccgLBU0HY5JGpA'; // Replace with your access token
    const url = `https://api.mapbox.com/geocoding/v5/mapbox.places/${encodeURIComponent(address)}.json?access_token=${mapboxAccessToken}`;
    try {
      const response = await fetch(url);
      const data = await response.json();
      if (data.features && data.features.length > 0) {
        // Get the coordinates from the first feature's center
        const [lng, lat] = data.features[0].center;
        return [lat, lng]; // Return as [latitude, longitude]
      }
      return null; // Handle no result found or other issues
    } catch (error) {
      console.error('Geocoding error:', error);
      return null; // Handle errors
    }
  }
  function calculateCountdown(meetingDate) {
    var now = new Date();
    var timeDifference = meetingDate - now;
    if (timeDifference > 0) {
      var seconds = Math.floor((timeDifference / 1000) % 60);
      var minutes = Math.floor((timeDifference / (1000 * 60)) % 60);
      var hours = Math.floor((timeDifference / (1000 * 60 * 60)) % 24);
      var days = Math.floor(timeDifference / (1000 * 60 * 60 * 24));
      document.getElementById('countdownTimer').innerText =
        `${days} days ${hours} hours ${minutes} minutes ${seconds} seconds`;
    } else {
      clearInterval(countdownInterval); // Stop countdown when date is past
      document.getElementById('countdownTimer').innerText = "Meeting time has passed.";
    }
  }
});