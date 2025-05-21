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

# Create your views here.
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
        
        # Extract the response text
        response_text = result.text
        
        # Try to parse the JSON from the response
        try:
            # Check if the response contains code blocks
            if "```json" in response_text:
                # Extract the JSON inside the code block
                json_content = response_text.split("```json")[1].split("```")[0].strip()
                parsed_data = json.loads(json_content)
            else:
                # Try parsing the entire response as JSON
                parsed_data = json.loads(response_text)
                
            # Make sure the HTML is not escaped in the simulationContent
            if 'simulationContent' in parsed_data:
                # Ensure we're not double-escaping HTML
                parsed_data['simulationContent'] = parsed_data['simulationContent']
            
            # Return the properly formatted JSON response
            return JsonResponse(parsed_data, safe=False)
            
        except json.JSONDecodeError:
            # If JSON parsing fails, return the raw text
            return JsonResponse({'simulationContent': response_text, 'caption': 'Generated content'})
        
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
