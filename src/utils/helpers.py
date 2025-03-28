def show_error(message):
    print(f"Error: {message}")

def format_party_details(party_details):
    return {
        "id_party": party_details.get("id_party"),
        "title": party_details.get("title", "Unknown Party"),
        "grid_size": party_details.get("grid_size", 10),
        "max_players": party_details.get("max_players", 8),
        "current_players": party_details.get("current_players", 0),
        "max_turns": party_details.get("max_turns", 30),
        "turn_duration": party_details.get("turn_duration", 60),
        "villagers_count": party_details.get("villagers_count", 0),
        "werewolves_count": party_details.get("werewolves_count", 0)
    }