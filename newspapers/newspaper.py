from abc import ABC
from bs4 import BeautifulSoup
import requests


class Newspaper(ABC):
    def __init__(self, name):
        self.name = name
        self.parser = BeautifulSoup

    def __repr__(self) -> str:
        return f"> {self.name}"

    def get_html(self, url):
        response = requests.get(url)

        if response.status_code == 200:
            return response.text

        else:
            raise Exception(f"[{response.status_code}] Couldnt GET html for {url} ")

    def last_news(self):
        pass
