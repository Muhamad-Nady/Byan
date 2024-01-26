from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
import google.generativeai as genai
import os
from dotenv import load_dotenv
import re
import requests
from threading import Thread


app = Flask(__name__)

load_dotenv()
gemini_api_key = os.environ.get('gemini')
genai.configure(api_key=gemini_api_key)

model = genai.GenerativeModel('gemini-pro')

few_shot = pd.read_excel("quaran_labeled.xlsx")
array_range_25 = np.arange(len(few_shot))
random_numbers = np.random.choice(array_range_25, size=7, replace=False)
few_shot_example = few_shot.iloc[random_numbers, :]
few_shot_dict = {}
for value in range(len(few_shot_example)):
    prompt = f"prompt_{value}"
    completion = f"label_{value}"
    few_shot_dict[prompt] = few_shot.iloc[value, 0]
    few_shot_dict[completion] = f"{few_shot.iloc[value, 1]} و {few_shot.iloc[value, 2]}"    # print(f"promtpt: {few_shot_dict[prompt]}")

def classify(few_shot_dict, input_text):
    few_temp = """في النص القادم بعض الامثلة لكلام عن القرأن الكريم موضح اذا كان هذا الكلام إيجابي أو سلبي {few_shot_dict}
      بناء علي الأمثلة السابقة الرجاء تحديد ما اذا كان المثال الاتي {template} ايجابي ام سلبي في حالة ان كان النص سلبي يجب الرد علي الشبهة كما موضح في الامثلة السابقة """.format(few_shot_dict=few_shot_dict,template=input_text)
    prompt :str = few_temp
    try:
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                candidate_count=1,
                max_output_tokens=1024,
                temperature=0.7
            ))
        generated_content = response.text
        return generated_content
    except Exception as e:
        print(e)
        return None

@app.route('/generate', methods=['POST'])
def generate_content():
    try:
        data = request.get_json()
        input_text = data.get('input_text', '')
        result = classify(few_shot_dict=few_shot_dict, input_text=input_text)
        if result:
            return jsonify({'result': result})
        else:
            return jsonify({'error': 'An error occurred during generation'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
