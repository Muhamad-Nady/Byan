import requests
import json

# Specify the URL of your Flask API endpoint
api_url = "http://127.0.0.1:5000/generate"  # Replace with your actual URL

# Input text for testing

input_text = '''إِنَّ مَثَلَ عِيسَىٰ عِندَ اللَّـهِ كَمَثَلِ آدَمَ خَلَقَهُ مِن تُرَابٍ ثُمَّ قَالَ لَهُ كُن فَيَكُونُ ) [ آل عمران : 59 ] // كان يجب ان يعتبر المقام الذي يقتضي صيغة الماضي لا المضارع فيقول :قال له كن فكان'''

# Create a JSON payload
payload = {"input_text": input_text}

# Make a POST request to the API
response = requests.post(api_url, json=payload)

# Check the response status code
if response.status_code == 200:
    # Parse the JSON response
    result = response.json()
    print("Generated result:", result['result'])
else:
    print("Error:", response.text)
