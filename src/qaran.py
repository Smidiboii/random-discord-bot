import requests
import random

# Quran API base URL
QURAN_API_BASE_URL = 'http://api.alquran.cloud/v1'

# Function to fetch a random ayah
def get_random_ayah(editions=['quran-uthmani', 'en.asad']):
    total_verses = 6236
    random_verse = random.randint(1, total_verses)
    verses = {}
    for edition in editions:
        endpoint = f'{QURAN_API_BASE_URL}/ayah/{random_verse}/{edition}'
        response = requests.get(endpoint)
        data = response.json()
        verse_text = data['data']['text']
        verses[edition] = verse_text
    return verses
