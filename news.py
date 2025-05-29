import os
import requests

api_key = os.getenv("NEWS_API_KEY")

if not api_key:
    print("ERROR: NEWS_API_KEY is not set")
    exit(1)

url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("📰 Raw JSON Response:")
    print(data)  # Add this line for debugging

    articles = data.get("articles", [])
    if not articles:
        print("No articles found.")
    with open("output.txt", "w") as f:
        for article in articles[:5]:
            f.write(f"{article['title']}\n")
    print("News headlines saved to output.txt")
else:
    print(f"Failed to fetch news: {response.status_code}, {response.text}")

