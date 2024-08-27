function convertTemperature() {
    const temp = parseFloat(document.getElementById('inputTemp').value);
    const fromUnit = document.getElementById('fromUnit').value;
    const toUnit = document.getElementById('toUnit').value;

    if (isNaN(temp)) {
        alert('Por favor, insira um valor numérico para a temperatura.');
        return;
    }

    let result;

    // Conversão para Celsius
    if (fromUnit === 'C') {
        if (toUnit === 'F') {
            result = temp * 9/5 + 32;
        } else if (toUnit === 'K') {
            result = temp + 273.15;
        } else {
            result = temp; // Convertendo para Celsius
        }
    }
    
    // Conversão para Fahrenheit
    else if (fromUnit === 'F') {
        if (toUnit === 'C') {
            result = (temp - 32) * 5/9;
        } else if (toUnit === 'K') {
            result = (temp - 32) * 5/9 + 273.15;
        } else {
            result = temp; // Convertendo para Fahrenheit
        }
    }
    
    // Conversão para Kelvin
    else if (fromUnit === 'K') {
        if (toUnit === 'C') {
            result = temp - 273.15;
        } else if (toUnit === 'F') {
            result = (temp - 273.15) * 9/5 + 32;
        } else {
            result = temp; // Convertendo para Kelvin
        }
    }

    document.getElementById('result').innerText = `Resultado: ${result.toFixed(2)} ${toUnit}`;
}
