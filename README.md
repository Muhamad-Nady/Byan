# Tbyan

## this project detect shobhat in The Holy Quran.


Project Description:
The goal of the project is to identify shobhat in The Holy Quran.

Implementation Steps:

Create Flask Server:
Develop a Flask server to handle POST requests for the API.
The server should be capable of receiving text input for analysis.

API Functionality:
Implement an API endpoint that analyzes the input text to determine if it contains shobha or not.
The API should return a JSON object containing information about whether the input text has misconceptions and provide corrections if needed.

Amazon EC2 Instance:
Set up an Amazon EC2 instance to host the Flask server.
Upload the Flask application files to the EC2 instance.

Security Group Configuration:
Configure the security group associated with the EC2 instance.
Open necessary ports, such as "custom https," "http," and "http," to allow communication with the Flask API.

Deploy and Run:
Upload the Flask application files to the EC2 server.
Execute the Flask server on the EC2 instance.

API Call:
Make API calls to the deployed server, providing input text to detect shobhat.
Retrieve the API response, which should include information about whether the text contains misconceptions and any corrections suggested.
