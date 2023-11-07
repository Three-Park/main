from django.shortcuts import render 
from django.http import JsonResponse 
import openai 
from django.conf import settings

openai.api_key = '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'

def get_completion(prompt): 
	print(prompt) 
	query = openai.Completion.create( 
		engine="text-davinci-003", 
		prompt=prompt, 
		max_tokens=1024, 
		n=1, 
		stop=None, 
		temperature=0.5, 
	) 

	response = query.choices[0].text 
	print(response) 
	return response 


def query_view(request): 
	if request.method == 'POST': 
		prompt = request.POST.get('prompt') 
		response = get_completion(prompt) 
		return JsonResponse({'response': response}) 
	return render(request, 'index.html') 
