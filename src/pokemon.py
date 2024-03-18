import requests
import random

def get_random_pokemon():
    try:
        # Fetching data from the PokeAPI for a random Pokémon
        pokemon_id = random.randint(1, 898)  # There are 898 Pokémon in total
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
        response = requests.get(url)
        response.raise_for_status()

        # Extracting the name of the Pokémon from the JSON response
        data = response.json()
        pokemon_name = data["name"]
        # pokemon_number = data["id"]

        # Constructing the URL for the Pokémon sprite image
        sprite_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{pokemon_id}.png"

        # Remove any leading or trailing whitespace characters
        sprite_url = sprite_url.strip()

        return pokemon_name, pokemon_id, f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{pokemon_id}.png"
    except requests.exceptions.RequestException as e:
        print("Error fetching random Pokémon:", e)
        return None, None, None

