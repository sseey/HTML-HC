document.getElementById("calculate-bmi").addEventListener("click", function() {
    const height = document.getElementById("height").value;
    const weight = document.getElementById("weight").value;

    fetch("/bmi", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ height: parseFloat(height), weight: parseFloat(weight) })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").innerText = `Your BMI is: ${data.bmi}`;
    })
    .catch(error => {
        console.error("Error:", error);
    });
});

document.getElementById("calculate-bmr").addEventListener("click", function() {
    const height = document.getElementById("height").value;
    const weight = document.getElementById("weight").value;
    const age = document.getElementById("age").value;
    const gender = document.getElementById("gender").value;

    fetch("/bmr", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ height: parseFloat(height), weight: parseFloat(weight), age: parseInt(age), gender })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").innerText = `Your BMR is: ${data.bmr}`;
    })
    .catch(error => {
        console.error("Error:", error);
    });
});
