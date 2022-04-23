from abc import ABC
from bs4 import BeautifulSoup
import requests


def get_html(url) -> str:
    response = requests.get(url)

    if response.status_code == 200:
        return response.text

    else:
        raise Exception(f"[{response.status_code}] Couldnt GET html for {url} ")


def get_json(url):
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

    else:
        raise Exception(f"[{response.status_code}] Couldnt GET json for {url} ")


def validate_tags(*args):
    for tag in args:
        if tag is None:
            return False

    return True


class Newspaper(ABC):
    def __init__(self, name: str):
        self.name = name
        self.parser = BeautifulSoup

    def __repr__(self) -> str:
        return f"> {self.name}"

    def last_news(self, limit: int = 10):
        pass
