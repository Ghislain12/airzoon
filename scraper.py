from flask import Flask, render_template, jsonify
import requests
from bs4 import BeautifulSoup
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/alert")
def show_alert():
    url = "https://www.sxmcyclone.com"

    try:
        response = requests.get(url)
        response.raise_for_status()

        # Parser le contenu HTML
        soup = BeautifulSoup(response.text, "html.parser")

        # Trouver le tableau
        table = soup.find("table", class_="tablepress tablepress-id-59")
        if not table:
            return {"error": "Le tableau n'a pas été trouvé."}

        # Initialiser un dictionnaire pour stocker les données
        data = {}

        # Parcourir chaque ligne du tableau
        for row in table.find_all("tr"):
            cells = row.find_all("td")
            if len(cells) >= 2:  # S'assurer qu'il y a au moins deux colonnes
                key = cells[0].get_text(strip=True)  # La première colonne est la clé
                values = [
                    cell.get_text(strip=True) for cell in cells[1:]
                ]  # Les autres colonnes sont les valeurs
                data[key] = (
                    values if len(values) > 1 else values[0]
                )  # Si une seule valeur, ne pas utiliser de liste

        return jsonify(data)

    except requests.RequestException as e:
        return {"error": f"Erreur lors de la récupération des données : {e}"}


if __name__ == "__main__":
    app.run(debug=True)
