<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Car Insurance Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        .vehicle-details {
            margin-bottom: 20px;
            padding: 10px;
            border: 1px solid #ccc;
        }
        .vehicle-details h3 {
            margin-top: 0;
        }
    </style>
</head>

# Car Insurance Form
<form id="insurance-form">
    <div id="vehicles-container"></div>
    <button type="button" onclick="addVehicle()">Add Vehicle</button>
    <button type="submit">Submit</button>
</form>

<script>
    let vehicleCount = 0;

    function addVehicle() {
        vehicleCount++;
        const vehicleContainer = document.getElementById('vehicles-container');
        
        const vehicleDetails = document.createElement('div');
        vehicleDetails.className = 'vehicle-details';
        vehicleDetails.innerHTML = `
            <h3>Vehicle ${vehicleCount}</h3>
            <label for="make-${vehicleCount}">Make:</label>
            <input type="text" id="make-${vehicleCount}" name="make-${vehicleCount}" required><br>
            <label for="model-${vehicleCount}">Model:</label>
            <input type="text" id="model-${vehicleCount}" name="model-${vehicleCount}" required><br>
            <label for="year-${vehicleCount}">Year:</label>
            <input type="number" id="year-${vehicleCount}" name="year-${vehicleCount}" required><br>
            <label for="mileage-${vehicleCount}">Mileage:</label>
            <input type="number" id="mileage-${vehicleCount}" name="mileage-${vehicleCount}" required><br>
            <label for="excess-${vehicleCount}">Excess Type:</label>
            <input type="text" id="excess-${vehicleCount}" name="excess-${vehicleCount}" required><br>
        `;
        
        vehicleContainer.appendChild(vehicleDetails);
    }

    document.getElementById('insurance-form').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent the form from submitting the default way
            
            // Create a FormData object from the form
            const formData = new FormData(event.target);

            // Send the form data using fetch
            fetch('http://127.0.0.1:5000/healthcheck', { // Replace with your server endpoint
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(response => console.log(response))
            .then(data => {
                // Redirect to another local page after successful submission
                window.location.href = '/module1.html'; // Replace with your local page
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
</script>