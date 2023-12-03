from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view

import config
import requests
import re
from googletrans import Translator

from transformers import pipeline

def translate_text(text, target_language='ru'):
    try:
        translator = Translator()
        translation = translator.translate(text, dest=target_language)
        return translation.text

    except Exception as e:
        print(f"Error: {e}")
        return None
    
def extract_video_id(url):
    pattern = r'(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})'
    match = re.search(pattern, url)
    
    if match:
        video_id = match.group(1)
        return video_id
    else:
        return None
    
def get_youtube_thumbnail(video_id):
    base_url = "https://www.googleapis.com/youtube/v3/videos"
    params = {
        'id': video_id,
        'key': config.API_KEY,
        'part': 'snippet',
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if 'items' in data and data['items']:
        thumbnail_url = data['items'][0]['snippet']['thumbnails']['medium']['url']
        return thumbnail_url
    else:
        return None
    
@api_view(['POST'])
def img_text(request):
    video_url = request.data.get('video_url')
    video_id = extract_video_id(video_url)
    thumbnail_url = get_youtube_thumbnail(video_id)
    if thumbnail_url:
        image_to_text = pipeline("image-to-text", model="nlpconnect/vit-gpt2-image-captioning")
        text = image_to_text(thumbnail_url)[0]['generated_text']
        ruText = translate_text(text)
        response_data = {
            'text': ruText
        }
        return JsonResponse(response_data)
    else:
        print("Превью не найдено.")
        return JsonResponse({'error': 'Failed to get the preview.'}, status=400)