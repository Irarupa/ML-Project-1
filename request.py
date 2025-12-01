import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'http://quotes.toscrape.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')
data = [{'quote': q.text, 'author': a.text} for q, a in zip(quotes, authors)]

df = pd.DataFrame(data)
df.to_csv('headings.csv', index=False)  # Saves to CSV file
print("Data saved to quotes.csv")
print(df.head())
