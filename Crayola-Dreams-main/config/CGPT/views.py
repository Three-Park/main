from django.shortcuts import render 
from django.http import JsonResponse 
from typing_extensions import Text
import openai
import os

openai.api_key='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'



def get_completion(final):  
	query = openai.ChatCompletion.create( 
		model="gpt-3.5-turbo",
		messages=[
        	{'role':'user','content': final}
    	], 
		max_tokens=1024, 
		n=1, 
		stop=None, 
		temperature=0.5, 
	) 
	response = query.choices[0].message["content"]
	response=response.split('\n')
	prompts = [v for v in response if v]
	return response


def query_view(request): 
	if request.method == 'POST': 
		wdiary = request.POST.get('wdiary')
		predefined_text = '''I want you to help me make prompts for the Stable Diffusion. 
Stable Diffusion is a text-based image generation model that can create diverse and high-quality images based on users' requests. In order to get the best results from Stable diffusion, you need to follow some guidelines when composing prompts.

Here are some tips for writing prompts for Stable Diffusion:

1. Be as specific as possible in the requests. Stable diffusion handles concrete prompts better than abstract or ambiguous ones. For example, instead of “portrait of a woman,” it is better to write “portrait of a Korean woman with brown eyes and red hair in Renaissance style.”
2. Specify specific art styles or materials. If you want to get an image in a certain style or with a certain texture, then specify this in the request. For example, instead of “landscape,” it is better to write “watercolor landscape with mountains and lake."
3. Specify specific artists for reference. If you want to get an image similar to the work of some artist, then specify his name in the request. For example, instead of “abstract image,” it is better to write “abstract image in the style of Picasso.”
4. Don't use any pronouns.
5. Avoid using thesr words: in a, a, an, the, with, of, and, is, of, by
6. Weigh your keywords. You can use token:1.3 to specify the weight of keywords in your query. The greater the weight of the keyword, the more it will affect the result. For example, if you want to get an image of a cat with green eyes and a pink nose, then you can write “a cat:1.5, green eyes:1.3, pink nose:1.” This means that the cat will be the most important element of the image, the green eyes will be less important, and the pink nose will be the least important.
Another way to adjust the strength of a keyword is to use () and []. (keyword) increases the strength of the keyword by 1.1 times and is equivalent to (keyword:1.1). [keyword] reduces the strength of the keyword by 0.9 times and corresponds to (keyword:0.9).

You can use several of them, as in algebra... The effect is multiplicative.
(keyword): 1.1
((keyword)): 1.21
(((keyword))): 1.33

Similarly, the effects of using multiple [] are as follows
[keyword]: 0.9
[[keyword]]: 0.81
[[[keyword]]]: 0.73

I will also give some examples of good prompts for Stable Diffusion so that you can study them and focus on them.
Here are Examples.

Examples:
a cute kitten made out of metal, (cyborg:1.1), ([tail | detailed wire]:1.3), (intricate details), hdr, (intricate details, hyperdetailed:1.2), cinematic shot, vignette, centered

medical mask, victorian era, cinematography, intricately detailed, crafted, meticulous, magnificent, maximum details, extremely hyper aesthetic

a Korean girl, wearing a tie, cupcake in her hands, school, indoors, (soothing tones:1.25), (hdr:1.25), (artstation:1.2), dramatic, (intricate details:1.14), (hyperrealistic 3d render:1.16), (filmic:0.55), (rutkowski:1.1), (faded:1.3)

Jane Eyre with headphones, natural skin texture, 24mm, 4k textures, soft cinematic light, adobe lightroom, photolab, hdr, intricate, elegant, highly detailed, sharp focus, ((((cinematic look)))), soothing tones, insane details, intricate details, hyperdetailed, low contrast, soft cinematic light, dim colors, exposure blend, hdr, faded

a portrait of a laughing, toxic, muscle, god, elder, (hdr:1.28), bald, hyperdetailed, cinematic, warm lights, intricate details, hyperrealistic, dark radial background, (muted colors:1.38), (neutral colors:1.2)

My query may be in other languages. In that case, Your answer is exclusively in English (IMPORTANT!!!), since the model only understands English.
Also, you should not copy my request directly in your response, you should compose a new one, observing the format given in the examples. Finally, give three prompts always. Insert two empty lines after the end of each prompt.
Don't add your comments. you must answer right away.
my query is : '''
		combined_text=f"{predefined_text}+{wdiary}"
		response = get_completion(combined_text)
		return JsonResponse({'response': response}) 