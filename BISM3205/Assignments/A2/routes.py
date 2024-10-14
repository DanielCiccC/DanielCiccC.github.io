import requests


base_url = "https://alexpudmenzky.com/BISM3205/"

letters_left = ['F', 'G', 'J', 'Q', 'R', 'V', 'W', 'Z']


for letter1 in letters_left:
    for letter2 in letters_left:
        url = base_url + letter1 + letter2 + 'code.zip'
        try:
            response = requests.get(url)
            # Check if the response status code is 200 (OK)
            if response.status_code == 200:
                print(f"Valid route found: {url}")
            else:
                print(f"Route not found: {url} (Status code: {response.status_code})")
        except requests.exceptions.RequestException as e:
            print(f"Error accessing {url}: {e}")
