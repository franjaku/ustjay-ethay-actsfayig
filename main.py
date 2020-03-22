import os

import requests
from flask import Flask, render_template
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()


@app.route('/')
def home():
    fact = get_fact()

    response = requests.post("https://hidden-journey-62459.herokuapp.com/piglatinize/",
                             allow_redirects=False,
                             data={"input_text": fact})

    url = response.headers['Location']
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    pig_latin = soup.getText().strip('\n').split('\n')[-1]
    data = {"fact": fact,
            "pig_latin": pig_latin,
            "URL": url}

    return render_template('home.jinja2', **data)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='127.0.0.1', port=port)

