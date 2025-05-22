from django.shortcuts import render,redirect

import google.generativeai as genai
import requests
import json
genai.configure(api_key="AIzaSyDmHRsU9WuC_LXmWpJcF84rp4f3E7lot5o")
model = genai.GenerativeModel(model_name="gemini-2.0-flash")

def query_ollama(model="deepseek-llm:7b"):
    url = "http://localhost:11434/api/generate"

    prompt = '''
    Generate exactly 10 unique true/false questions spanning different scientific fields (e.g., physics, biology, chemistry, astronomy, earth science, computer science, etc.). For each question, provide:

    - "question": A clear, factual statement that can be answered with true or false.
    - "answer": The correct answer, either "true" or "false" (all lowercase).
    - "explanation": A concise, single-sentence explanation justifying the answer.

    Output requirements:
    - Return only a valid JSON array of 10 objects, each with the keys: "question", "answer", and "explanation".
    - Do not include any text, commentary, or formatting outside the JSON array.
    - Ensure the JSON is properly formatted, with no trailing commas and all values as strings.
    - Do not repeat questions or use any examples from previous prompts.
    - Questions should be interesting, engaging and curious.

    Example format:
    [
      {
        "question": "Water boils at 100 degrees Celsius at standard atmospheric pressure.",
        "answer": "true",
        "explanation": "At sea level, water boils at 100°C due to atmospheric pressure."
      },
      {
        "question": "Humans have three lungs.",
        "answer": "false",
        "explanation": "Humans normally have two lungs, not three."
      }
      // ...8 more objects
    ]

    Only output the JSON array as shown above.
    '''
    
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {
            "deepthink": False  # Disable deep think
        }
    }
    response = requests.post(url, json=payload)
    # response.raise_for_status()
    return response.json()["response"]

def index_true_false_game(request):
    response = query_ollama()
    print(response)
    print(type(response))
    try:
        flashcard_data = json.loads(response)
    except json.JSONDecodeError:
        return redirect('/true_false_game/')
    print(flashcard_data)
    print(type(flashcard_data))
    for item in flashcard_data:
        item['answer'] = item['answer'].capitalize()
        item['starred'] = False
        item['seen'] = False
    return render(request, 'the_true_false_game.html',{
        'flashcards': json.dumps(flashcard_data)
    })
