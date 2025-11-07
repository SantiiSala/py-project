import requests

def get_razas():
    url = "https://dog.ceo/api/breeds/list/all"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print("🐾 Razas de perros disponibles:")
        for raza in data["message"]:
            print("-", raza)
    else:
        print("Error al obtener las razas.")
