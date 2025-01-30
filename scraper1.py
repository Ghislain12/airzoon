import requests
from bs4 import BeautifulSoup

url = "https://www.sxmcyclone.com"

try:
    response = requests.get(url)
    response.raise_for_status()

    # Parser le contenu HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Trouver le tableau
    table = soup.find("table", class_="tablepress tablepress-id-59")
    if not table:
        print("<p>Le tableau n'a pas été trouvé.</p>")

    # Initialiser un dictionnaire pour stocker les données
    data = {}

    # Parcourir chaque ligne du tableau
    for row in table.find_all("tr"):
        cells = row.find_all("td")
        if len(cells) >= 2:  # S'assurer qu'il y a au moins deux colonnes
            key = cells[0].get_text(strip=True)  # La première colonne est la clé
            value = cells[1].get_text(strip=True)  # La deuxième colonne est la valeur
            data[key] = value

            # Si la ligne contient plus de colonnes, les ajouter également
            if len(cells) > 2:
                for i in range(2, len(cells)):
                    data[f"{key}{i}"] = cells[i].get_text(strip=True)

    # Formater les données en HTML
    html_output = "<ul>"
    for key, value in data.items():
        html_output += f"<li><strong>{key}:</strong> {value}</li>"
    html_output += "</ul>"

    print(html_output)

except requests.exceptions.RequestException as e:
    print(f"Erreur lors de la récupération de la page : {e}")
