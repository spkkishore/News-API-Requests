import requests

def get_news(topic, from_date, to_date, language='en', api_key='f54b6b10dbd4436bad820e62175f789c'):
  url = f'https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={to_date}&sortBy=popularity&language={language}&apiKey={api_key}'
  r = requests.get(url)
  content = r.json()
  articles = content['articles']
  results = []
  for article in articles:
    results.append(f"'TITLE\n', {article['title']}, '\nDESCRIPTION\n', {article['description']}")
  return results

print(get_news(topic='space', from_date='2022-4-27', to_date='2022-4-28'))