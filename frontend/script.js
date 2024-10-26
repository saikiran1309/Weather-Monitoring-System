// fetchWeatherForCity
async function fetchWeatherForCity(city) {
    try {
        const response = await fetch(`/weather/${city}`);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        // Fetch forecast data
        const forecastResponse = await fetch(`/forecast/${city}`);
        if (!forecastResponse.ok) {
            throw new Error(`HTTP error! status: ${forecastResponse.status}`);
        }
        const forecastData = await forecastResponse.json();
        displayWeatherData(data, city);
        displayForecastData(forecastData);
    } catch (error) {
        console.error('Error fetching weather data:', error);
        document.getElementById('weather-data').innerHTML = `<p>Error fetching weather data for ${city}. Please try again later.</p>`;
    }
}

// displayWeatherData
function displayWeatherData(data, city) {
    const weatherDiv = document.getElementById('weather-data');
    weatherDiv.innerHTML = ''; // Clear existing content

    if (!data) {
        weatherDiv.innerHTML = `<p>No weather data available for ${city}.</p>`;
        return;
    }
    // Add global dropdown for temperature conversion first
    const tempDropdown = document.createElement('div');
    tempDropdown.className = 'temp-dropdown';
    tempDropdown.innerHTML = `
        <label for="global-temp-unit"></label>
        <select id="global-temp-unit" onchange="handleGlobalTemperatureConversion()">
            <option value="C">Celsius</option>
            <option value="K">Kelvin</option>
            <option value="F">Fahrenheit</option>
        </select>
    `;
    weatherDiv.appendChild(tempDropdown); // Append dropdown to the top
    const entryDiv = document.createElement('div');
    entryDiv.className = 'weather-entry';
    entryDiv.innerHTML = `
        <h2>${city}</h2>
        <p><strong>Avg. Temperature:</strong> <span class="current-temp" data-temp-c="${data.temp}">${data.temp} °C</span></p>
        <p><strong>Max. Temperature:</strong> <span class="max-temp" data-temp-c="${data.max_temp !== undefined ? data.max_temp : 'N/A'}">${data.max_temp !== undefined ? data.max_temp + ' °C' : 'N/A'}</span></p>
        <p><strong>Min. Temperature:</strong> <span class="min-temp" data-temp-c="${data.min_temp !== undefined ? data.min_temp : 'N/A'}">${data.min_temp !== undefined ? data.min_temp + ' °C' : 'N/A'}</span></p>
        <p><strong>Condition:</strong> ${data.condition}</p>
        <p><strong>Feels Like:</strong> <span class="feels-like" data-temp-c="${data.feels_like}">${data.feels_like} °C</span></p>
        <p><strong>Humidity:</strong> ${data.humidity !== undefined ? data.humidity + '%' : 'N/A'}</p>
        <p><strong>Wind Speed:</strong> ${data.wind_speed !== undefined ? data.wind_speed + ' km/h' : 'N/A'}</p>
        <p><strong>Last Updated:</strong> ${new Date(data.timestamp).toLocaleString()}</p>
    `;
    weatherDiv.appendChild(entryDiv); // Append weather data below the dropdown
}

// displayForecastData
function displayForecastData(forecastData) {
    const forecastDiv = document.getElementById('forecast-data');
    forecastDiv.innerHTML = ''; // Clear existing content
    // Create and append an input box for next 5 days data
    const inputDiv = document.createElement('div');
    inputDiv.className = 'forecast-input';
    inputDiv.innerHTML = `
    <div class="f-title">
        <label>Weather Forecast</label>
    </div>
    `;
    forecastDiv.appendChild(inputDiv); // Append input box to the top
    if (!forecastData || forecastData.length === 0) {
        forecastDiv.innerHTML = `<p>No forecast data available.</p>`;
        return;
    }
    forecastData.forEach(forecast => {
        const entryDiv = document.createElement('div');
        entryDiv.className = 'forecast-entry';
        entryDiv.innerHTML = `
            <p><strong>Date:</strong> ${forecast.date}</p>
            <p><strong>Temperature:</strong> <span class="forecast-temp" data-temp-c="${forecast.temp}">${forecast.temp} °C</span></p>
            <p><strong>Condition:</strong> ${forecast.condition}</p>
        `;
        forecastDiv.appendChild(entryDiv);
    });
}

// handleGlobalTemperatureConversion
function handleGlobalTemperatureConversion() {
    const selectedUnit = document.getElementById('global-temp-unit').value;
    // Convert current temperature
    const currentTempElement = document.querySelector('.current-temp');
    const maxTempElement = document.querySelector('.max-temp');
    const minTempElement = document.querySelector('.min-temp');
    const feelsLikeElement = document.querySelector('.feels-like');
    // Convert the current temperatures
    convertTemperature(currentTempElement, selectedUnit);
    convertTemperature(maxTempElement, selectedUnit);
    convertTemperature(minTempElement, selectedUnit);
    convertTemperature(feelsLikeElement, selectedUnit);
    // Convert forecast temperatures
    const forecastTemps = document.querySelectorAll('.forecast-temp');
    forecastTemps.forEach(tempElement => convertTemperature(tempElement, selectedUnit));
}

// convertTemperature
function convertTemperature(tempElement, selectedUnit) {
    const tempInCelsius = parseFloat(tempElement.getAttribute('data-temp-c'));
    let convertedValue;
    switch (selectedUnit) {
        case 'K':
            convertedValue = tempInCelsius + 273.15;
            tempElement.textContent = `${convertedValue.toFixed(2)} °K`;
            break;
        case 'F':
            convertedValue = (tempInCelsius * 9 / 5) + 32;
            tempElement.textContent = `${convertedValue.toFixed(2)} °F`;
            break;
        case 'C':
        default:
            tempElement.textContent = `${tempInCelsius} °C`;
            break;
    }
}
