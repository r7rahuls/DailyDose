import requests
from homepage.models import NewsArticle

def fetch_news():
    
    # replace YOUR_API_KEY with your NewsAPI key
    api_key = "YOUR_API_KEY"

    # define the API endpoint and categories
    url = "https://newsapi.org/v2/top-headlines"
    categories = ["business", "general", "health", "sports", "technology"]

    for category in categories :
        params = {"apiKey": api_key, "country": "in", "language": "en", "category": category, "pageSize": 1}
        response = requests.get(url, params=params)
    

        if response.status_code == 200:
            data = response.json()
            articles = data["articles"]
            for article in articles:
                #print(article)
                # create a NewsArticle object and save it to the database
                news_article = NewsArticle(
                    title=article["title"],
                    description=article["description"],
                    url=article["url"],
                    news_category=category
            
                )
                news_article.save()
                print(f'{category} news stored successfully')
        else:
            print("Error fetching news:", response.status_code)