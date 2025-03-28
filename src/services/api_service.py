import requests
from utils.constants import BASE_URL

def list_parties():
    try:
        response = requests.get(f"{BASE_URL}/list_parties")
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Unable to retrieve parties. Code: {response.status_code}"}
    except Exception as e:
        return {"error": f"Connection error: {e}"}

def get_party_details(party_id):
    try:
        response = requests.get(f"{BASE_URL}/party_details/{party_id}")
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Unable to retrieve party details. Code: {response.status_code}"}
    except Exception as e:
        return {"error": f"Connection error: {e}"}

def subscribe_to_party(player, id_party, role_preference):
    data = {
        "player": player,
        "id_party": id_party,
        "role_preference": role_preference
    }
    try:
        response = requests.post(f"{BASE_URL}/subscribe", json=data)
        if response.status_code == 200:
            return response.json().get("response", {})
        else:
            return {"error": f"Unable to subscribe to party. Code: {response.status_code}"}
    except Exception as e:
        return {"error": f"Connection error: {e}"}