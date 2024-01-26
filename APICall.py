import requests
import json

# Specify the URL of your Flask API endpoint
api_url = "http://52.45.65.107:5000/generate"  # Replace with your actual URL

# Input text for testing

input_text = "كان العلماء يعتقدون أن أصغرَ جزء في العناصر هو الذرة حتى القرن التاسع عشر، ثم اكتشفوا أن الذرة تحتوي على أجزاء مكونة لها أصغر منها: 1ـ البروتون 2ـ النيترون 3ـ"" الإلكترون، وبواسطة هذه الأجزاء اخترعوا القنبلة الذرية والهيدروجينية. قال تعالى: ﴿ وَمَا يَعْزُبُ عَنْ رَبِّكَ مِنْ مِثْقَالِ ذَرَّةٍ فِي الْأَرْضِ وَلَا فِي السَّمَاءِ وَلَا أَصْغَرَ مِنْ ذَلِكَ وَلَا أَكْبَرَ إِلَّا فِي كِتَابٍ مُبِينٍ ﴾ [يونس: 61]؛ (التبيان للصابوني صـ 129)."""

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
