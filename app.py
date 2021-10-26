from flask import Flask, render_template, request
from werkzeug.wrappers import response
import requests
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html.j2')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        pokemon_name = request.form.get('pokemon-name')
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'
        response = requests.get(url)
        if response.ok:
            stats = {
                "name": response.json()["forms"][0]["name"],
                "hp": response.json()["stats"][0]["base_stat"],
                "defense": response.json()["stats"][2]["base_stat"],
                "attack": response.json()["stats"][1]["base_stat"],
                "shiny": response.json()["sprites"]["front_shiny"]
                }
            print(stats)
            return render_template('search.html.j2', stats=stats)
    return render_template('search.html.j2')