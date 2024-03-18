import requests

def get_random_wikipedia_page():
    # Wikipedia API endpoint for fetching a random page
    api_url = "https://en.wikipedia.org/w/api.php?action=query&list=random&rnnamespace=0&format=json"

    try:
        # Sending a GET request to the Wikipedia API
        response = requests.get(api_url)
        response.raise_for_status()

        # Extracting the title of the random page from JSON response
        data = response.json()
        random_page_title = data["query"]["random"][0]["title"]

        # Constructing the URL of the random page
        page_url = f"https://en.wikipedia.org/wiki/{random_page_title.replace(' ', '_')}"

        return random_page_title, page_url
    except requests.exceptions.RequestException as e:
        print("Error fetching random Wikipedia page:", e)
        return None, None
