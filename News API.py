import requests
def get_news(topic, from_date, to_date, language='en',
            api_key='352b1e1cc0da4b53ac149272afece376'):
  url = f'https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={to_date}&sortBy=popularity&language={language}&apiKey={api_key}'
  r = requests.get(url)
  content = r.json()
  articles = content['articles']
  results = []
  for article in articles:
    results.append(f"TITLE\n'{article['title']}, '\nDESCRIPTION\n', {article['description']}")
  return results

# NOTE: Change the from_date and to_date below to reflect recent dates
# Otherwise, you will get an error.
print(get_news(topic='space', from_date='2024-07-16', to_date='2024-07-17'))



