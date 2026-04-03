let RunSentimentAnalysis = () => {
    let textToAnalyze = document.getElementById("textToAnalyze").value;
    let responseDiv = document.getElementById("system_response");

    // Clear previous response and show loading state
    responseDiv.innerHTML = "Analyzing...";

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4) {
            if (this.status == 200) {
                // Display the successful response from server.py
                responseDiv.innerHTML = this.responseText;
                responseDiv.style.color = "#2d3748";
            } else {
                // Display generic error if something goes wrong with the request
                responseDiv.innerHTML = "Error: Could not reach the server.";
                responseDiv.style.color = "red";
            }
        }
    };
    
    // Send the GET request to the Flask route /emotionDetector
    xhttp.open("GET", "emotionDetector?textToAnalyze=" + encodeURIComponent(textToAnalyze), true);
    xhttp.send();
}