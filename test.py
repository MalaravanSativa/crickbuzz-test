import requests

url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/recent"

headers = {
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com",
        "X-RapidAPI-Key": "f8def70937msh99f17b60d1f28ddp1a3c76jsncb06b2562348"  # Replace with your RapidAPI key
    }
response = requests.get(url, headers=headers)
print(response.json())
