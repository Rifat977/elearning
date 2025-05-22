from django.shortcuts import render
from django.http import JsonResponse
import requests
import json
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import html

import google.generativeai as genai

genai.configure(api_key="AIzaSyDmHRsU9WuC_LXmWpJcF84rp4f3E7lot5o")
model = genai.GenerativeModel(model_name="gemini-2.0-flash")


def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'index.html')

def myth_check(request):
    return render(request, 'myth_check.html')

@csrf_exempt
@require_http_methods(["GET"])
def generate_simulation(request):
    query = request.GET.get('query', '')
    if not query:
        return JsonResponse({'error': 'Query parameter is required'}, status=400)
    
    try:
        result = model.generate_content(query)
        
        response_text = result.text
        
        try:
            if "```json" in response_text:
                json_content = response_text.split("```json")[1].split("```")[0].strip()
                parsed_data = json.loads(json_content)
            else:
                parsed_data = json.loads(response_text)
                
            if 'simulationContent' in parsed_data:
                parsed_data['simulationContent'] = parsed_data['simulationContent']
            
            return JsonResponse(parsed_data, safe=False)
            
        except json.JSONDecodeError:
            return JsonResponse({'simulationContent': response_text, 'caption': 'Generated content'})
        
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def fact_check_prompt(user_query):
    return f'''
আপনি একজন তথ্য যাচাইকারী বিশেষজ্ঞ। নিচের প্রশ্ন বা দাবিটি যাচাই করুন এবং বাংলায় নিচের ফরম্যাটে JSON আকারে উত্তর দিন:

{{
  "question": "{user_query}",
  "claim": "মূল দাবিটি সংক্ষেপে লিখুন (বাংলায়)",
  "verdict": "সত্য" বা "মিথ্যা" বা "আংশিক সত্য",  # এক শব্দে
  "trustScore": 0-100,  # শতাংশে নির্ভরযোগ্যতার স্কোর
  "sources": [
    {{"title": "উৎসের নাম", "snippet": "সংক্ষিপ্ত তথ্য", "url": "https://..."}},
    ...
  ],
  "finalComment": "চূড়ান্ত মন্তব্য (বাংলায়)",
  "funFact": "প্রাসঙ্গিক মজার তথ্য (বাংলায়)",
  "imageUrl": "ঐচ্ছিক, প্রাসঙ্গিক ছবি URL"
}}

কমপক্ষে ৩টি নির্ভরযোগ্য উৎস ব্যবহার করুন (যেমন WHO, FDA, Wikipedia, ইত্যাদি)।
উত্তরটি অবশ্যই শুধুমাত্র JSON আকারে দিন, কোনো ব্যাখ্যা ছাড়াই।
'''



@csrf_exempt
@require_http_methods(["POST", "GET"])
def fact_check_api(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode('utf-8'))
            user_query = data.get('query', '')
        except Exception:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    else:
        user_query = request.GET.get('query', '')

    if not user_query:
        return JsonResponse({'error': 'Query parameter is required'}, status=400)

    prompt = fact_check_prompt(user_query)
    try:
        result = model.generate_content(prompt)
        response_text = result.text
        try:
            if "```json" in response_text:
                json_content = response_text.split("```json")[1].split("```", 1)[0].strip()
                parsed_data = json.loads(json_content)
            else:
                parsed_data = json.loads(response_text)
            # Ensure required fields exist
            if 'trustScore' not in parsed_data:
                parsed_data['trustScore'] = 0
            if 'verdict' not in parsed_data:
                parsed_data['verdict'] = ''
            if 'sources' not in parsed_data:
                parsed_data['sources'] = []
            return JsonResponse(parsed_data, safe=False)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Could not parse Gemini response', 'raw': response_text}, status=500)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def role_play(request):
    return render(request, 'role_play.html')

# ```roleplay as scientists: form hypotheses, test ideas, analyze results.


# Solve the case: “{Why are fish dying in a river?}”

# Choose hypothesis → test with virtual data → get result

def role_play_prompt(user_query):
    return f'''
Roleplay as scientists: form hypotheses, test ideas, analyze results.

Solve this case: “{user_query}”

Choose hypothesis → test with virtual data → get result

'''

def role_play_api(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode('utf-8'))
            user_query = data.get('query', '')
        except Exception:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    else:
        user_query = request.GET.get('query', '')

    if not user_query:
        return JsonResponse({'error': 'Query parameter is required'}, status=400)
    
    