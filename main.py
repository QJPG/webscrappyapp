import requests
import bs4

class Scrappy:
	def __init__(self) -> None:
		pass

	def get_url(self, url: str):
		return requests.get(url).content
		pass

	def get_content(self, contents):
		return bs4.BeautifulSoup(contents, "html.parser")
		pass

scr = Scrappy()
print(scr.get_content(scr.get_url("https://www.google.com")))