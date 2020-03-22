import os

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()


@app.route('/')
def home():
    return "FILL ME!"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='127.0.0.1', port=port)

