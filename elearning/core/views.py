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

def index(request):
    return render(request, 'index.html')


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

