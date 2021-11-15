import requests
from bs4 import BeautifulSoup

def crawler(url):
  html = requests.get(url)
  return html.text

def crawler_parsing(url, tag):
  html = requests.get(url)
  soup = BeautifulSoup(html.text, 'html.parser')
  select = soup.select_one(tag)

  return select.text
